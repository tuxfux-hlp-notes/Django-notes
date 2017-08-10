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
from django.utils import timezone
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
    from django.contrib.auth.models import User

    # Processing model: blog.models.Post

    from blog.models import Post

    blog_post_1 = Post()
    blog_post_1.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'arjouth', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2017, 8, 7, 2, 5, 12, 883850, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$SElIUk5eGT9u$eFK6Zksu6eqjL3y3TwlwQTl3HkK94+S2QGz0op9XHXE=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 18, 1, 57, 17, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_1.title = u'My first blog '
    blog_post_1.text = u'Today it raining cats and dogs in Hyderabad. Seems we are going to have a mini swimming pool in hyderabad.'
    blog_post_1.created_date = dateutil.parser.parse("2017-07-18T02:24:42+00:00")
    blog_post_1.published_date = None
    blog_post_1.email = None
    blog_post_1 = importer.save_or_locate(blog_post_1)

    blog_post_2 = Post()
    blog_post_2.author =  importer.locate_object(User, "id", User, "id", 3, {'username': u'deepthi', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 3, 'is_superuser': True, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$4zyBBcbOdEoq$Yjwou5b5dT/QvG1yzfph9+Lf9Y8dJsPWcq0PAofW/iI=', 'email': u'deepthi@gmail.com', 'date_joined': datetime.datetime(2017, 7, 18, 2, 33, 32, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_2.title = u'Deepthi first blog'
    blog_post_2.text = u'Its raining heavily today too.'
    blog_post_2.created_date = dateutil.parser.parse("2017-07-18T02:34:06+00:00")
    blog_post_2.published_date = None
    blog_post_2.email = None
    blog_post_2 = importer.save_or_locate(blog_post_2)

    blog_post_3 = Post()
    blog_post_3.author =  importer.locate_object(User, "id", User, "id", 4, {'username': u'manpreeth', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 4, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$BY1tDskzSfBt$UzwjG+pDjxW03WzTdGXv4KRpKdxYi0vrFvhttY4tDHI=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 19, 1, 53, 0, 269986, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_3.title = u'Manpreeth first blog'
    blog_post_3.text = u'Seems the rain has subsided today. A very good news. I am eager to see my boss face :).'
    blog_post_3.created_date = dateutil.parser.parse("2017-07-19T01:53:54+00:00")
    blog_post_3.published_date = None
    blog_post_3.email = None
    blog_post_3 = importer.save_or_locate(blog_post_3)

    blog_post_4 = Post()
    blog_post_4.author =  importer.locate_object(User, "id", User, "id", 5, {'username': u'naresh', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 5, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$LRs1kcRyw7T2$khqfkfKwFoY13dmmAQAIqz89Tjl5VZYLgJm1v/J7CWg=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 19, 1, 53, 23, 563210, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_4.title = u'Naresh first blog'
    blog_post_4.text = u'Today i have to go to college to teach my students. Hopefully they listen to me.'
    blog_post_4.created_date = dateutil.parser.parse("2017-07-19T01:54:55+00:00")
    blog_post_4.published_date = None
    blog_post_4.email = None
    blog_post_4 = importer.save_or_locate(blog_post_4)

    blog_post_5 = Post()
    blog_post_5.author =  importer.locate_object(User, "id", User, "id", 6, {'username': u'sivaram', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 6, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$mjfxeOfEMpeb$sbCx1Of2+HkX6k5LBB3aHyv3BfFkI/OhUQR2pLKFQWs=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 19, 2, 2, 19, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_5.title = u'sivarams first blog'
    blog_post_5.text = u'Seems we have a cool climate the rest of the day. I want to relax a bit without any traffic.'
    blog_post_5.created_date = dateutil.parser.parse("2017-07-19T02:02:33+00:00")
    blog_post_5.published_date = None
    blog_post_5.email = None
    blog_post_5 = importer.save_or_locate(blog_post_5)

    blog_post_6 = Post()
    blog_post_6.author =  importer.locate_object(User, "id", User, "id", 7, {'username': u'govardhan', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 7, 'is_superuser': True, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$Gggh2BsdVNf4$R/FLei9D3H7kdLeysBO5HQ/6CwXv7d/zyg86j+6HPIY=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 25, 2, 18, 16, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_6.title = u'My first blog - govardan'
    blog_post_6.text = u'hey there this is my first post.'
    blog_post_6.created_date = dateutil.parser.parse("2017-07-25T02:22:03+00:00")
    blog_post_6.published_date = None
    blog_post_6.email = None
    blog_post_6 = importer.save_or_locate(blog_post_6)

    blog_post_7 = Post()
    blog_post_7.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'arjouth', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2017, 8, 7, 2, 5, 12, 883850, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$SElIUk5eGT9u$eFK6Zksu6eqjL3y3TwlwQTl3HkK94+S2QGz0op9XHXE=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 18, 1, 57, 17, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_7.title = u'This is my second post'
    blog_post_7.text = u'Hey there i am going over my second post.'
    blog_post_7.created_date = dateutil.parser.parse("2017-07-28T01:53:09+00:00")
    blog_post_7.published_date = None
    blog_post_7.email = u'arjouth@gmail.com'
    blog_post_7 = importer.save_or_locate(blog_post_7)

    blog_post_8 = Post()
    blog_post_8.author =  importer.locate_object(User, "id", User, "id", 3, {'username': u'deepthi', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 3, 'is_superuser': True, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$4zyBBcbOdEoq$Yjwou5b5dT/QvG1yzfph9+Lf9Y8dJsPWcq0PAofW/iI=', 'email': u'deepthi@gmail.com', 'date_joined': datetime.datetime(2017, 7, 18, 2, 33, 32, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_8.title = u'This is my second post'
    blog_post_8.text = u'Hey there i am going over my second post.'
    blog_post_8.created_date = dateutil.parser.parse("2017-07-28T01:59:29+00:00")
    blog_post_8.published_date = None
    blog_post_8.email = u'deepthi@gmail.com'
    blog_post_8 = importer.save_or_locate(blog_post_8)

    blog_post_9 = Post()
    blog_post_9.author =  importer.locate_object(User, "id", User, "id", 8, {'username': u'ramanji', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 8, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$Ks2x3Utlvvci$i0VY89tKZmVMynfxk/hFwNVqyTORWoRjFtEnvjTsN8o=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 28, 2, 10, 34, 721453, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_9.title = u'this is my first post'
    blog_post_9.text = u'i am trying to add a entry to the blog.'
    blog_post_9.created_date = dateutil.parser.parse("2017-07-28T02:10:46+00:00")
    blog_post_9.published_date = None
    blog_post_9.email = u'ramanji@khyaathi.com'
    blog_post_9 = importer.save_or_locate(blog_post_9)

    blog_post_10 = Post()
    blog_post_10.author =  importer.locate_object(User, "id", User, "id", 3, {'username': u'deepthi', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 3, 'is_superuser': True, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$4zyBBcbOdEoq$Yjwou5b5dT/QvG1yzfph9+Lf9Y8dJsPWcq0PAofW/iI=', 'email': u'deepthi@gmail.com', 'date_joined': datetime.datetime(2017, 7, 18, 2, 33, 32, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_10.title = u'this is my third post'
    blog_post_10.text = u'hey there this is my third post.'
    blog_post_10.created_date = dateutil.parser.parse("2017-07-28T02:13:50+00:00")
    blog_post_10.published_date = None
    blog_post_10.email = u'deepthi@khyaathi.com'
    blog_post_10 = importer.save_or_locate(blog_post_10)

    blog_post_11 = Post()
    blog_post_11.author =  importer.locate_object(User, "id", User, "id", 8, {'username': u'ramanji', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 8, 'is_superuser': False, 'is_staff': False, 'last_login': None, 'password': u'pbkdf2_sha256$20000$Ks2x3Utlvvci$i0VY89tKZmVMynfxk/hFwNVqyTORWoRjFtEnvjTsN8o=', 'email': u'', 'date_joined': datetime.datetime(2017, 7, 28, 2, 10, 34, 721453, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_11.title = u'Third blog '
    blog_post_11.text = u'This is my third blog.'
    blog_post_11.created_date = dateutil.parser.parse("2017-08-01T02:07:45+00:00")
    blog_post_11.published_date = None
    blog_post_11.email = u'ramanji@khyaathi.com'
    blog_post_11 = importer.save_or_locate(blog_post_11)

