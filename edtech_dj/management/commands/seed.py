from ast import Delete
import os
from django.core.management.base import BaseCommand
import random
import logging
import csv
from college.models import Branch, College, Subject, Year
from edtech_dj.settings import BASE_DIR


logger = logging.getLogger()

# path to folder containing csv files
CSV_FILES_FOLDER_PATH = "util\csv"

# python manage.py seed --mode=refresh

""" Clear all data and create new objects """
MODE_REFRESH = 'refresh'

""" Clear all data and do not create new objects """
MODE_CLEAR = 'clear'


class Command(BaseCommand):
    help = "seed database for testing and development."

    def add_arguments(self, parser):
        parser.add_argument('--mode', type=str, help="Mode")

    def handle(self, *args, **options):
        self.stdout.write('seeding data...')
        run_seed(self, options['mode'])
        self.stdout.write('done.')


def clear_data():
    """Deletes all the table data"""
    logger.info("Delete all Colleges")
    print("Delete all Colleges")
    College.objects.all().delete()
    print("Delete all Branches")
    Branch.objects.all().delete()
    print("Delete all Years")
    Year.objects.all().delete()
    print("Delete all Subjects")
    Subject.objects.all().delete()
    print("Delete all Year")
    Year.objects.all().delete()


def create_college(data):
    """Creates an address object combining different elements from the list"""
    logger.info("Creating address")

    college = College(
        **data
    )
    college.save()
    logger.info("{} address created.".format(college))
    return college


def create_branch(data):
    """Creates an address object combining different elements from the list"""
    logger.info("Creating branches")

    colleges = College.objects.filter(college_code=data['college'])
    del data['id']
    del data['college']
    del data['description']

    branch = Branch(
        **data,
    )
    branch.save()
    branch.colleges.set(colleges)
    branch.save()
    logger.info("{} address created.".format(branch))
    return branch


def run_seed(self, mode):
    # Clear data from tables
    clear_data()
    if mode == MODE_CLEAR:
        return

    print(os.path.join(BASE_DIR, CSV_FILES_FOLDER_PATH, "colleges.csv"))

    # creating colleges
    with open(os.path.join(BASE_DIR, CSV_FILES_FOLDER_PATH, "colleges.csv")) as file:
        reader = csv.DictReader(file)
        for row in reader:
            create_college(row)

    # creating branches
    with open(os.path.join(BASE_DIR, CSV_FILES_FOLDER_PATH, "branches.csv")) as file:
        reader = csv.DictReader(file)
        for row in reader:
            create_branch(row)
