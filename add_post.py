#!/usr/bin/env python3
"""
Add a new post to the BEA Designs blog.

Run this from the Python Website folder (same place as app.py):
    python3 add_post.py

It writes straight into blog.db, the same SQLite database the Flask app reads
from, so a new post shows up at /blog immediately without restarting the app.
"""
import re
from datetime import datetime

from app import app
from blog_models import db, BlogPost


def slugify(title):
    slug = title.lower().strip()
    slug = re.sub(r"[^\w\s-]", "", slug)
    slug = re.sub(r"[\s_]+", "-", slug)
    return slug.strip("-")


def main():
    print("New BEA Designs Blog Post")
    print("-" * 30)

    title = input("Title: ").strip()
    if not title:
        print("Title can't be empty. Aborting.")
        return

    excerpt = input("Short excerpt (shown on the blog list page): ").strip()

    print("Body (paste or type the post, then Ctrl-D on its own line to finish):")
    content_lines = []
    try:
        while True:
            content_lines.append(input())
    except EOFError:
        pass
    content = "\n".join(content_lines).strip()

    if not content:
        print("Post body can't be empty. Aborting.")
        return

    slug = slugify(title)

    with app.app_context():
        if BlogPost.query.filter_by(slug=slug).first():
            print(f"\nA post with slug '{slug}' already exists — use a different title.")
            return

        post = BlogPost(
            title=title,
            slug=slug,
            excerpt=excerpt,
            content=content,
            published_at=datetime.utcnow(),
        )
        db.session.add(post)
        db.session.commit()

    print(f"\nPublished. View it at /blog/{slug}")


if __name__ == "__main__":
    main()
