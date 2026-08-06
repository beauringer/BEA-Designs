from datetime import datetime

from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class BlogPost(db.Model):
    __tablename__ = 'blog_posts'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    slug = db.Column(db.String(220), unique=True, nullable=False, index=True)
    excerpt = db.Column(db.String(400))
    content = db.Column(db.Text, nullable=False)
    author = db.Column(db.String(100), default='Brent Eugene Auringer')
    published_at = db.Column(db.DateTime, default=datetime.utcnow)

    def formatted_date(self):
        return self.published_at.strftime('%B %-d, %Y')
