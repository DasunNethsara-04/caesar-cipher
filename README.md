# Caesar Cipher Project

This project implements a Caesar Cipher, a type of substitution cipher in which each letter in the plaintext is shifted a certain number of places down or up the alphabet. This README provides instructions on how to set up and run both the frontend and backend components of the project.

## Introduction

The Caesar Cipher is one of the simplest and most widely known encryption techniques. This project includes a web-based interface for encrypting and decrypting messages using the Caesar Cipher algorithm.

## Project Structure

- `frontend/`: Contains the frontend code (React, TypeScript, React Bootstrap).
- `backend/`: Contains the backend code (Python, FastAPI).

## Prerequisites

- Node.js (v14 or higher)
- npm (v6 or higher)
- Python (v3.10 or higher)
- pip

## Setup

### Frontend

1. Navigate to the `frontend` directory:

   ```sh
   cd frontend
   ```

2. Install dependencies:

   ```sh
   npm install
   ```

3. Start the frontend development server:
   ```sh
   npm run dev
   ```

### Backend

1. Navigate to the `backend` directory:

   ```sh
   cd backend
   ```

2. Create a virtual environment:

   ```sh
   python -m venv venv
   ```

3. Activate the virtual environment:

   - On Windows:
     ```sh
     venv\Scripts\activate
     ```
   - On macOS/Linux:
     ```sh
     source venv/bin/activate
     ```

4. Install dependencies:

   ```sh
   pip install -r requirements.txt
   ```

5. Start the backend server:
   ```sh
   fastapi dev app.py
   ```

## Running the Project

1. Ensure both the frontend and backend servers are running.
2. Open your web browser and navigate to `http://localhost:5173` (or the port specified in your frontend configuration).
3. Use the web interface to encrypt and decrypt messages using the Caesar Cipher.

## Contributing

Contributions are welcome! Please follow these steps to contribute:

1. Fork the repository.
2. Create a new branch (`git checkout -b feature-branch`).
3. Make your changes.
4. Commit your changes (`git commit -m 'Add some feature'`).
5. Push to the branch (`git push origin feature-branch`).
6. Open a pull request.

## Issues

If you encounter any issues, please open an issue on the repository. Provide as much detail as possible to help us resolve the problem quickly.

## Contact

For any questions or inquiries, please contact [techsaralk.pro@gmail.com].
