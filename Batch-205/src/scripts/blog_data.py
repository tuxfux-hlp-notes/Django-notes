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
# manage.py dumpscript blog
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
from django.utils import timezone

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
    from django.contrib.auth.models import User

    # Processing model: blog.models.Post

    from blog.models import Post

    blog_post_1 = Post()
    blog_post_1.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_1.email = u'rama@khyaathi.com'
    blog_post_1.title = u'my first blog'
    blog_post_1.text = u'hey my test is written from sqlite3'
    blog_post_1.created_date = dateutil.parser.parse("2017-11-17T02:06:24+00:00")
    blog_post_1.published_date = None
    blog_post_1 = importer.save_or_locate(blog_post_1)

    blog_post_2 = Post()
    blog_post_2.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_2.email = u'rama@khyaathi.com'
    blog_post_2.title = u'This is my second post'
    blog_post_2.text = u'Hey there this is my second post.'
    blog_post_2.created_date = dateutil.parser.parse("2017-11-17T02:27:11+00:00")
    blog_post_2.published_date = None
    blog_post_2 = importer.save_or_locate(blog_post_2)

    blog_post_3 = Post()
    blog_post_3.author =  importer.locate_object(User, "id", User, "id", 3, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 3, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$feEiyBWcZ85p$w06/3Wb6o6sVTr/xY1q/hUCZ1qWO7mImb0pBljtzP40=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 30, 2, 52, 58, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_3.email = None
    blog_post_3.title = u'This is my first blog - kumar'
    blog_post_3.text = u'I am trying to enter some data usign the model forms.'
    blog_post_3.created_date = dateutil.parser.parse("2017-11-30T02:53:15+00:00")
    blog_post_3.published_date = None
    blog_post_3 = importer.save_or_locate(blog_post_3)

    blog_post_4 = Post()
    blog_post_4.author =  importer.locate_object(User, "id", User, "id", 3, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 3, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$feEiyBWcZ85p$w06/3Wb6o6sVTr/xY1q/hUCZ1qWO7mImb0pBljtzP40=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 30, 2, 52, 58, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_4.email = None
    blog_post_4.title = u'hey there'
    blog_post_4.text = u'hey there.'
    blog_post_4.created_date = dateutil.parser.parse("2017-12-02T01:46:52+00:00")
    blog_post_4.published_date = None
    blog_post_4 = importer.save_or_locate(blog_post_4)

    blog_post_5 = Post()
    blog_post_5.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_5.email = None
    blog_post_5.title = u'rama - khyaathi.com'
    blog_post_5.text = u'hey i am rama from khyaathi.com'
    blog_post_5.created_date = dateutil.parser.parse("2017-12-02T01:50:17+00:00")
    blog_post_5.published_date = None
    blog_post_5 = importer.save_or_locate(blog_post_5)

    blog_post_6 = Post()
    blog_post_6.author =  importer.locate_object(User, "id", User, "id", 4, {'username': u'keethu', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 4, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$p9n5T7rvNexH$18ZZKTNFwl+CgbZfhXAwogOTucQTcsi4VR8S2MzOEd0=', 'email': u'', 'date_joined': datetime.datetime(2017, 12, 2, 1, 54, 45, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_6.email = None
    blog_post_6.title = u'keethu'
    blog_post_6.text = u'keethu'
    blog_post_6.created_date = dateutil.parser.parse("2017-12-02T01:55:02+00:00")
    blog_post_6.published_date = None
    blog_post_6 = importer.save_or_locate(blog_post_6)

    blog_post_7 = Post()
    blog_post_7.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_7.email = None
    blog_post_7.title = u'rama - without email'
    blog_post_7.text = u'hey there its rama without email.'
    blog_post_7.created_date = dateutil.parser.parse("2017-12-02T01:55:52+00:00")
    blog_post_7.published_date = None
    blog_post_7 = importer.save_or_locate(blog_post_7)

    blog_post_8 = Post()
    blog_post_8.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_8.email = None
    blog_post_8.title = u'hi'
    blog_post_8.text = u'hi'
    blog_post_8.created_date = dateutil.parser.parse("2017-12-02T01:59:57+00:00")
    blog_post_8.published_date = None
    blog_post_8 = importer.save_or_locate(blog_post_8)

    blog_post_9 = Post()
    blog_post_9.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'rama', 'first_name': u'Rama', 'last_name': u'Krishna', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': datetime.datetime(2017, 12, 8, 2, 21, 33, 636683, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8=', 'email': u'', 'date_joined': datetime.datetime(2017, 11, 17, 2, 6, 24, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_9.email = u'rama@khyaathi.com'
    blog_post_9.title = u'rama - email testing'
    blog_post_9.text = u'i am trying to check if email is getting populated.'
    blog_post_9.created_date = dateutil.parser.parse("2017-12-02T02:28:54+00:00")
    blog_post_9.published_date = None
    blog_post_9 = importer.save_or_locate(blog_post_9)

