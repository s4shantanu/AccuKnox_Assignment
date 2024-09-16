import time
import threading
import datetime
from django.db import connection, transaction
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.contrib.auth.models import User

@receiver(post_save, sender=User)
def my_signal_handler(sender, instance, **kwargs):
    print(f"Signal started at {datetime.datetime.now()}")
    time.sleep(5)
    print(f"Signal finished at {datetime.datetime.now()}")

@receiver(post_save, sender=User)
def my_signal_thread_test(sender, instance, **kwargs):
    print(f"Signal executed in thread: {threading.get_ident()}")

@receiver(post_save, sender=User)
def my_signal_transaction_test(sender, instance, **kwargs):
    with connection.cursor() as cursor:
        cursor.execute("INSERT INTO test_table (data) VALUES ('Signal executed')")
    print("Signal handler executed")



from django.apps import AppConfig

class SignalAppConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'signal_app'

    def ready(self):
        import signal_app.signals  # Import signals here
