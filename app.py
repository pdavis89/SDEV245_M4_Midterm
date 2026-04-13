from flask import Flask, render_template, request
import hashlib
from cryptography.fernet import Fernet

app = Flask(__name__)

def sha256_hash(data: bytes) -> str:
    return hashlib.sha256(data).hexdigest()

@app.route("/", methods=["GET", "POST"])
def index():
    result = None

    if request.method == "POST":
        user_input = request.form.get("message", "").encode()

        # Hash original
        original_hash = sha256_hash(user_input)

        # Generate AES key (Fernet uses AES-128 + HMAC)
        key = Fernet.generate_key()
        cipher = Fernet(key)

        # Encrypt
        encrypted = cipher.encrypt(user_input)

        # Decrypt
        decrypted = cipher.decrypt(encrypted)
        decrypted_hash = sha256_hash(decrypted)

        # Integrity check
        integrity_ok = (original_hash == decrypted_hash)

        result = {
            "original": user_input.decode(),
            "original_hash": original_hash,
            "encrypted": encrypted.decode(),
            "decrypted": decrypted.decode(),
            "decrypted_hash": decrypted_hash,
            "integrity_ok": integrity_ok,
            "key": key.decode()
        }

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run()
