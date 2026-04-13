# Crypto Demo Web App

A simple Flask web application that demonstrates SHA‑256 hashing, AES encryption, AES decryption, and integrity verification.

This app is designed to show how confidentiality, integrity, and availability (CIA triad) are upheld in a basic cryptographic workflow.

## Overview

This app allows a user to enter a message into a web form.
The backend then:

Hashes the message using SHA‑256

Encrypts the message using AES (via Fernet)

Decrypts the encrypted message

Re‑hashes the decrypted message

Compares both hashes to verify integrity

The results are displayed in a Bootstrap interface.

This makes the app a simple, visual way to understand how hashing and encryption work together to protect data.

## 🧠 How the App Works (Step‑by‑Step)

1. User enters a message
   The message is submitted through a simple HTML form.

2. The server hashes the message (SHA‑256)
   SHA‑256 produces a unique, fixed‑length fingerprint of the input.
   Even a one‑character change results in a completely different hash.

3. The server generates a symmetric AES key
   The key is created using a cryptographically secure random number generator.

4. The message is encrypted using AES
   AES (via Fernet) transforms the message into unreadable ciphertext.

5. The ciphertext is decrypted
   Using the same AES key, the original message is recovered.

6. The decrypted message is hashed again
   If the decrypted hash matches the original hash, the data was not altered.

7. All results are displayed in the UI
   The user sees:

Original message

Original SHA‑256 hash

AES key

Encrypted text

Decrypted text

Decrypted SHA‑256 hash

Integrity verification result

## Security Concepts Explained

### Confidentiality

Confidentiality ensures that only authorized parties can read the data.

In this app:

The message is encrypted using AES, a widely trusted symmetric encryption algorithm.

Without the AES key, the ciphertext is unreadable.

This protects the message from unauthorized access.

### Integrity

Integrity ensures that data has not been altered.

In this app:

The message is hashed before encryption.

After decryption, it is hashed again.

If both hashes match, the data is unchanged.

This proves the message was not tampered with during processing.

### Availability

Availability ensures that data and systems remain accessible to users with proper permissions.

In this app:

The cryptographic operations are lightweight and fast.

The app uses stable, well‑supported libraries (Flask, cryptography).

The UI is simple and reliable.

This ensures the service remains usable and responsive.

## Entropy & Key Generation

Entropy refers to the level of randomness that a key has.
High entropy that is pulled from the OS is essential for generating secure cryptographic keys.

If entropy is low:

Keys become predictable

Attackers can guess or brute‑force them

The cryptography library uses a cryptographically secure random number generator, ensuring strong entropy.

Key Generation
The AES key is generated automatically using secure randomness pulled from the OS.

A strong key:

Cannot be guessed

Cannot be derived from the ciphertext

Makes AES encryption extremely difficult to break

In short:
Good entropy → strong keys → strong encryption.

## Summary

This project is a simple but powerful demonstration of core cryptographic principles:

Hashing ensures integrity

AES encryption ensures confidentiality

Bootstrap UI ensures usability and availability

Entropy and secure key generation ensure strong protection.
