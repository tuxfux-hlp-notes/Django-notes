#!/usr/bin/env python
# -*- coding: utf-8 -*-

# This file has been automatically generated.
# Instead of changing it, create a file called import_helper.py
# and put there a class called ImportHelper(object) in it.
#
# This class will be specially casted so that instead of extending object,
# it will actually extend the class BasicImportHelper()
#
# That means you just have to overload the methods you want to
# change, leaving the other ones inteact.
#
# Something that you might want to do is use transactions, for example.
#
# Also, don't forget to add the necessary Django imports.
#
# This file was generated with the following command:
# manage.py dumpscript auth.User
#
# to restore it, run
# manage.py runscript module_name.this_script_name
#
# example: if manage.py is at ./manage.py
# and the script is at ./some_folder/some_script.py
# you must make sure ./some_folder/__init__.py exists
# and run  ./manage.py runscript some_folder.some_script
import os, sys
from django.db import transaction

class BasicImportHelper(object):

    def pre_import(self):
        pass

    @transaction.atomic
    def run_import(self, import_data):
        import_data()

    def post_import(self):
        pass

    def locate_similar(self, current_object, search_data):
        # You will probably want to call this method from save_or_locate()
        # Example:
        #   new_obj = self.locate_similar(the_obj, {"national_id": the_obj.national_id } )

        the_obj = current_object.__class__.objects.get(**search_data)
        return the_obj

    def locate_object(self, original_class, original_pk_name, the_class, pk_name, pk_value, obj_content):
        # You may change this function to do specific lookup for specific objects
        #
        # original_class class of the django orm's object that needs to be located
        # original_pk_name the primary key of original_class
        # the_class      parent class of original_class which contains obj_content
        # pk_name        the primary key of original_class
        # pk_value       value of the primary_key
        # obj_content    content of the object which was not exported.
        #
        # You should use obj_content to locate the object on the target db
        #
        # An example where original_class and the_class are different is
        # when original_class is Farmer and the_class is Person. The table
        # may refer to a Farmer but you will actually need to locate Person
        # in order to instantiate that Farmer
        #
        # Example:
        #   if the_class == SurveyResultFormat or the_class == SurveyType or the_class == SurveyState:
        #       pk_name="name"
        #       pk_value=obj_content[pk_name]
        #   if the_class == StaffGroup:
        #       pk_value=8

        search_data = { pk_name: pk_value }
        the_obj = the_class.objects.get(**search_data)
        #print(the_obj)
        return the_obj


    def save_or_locate(self, the_obj):
        # Change this if you want to locate the object in the database
        try:
            the_obj.save()
        except:
            print("---------------")
            print("Error saving the following object:")
            print(the_obj.__class__)
            print(" ")
            print(the_obj.__dict__)
            print(" ")
            print(the_obj)
            print(" ")
            print("---------------")

            raise
        return the_obj


importer = None
try:
    import import_helper
    # We need this so ImportHelper can extend BasicImportHelper, although import_helper.py
    # has no knowlodge of this class
    importer = type("DynamicImportHelper", (import_helper.ImportHelper, BasicImportHelper ) , {} )()
except ImportError as e:
    # From Python 3.3 we can check e.name - string match is for backward compatibility.
    if 'import_helper' in str(e):
        importer = BasicImportHelper()
    else:
        raise

import datetime
from decimal import Decimal
from django.contrib.contenttypes.models import ContentType

try:
    import dateutil.parser
except ImportError:
    print("Please install python-dateutil")
    sys.exit(os.EX_USAGE)

def run():
    importer.pre_import()
    importer.run_import(import_data)
    importer.post_import()

def import_data():
    # Initial Imports

    # Processing model: django.contrib.auth.models.User

    from django.contrib.auth.models import User

    auth_user_1 = User()
    auth_user_1.password = u'pbkdf2_sha256$20000$pH0MYd0HDYIO$Q619iGrtEe1jUF3hicNzAT21IPJdyEJOzzi3lgxwA28='
    auth_user_1.last_login = dateutil.parser.parse("2017-10-10T01:59:41.078801+00:00")
    auth_user_1.is_superuser = True
    auth_user_1.username = u'admin'
    auth_user_1.first_name = u''
    auth_user_1.last_name = u''
    auth_user_1.email = u'admin@gmail.com'
    auth_user_1.is_staff = True
    auth_user_1.is_active = True
    auth_user_1.date_joined = dateutil.parser.parse("2017-09-12T01:51:48.114417+00:00")
    auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$20000$6tpslaxFDeaS$K6uhG/cLQBYHHsfNjzA02Z/KScSjNIK83cDMDdStciQ='
    auth_user_2.last_login = None
    auth_user_2.is_superuser = True
    auth_user_2.username = u'manindra'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.is_staff = False
    auth_user_2.is_active = True
    auth_user_2.date_joined = dateutil.parser.parse("2017-09-15T01:50:40+00:00")
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$20000$fwpawPUQlMJx$zMHYKHy+a5bT2UceFfvOXqUduIugKt+Gq5KasdBsxVo='
    auth_user_3.last_login = dateutil.parser.parse("2017-10-09T02:19:34.469807+00:00")
    auth_user_3.is_superuser = False
    auth_user_3.username = u'anu'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.date_joined = dateutil.parser.parse("2017-09-18T02:54:25+00:00")
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$20000$nFJqxv2aKQ2b$auOuJ8IWleRG2I4X7+iqC3R3FyxBIYCVevIIWV4yLf4='
    auth_user_4.last_login = dateutil.parser.parse("2017-09-29T02:59:31.036772+00:00")
    auth_user_4.is_superuser = False
    auth_user_4.username = u'sree'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.is_staff = True
    auth_user_4.is_active = True
    auth_user_4.date_joined = dateutil.parser.parse("2017-09-24T02:27:59+00:00")
    auth_user_4 = importer.save_or_locate(auth_user_4)

    # Re-processing model: django.contrib.auth.models.User





