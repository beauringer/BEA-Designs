from flask import Flask, render_template, request, redirect, url_for, flash, abort

from blog_models import db, BlogPost

app = Flask(__name__)
app.secret_key = 'bea-designs-secret-key'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///blog.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)

with app.app_context():
    db.create_all()


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


@app.route('/blog')
def blog_list():
    posts = BlogPost.query.order_by(BlogPost.published_at.desc()).all()
    return render_template('blog_list.html', posts=posts)


@app.route('/blog/<slug>')
def blog_post(slug):
    post = BlogPost.query.filter_by(slug=slug).first()
    if post is None:
        abort(404)
    return render_template('blog_post.html', post=post)


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
