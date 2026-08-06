from flask import Flask, render_template, request, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = 'bea-designs-secret-key'


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/contact', methods=['POST'])
def contact():
    name = request.form.get('name', '')
    email = request.form.get('email', '')
    message = request.form.get('message', '')

    print(f"\n{'='*50}")
    print("NEW CONTACT FORM SUBMISSION")
    print(f"{'='*50}")
    print(f"Name:    {name}")
    print(f"Email:   {email}")
    print(f"Message: {message}")
    print(f"{'='*50}\n")

    flash('Thank you for your message! We will get back to you shortly.', 'success')
    return redirect(url_for('index', _anchor='contact'))


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)

