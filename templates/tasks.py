# tasks.py

# Import the necessary libraries and modules
import time
import requests
from celery import shared_task, Celery
from django.core.mail import send_mail
from myapp.models import (
    DataModel,
)  # Replace 'myapp' and 'DataModel' with your actual app and model names
from django.utils import timezone


# Create a shared task that performs a simple calculation
@shared_task
def add(x, y):
    """
    A basic task to add two numbers.
    This function will run in the background and return the result.
    """
    return x + y


# Task with retries for handling transient issues, such as network-related tasks
@shared_task(bind=True, max_retries=3)
def fetch_data(self, url):
    """
    Task that attempts to fetch data from an external URL.
    If it fails, it retries up to 3 times with exponential backoff.
    """
    try:
        # Simulate a data fetch from an external API or URL
        response = requests.get(url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as exc:
        # Retry the task with exponential backoff if an error occurs
        countdown = 2**self.request.retries  # Exponential backoff
        raise self.retry(exc=exc, countdown=countdown)


# Task to send an email, useful for notifications, user alerts, etc.
@shared_task
def send_welcome_email(user_id):
    """
    Sends a welcome email to a new user.
    This task fetches the user's email from the database and sends the email.
    """
    # Import the User model only when the function is called to avoid circular imports
    from django.contrib.auth.models import User

    user = User.objects.get(id=user_id)  # Fetch the user instance by ID
    send_mail(
        "Welcome to MyApp!",
        "Thanks for signing up for our service!",
        "from@example.com",  # Replace with your "from" email
        [user.email],  # Send to the user's email
        fail_silently=False,
    )


# Task to perform a scheduled database cleanup, for example, deleting old records
@shared_task
def cleanup_old_records():
    """
    Scheduled task to delete records older than 30 days from the DataModel table.
    This task can be scheduled to run periodically using Celery Beat.
    """
    threshold_date = timezone.now() - timezone.timedelta(days=30)
    # Delete records in DataModel older than 30 days
    deleted, _ = DataModel.objects.filter(created_at__lt=threshold_date).delete()
    return f"Deleted {deleted} old records"


# Long
