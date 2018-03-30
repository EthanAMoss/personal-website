from emoss_website import mail, blog_db as db
from emoss_website.models import Post
from flask_mail import Message

from .config import EMAIL_RECIPIENT, DEFAULT_EMAIL_SUBJECT, DATE_DISPLAY_FORMAT

from datetime import date, datetime
from dateutil import tz



def calculate_age(birthday):
    """Calculates the current age (in years) of the person with the given birthday"""
    today = date.today()
    age = today.year - birthday.year

    # If today's date is before birthdate, then subtract a year
    if (today.month, today.day) < (birthday.month, birthday.day):
        age = age - 1

    return age


def send_email(sender_name, sender_email, subject, body):
    # If no given subject, set to default
    if subject is None:
        subject = DEFAULT_EMAIL_SUBJECT

    # Set up message
    msg = Message(subject=subject,
                  recipients=[EMAIL_RECIPIENT],
                  body=body,
                  sender=(sender_name, sender_email),
                  reply_to=sender_email)

    # Send message
    mail.send(msg)


def get_all_blog_posts():
    posts = []

    # Get the posts from the database
    db_posts = Post.query.order_by(Post.posted_on.desc())

    # Put the post data into tuples, and then add them to the list
    for post in db_posts:
        # Convert the post datetime from UTC to local, then format it for display
        posted_on = post.posted_on

        # Setup 'initial' and 'target' time zones to convert our post's datetime to
        initial_zone = tz.tzutc()
        target_zone = tz.tzlocal()

        # Set initial timezone and get datetime based on target timezone
        posted_on = posted_on.replace(tzinfo=initial_zone)
        posted_on_local = posted_on.astimezone(target_zone)

        posts.append((post.p_id, post.title, post.author, posted_on_local.strftime(DATE_DISPLAY_FORMAT), post.body))

    return posts
