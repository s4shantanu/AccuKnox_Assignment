from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
import time
import datetime
import threading
from django.db import connection, transaction

# Signal to test synchronous execution
@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal started at {datetime.datetime.now()}")
    time.sleep(5)
    print(f"Signal finished at {datetime.datetime.now()}")

# Signal to test thread execution
@receiver(post_save, sender=User)
def my_signal_thread_test(sender, instance, **kwargs):
    print(f"Signal executed in thread: {threading.get_ident()}")

# Signal to test transaction rollback
@receiver(post_save, sender=User)
def my_signal_transaction_test(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO test_table (data) VALUES ('Signal executed')")
    print("Signal handler executed")
