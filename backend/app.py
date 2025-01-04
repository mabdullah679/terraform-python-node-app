from flask import Flask, send_from_directory, request

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def home():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    # Retrieve the user's name from the form, defaulting to 'Guest' if not provided
    user_name = request.form.get('user_name', 'Guest').strip().lower()
    # Normalize the input for consistent formatting and comparison
    formatted_name = ' '.join(word.capitalize() for word in user_name.split())
    # Remove all spaces and check against the normalized VIP names
    if user_name.replace(" ", "") in ["saadahmad", "nayabirfan"]:
        return (f"As Salam o Alaykum to Our Chief Guest, {formatted_name}<br>"
                "We hope you enjoyed this little gift from us<br>"
                "We pray for your guys' wellbeing and hope to see you soon!")
    else:
        return f"As Salam o Alaykum {formatted_name}! Welcome to our website."

if __name__ == '__main__':
    # Run the Flask app with the host set to all interfaces and debug mode enabled
    app.run(host='0.0.0.0', port=5000, debug=True)
