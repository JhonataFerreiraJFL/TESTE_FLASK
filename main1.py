from flask import Flask, request
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)

@app.route('/register', methods=['POST'])
def register():
    j = request.get_json()
    username = j['username']
    raw_password = j['password']

    # Hash the password before storing it in the database
    hashed_password = generate_password_hash(raw_password)

    # Save the username and hashed_password in the database (you need to implement this part)
    print(hashed_password)

    return f"User {username} registered successfully!"

@app.route('/login', methods=['POST'])
def login():
    j = request.get_json()
    username = j['username']
    raw_password = j['password']

    # Retrieve the hashed password from the database based on the provided username (you need to implement this part)
    hashed_password = 'pbkdf2:sha256:600000$u5si0OikyD8sMXbx$624335193b6c1c0a785452105b2b9afc0642489b8fec624c22e2b1f5451be7a4'
    # Check if the hashed password matches the raw password
    if check_password_hash(hashed_password, raw_password):
        return f"User {username} logged in successfully!"
    else:
        return "Invalid username or password."

if __name__ == "__main__":
    app.run()
