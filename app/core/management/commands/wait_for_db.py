"""
Django Commands to be used with the manage.py module
"""

from django.core.management.base import BaseCommand
import time
from psycopg2 import OperationalError as Psycopg2Error
from django.db.utils import OperationalError


class Command(BaseCommand):
    """Command to wait for DB to be available"""

    def handle(self, *args, **options):
        """Entrypoint for command."""
        self.stdout.write("Waiting for DB...")
        db_up = False
        while db_up is False:
            try:
                print("about to check_db")
                self.check(databases=["default"])
                db_up = True
            except (OperationalError, Psycopg2Error):
                self.stdout.write("DB unavailable waiting 1 second")
                time.sleep(1)
                # print(e, "operational_error")
                # print(e, "psycopg2_error")
        self.stdout.write(self.style.SUCCESS("DB available!"))
