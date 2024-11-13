# settings/celery.py
# Asynchronous task queue settings

import os

# Import the Celery class, which will be used to create a Celery application instance.
from celery import Celery

# This tells Celery which settings file to use for Django.
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "settings")

# Celery configuration:
# CELERY_TIMEZONE = "Etc/UCT"  # Optional: Define timezone for task scheduling.
CELERY_TASK_TRACK_STARTED = True  # Enables tracking of task start times.
CELERY_TASK_TIME_LIMIT = (
    3600 * 4
)  # Set a time limit (in seconds) for task execution; here it's 4 hours.
# CELERY_RESULT_BACKEND = 'django-db'  # Optional: store task results in Django's database.
# CELERY_CACHE_BACKEND = 'django-cache'  # Optional: use Django's cache system for task result storage.


# Custom Celery class to extend the parent class with overridden task name generation to simplify module paths:
class MyCelery(Celery):
    def gen_task_name(self, name, module):
        # Modify the module path by filtering out specific directories ('apps' and 'tasks') for a cleaner task name.
        # This avoids cluttering the task name with redundant parts.
        module = ".".join(
            [dir for dir in module.split(".") if dir not in ("apps", "tasks")]
        )

        # Call the parent class's 'gen_task_name' method as proxy object to generate the final task name
        # using the cleaned module path. This produces a more readable task name.
        return super().gen_task_name(name, module)


# Instantiate the Celery application with a specific name ("data" here).
celery_app = MyCelery("data")

# Configure Celery using Django settings.
# Using a string here avoids having to serialize the configuration to child processes.
# The namespace 'CELERY' means all Celery-related settings in Django should start with 'CELERY_'.
celery_app.config_from_object("django.conf:settings", namespace="CELERY")

# Automatically discover tasks in Django apps.
# This lets Celery find tasks defined in each Django app’s 'tasks.py' file.
celery_app.autodiscover_tasks()
