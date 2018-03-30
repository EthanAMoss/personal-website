from emoss_website import app, blog_db as db


class Post(db.Model):
    """
    Database model for blog posts to be displayed on this here website
    """
    __tablename__ = 'post'

    p_id = db.Column('id', db.Integer, primary_key=True)
    author = db.Column('author', db.String)
    title = db.Column('title', db.Text)
    posted_on = db.Column('posted_on', db.DateTime)
    body = db.Column('body', db.Text)
