from flask import Flask, request, send_from_directory

app = Flask(__name__, static_folder='../frontend')

@app.route('/')
def serve_frontend():
    return send_from_directory(app.static_folder, 'index.html')

@app.route('/submit', methods=['POST'])
def submit():
    user_name = request.form.get('user_name', 'Guest')
    # Capitalizes the first letter of each word
    formatted_name = ' '.join(word.capitalize() for word in user_name.split())
    return f"As Salam o Alaykum {formatted_name}! Saad Ahmad and Nayab Irfan had their Nikkah on December 27th! Please, pray for their welfare :)"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

# comment
