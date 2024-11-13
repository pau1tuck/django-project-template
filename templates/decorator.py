import time
import logging
from functools import wraps

# Set up logging configuration
logger = logging.getLogger(__name__)


def log_execution_time(func):
    """
    A custom decorator to log the execution time of a function.
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        # Start the timer before running the function
        start_time = time.time()

        # Run the original function and store its result
        result = func(*args, **kwargs)

        # Calculate the elapsed time
        end_time = time.time()
        execution_time = end_time - start_time

        # Log the execution time
        logger.info(f"{func.__name__} executed in {execution_time:.4f} seconds")

        return result  # Return the function's result

    return wrapper


# Example usage with a Django view
from django.http import HttpResponse


@log_execution_time
def my_view(request):
    """
    A sample Django view that simulates some work.
    """
    time.sleep(2)  # Simulate work by pausing for 2 seconds
    return HttpResponse("This view took some time to execute.")
