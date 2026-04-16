from flask import Flask, render_template, request, jsonify

app = Flask(__name__)

# Route for home page
@app.route('/')
def home():
    return render_template('index.html')

# Optional: Contact form handler
@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name')
    email = request.form.get('email')
    message = request.form.get('message')
    
    # For now, just print. You can add email sending later.
    print(f"Message from {name} ({email}): {message}")
    
    return jsonify({"status": "success", "message": "Thanks! I'll get back to you soon."})

if __name__ == '__main__':
    app.run(debug=True)