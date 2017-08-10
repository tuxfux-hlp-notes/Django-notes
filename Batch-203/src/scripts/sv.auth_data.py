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
# manage.py dumpscript auth
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

    # Processing model: django.contrib.auth.models.Permission

    from django.contrib.auth.models import Permission

    # auth_permission_1 = Permission()
    # auth_permission_1.name = u'Can add log entry'
    # auth_permission_1.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    # auth_permission_1.codename = u'add_logentry'
    # auth_permission_1 = importer.save_or_locate(auth_permission_1)

    # auth_permission_2 = Permission()
    # auth_permission_2.name = u'Can change log entry'
    # auth_permission_2.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    # auth_permission_2.codename = u'change_logentry'
    # auth_permission_2 = importer.save_or_locate(auth_permission_2)

    # auth_permission_3 = Permission()
    # auth_permission_3.name = u'Can delete log entry'
    # auth_permission_3.content_type = ContentType.objects.get(app_label="admin", model="logentry")
    # auth_permission_3.codename = u'delete_logentry'
    # auth_permission_3 = importer.save_or_locate(auth_permission_3)

    # auth_permission_4 = Permission()
    # auth_permission_4.name = u'Can add group'
    # auth_permission_4.content_type = ContentType.objects.get(app_label="auth", model="group")
    # auth_permission_4.codename = u'add_group'
    # auth_permission_4 = importer.save_or_locate(auth_permission_4)

    # auth_permission_5 = Permission()
    # auth_permission_5.name = u'Can change group'
    # auth_permission_5.content_type = ContentType.objects.get(app_label="auth", model="group")
    # auth_permission_5.codename = u'change_group'
    # auth_permission_5 = importer.save_or_locate(auth_permission_5)

    # auth_permission_6 = Permission()
    # auth_permission_6.name = u'Can delete group'
    # auth_permission_6.content_type = ContentType.objects.get(app_label="auth", model="group")
    # auth_permission_6.codename = u'delete_group'
    # auth_permission_6 = importer.save_or_locate(auth_permission_6)

    # auth_permission_7 = Permission()
    # auth_permission_7.name = u'Can add permission'
    # auth_permission_7.content_type = ContentType.objects.get(app_label="auth", model="permission")
    # auth_permission_7.codename = u'add_permission'
    # auth_permission_7 = importer.save_or_locate(auth_permission_7)

    # auth_permission_8 = Permission()
    # auth_permission_8.name = u'Can change permission'
    # auth_permission_8.content_type = ContentType.objects.get(app_label="auth", model="permission")
    # auth_permission_8.codename = u'change_permission'
    # auth_permission_8 = importer.save_or_locate(auth_permission_8)

    # auth_permission_9 = Permission()
    # auth_permission_9.name = u'Can delete permission'
    # auth_permission_9.content_type = ContentType.objects.get(app_label="auth", model="permission")
    # auth_permission_9.codename = u'delete_permission'
    # auth_permission_9 = importer.save_or_locate(auth_permission_9)

    # auth_permission_10 = Permission()
    # auth_permission_10.name = u'Can add user'
    # auth_permission_10.content_type = ContentType.objects.get(app_label="auth", model="user")
    # auth_permission_10.codename = u'add_user'
    # auth_permission_10 = importer.save_or_locate(auth_permission_10)

    # auth_permission_11 = Permission()
    # auth_permission_11.name = u'Can change user'
    # auth_permission_11.content_type = ContentType.objects.get(app_label="auth", model="user")
    # auth_permission_11.codename = u'change_user'
    # auth_permission_11 = importer.save_or_locate(auth_permission_11)

    # auth_permission_12 = Permission()
    # auth_permission_12.name = u'Can delete user'
    # auth_permission_12.content_type = ContentType.objects.get(app_label="auth", model="user")
    # auth_permission_12.codename = u'delete_user'
    # auth_permission_12 = importer.save_or_locate(auth_permission_12)

    # auth_permission_13 = Permission()
    # auth_permission_13.name = u'Can add post'
    # auth_permission_13.content_type = ContentType.objects.get(app_label="blog", model="post")
    # auth_permission_13.codename = u'add_post'
    # auth_permission_13 = importer.save_or_locate(auth_permission_13)

    # auth_permission_14 = Permission()
    # auth_permission_14.name = u'Can change post'
    # auth_permission_14.content_type = ContentType.objects.get(app_label="blog", model="post")
    # auth_permission_14.codename = u'change_post'
    # auth_permission_14 = importer.save_or_locate(auth_permission_14)

    # auth_permission_15 = Permission()
    # auth_permission_15.name = u'Can delete post'
    # auth_permission_15.content_type = ContentType.objects.get(app_label="blog", model="post")
    # auth_permission_15.codename = u'delete_post'
    # auth_permission_15 = importer.save_or_locate(auth_permission_15)

    # auth_permission_16 = Permission()
    # auth_permission_16.name = u'Can add content type'
    # auth_permission_16.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    # auth_permission_16.codename = u'add_contenttype'
    # auth_permission_16 = importer.save_or_locate(auth_permission_16)

    # auth_permission_17 = Permission()
    # auth_permission_17.name = u'Can change content type'
    # auth_permission_17.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    # auth_permission_17.codename = u'change_contenttype'
    # auth_permission_17 = importer.save_or_locate(auth_permission_17)

    # auth_permission_18 = Permission()
    # auth_permission_18.name = u'Can delete content type'
    # auth_permission_18.content_type = ContentType.objects.get(app_label="contenttypes", model="contenttype")
    # auth_permission_18.codename = u'delete_contenttype'
    # auth_permission_18 = importer.save_or_locate(auth_permission_18)

    # auth_permission_19 = Permission()
    # auth_permission_19.name = u'Can add registration profile'
    # auth_permission_19.content_type = ContentType.objects.get(app_label="registration", model="registrationprofile")
    # auth_permission_19.codename = u'add_registrationprofile'
    # auth_permission_19 = importer.save_or_locate(auth_permission_19)

    # auth_permission_20 = Permission()
    # auth_permission_20.name = u'Can change registration profile'
    # auth_permission_20.content_type = ContentType.objects.get(app_label="registration", model="registrationprofile")
    # auth_permission_20.codename = u'change_registrationprofile'
    # auth_permission_20 = importer.save_or_locate(auth_permission_20)

    # auth_permission_21 = Permission()
    # auth_permission_21.name = u'Can delete registration profile'
    # auth_permission_21.content_type = ContentType.objects.get(app_label="registration", model="registrationprofile")
    # auth_permission_21.codename = u'delete_registrationprofile'
    # auth_permission_21 = importer.save_or_locate(auth_permission_21)

    # auth_permission_22 = Permission()
    # auth_permission_22.name = u'Can add supervised registration profile'
    # auth_permission_22.content_type = ContentType.objects.get(app_label="registration", model="supervisedregistrationprofile")
    # auth_permission_22.codename = u'add_supervisedregistrationprofile'
    # auth_permission_22 = importer.save_or_locate(auth_permission_22)

    # auth_permission_23 = Permission()
    # auth_permission_23.name = u'Can change supervised registration profile'
    # auth_permission_23.content_type = ContentType.objects.get(app_label="registration", model="supervisedregistrationprofile")
    # auth_permission_23.codename = u'change_supervisedregistrationprofile'
    # auth_permission_23 = importer.save_or_locate(auth_permission_23)

    # auth_permission_24 = Permission()
    # auth_permission_24.name = u'Can delete supervised registration profile'
    # auth_permission_24.content_type = ContentType.objects.get(app_label="registration", model="supervisedregistrationprofile")
    # auth_permission_24.codename = u'delete_supervisedregistrationprofile'
    # auth_permission_24 = importer.save_or_locate(auth_permission_24)

    # auth_permission_25 = Permission()
    # auth_permission_25.name = u'Can add session'
    # auth_permission_25.content_type = ContentType.objects.get(app_label="sessions", model="session")
    # auth_permission_25.codename = u'add_session'
    # auth_permission_25 = importer.save_or_locate(auth_permission_25)

    # auth_permission_26 = Permission()
    # auth_permission_26.name = u'Can change session'
    # auth_permission_26.content_type = ContentType.objects.get(app_label="sessions", model="session")
    # auth_permission_26.codename = u'change_session'
    # auth_permission_26 = importer.save_or_locate(auth_permission_26)

    # auth_permission_27 = Permission()
    # auth_permission_27.name = u'Can delete session'
    # auth_permission_27.content_type = ContentType.objects.get(app_label="sessions", model="session")
    # auth_permission_27.codename = u'delete_session'
    # auth_permission_27 = importer.save_or_locate(auth_permission_27)

    # auth_permission_28 = Permission()
    # auth_permission_28.name = u'Can add article'
    # auth_permission_28.content_type = ContentType.objects.get(app_label="test_app", model="article")
    # auth_permission_28.codename = u'add_article'
    # auth_permission_28 = importer.save_or_locate(auth_permission_28)

    # auth_permission_29 = Permission()
    # auth_permission_29.name = u'Can change article'
    # auth_permission_29.content_type = ContentType.objects.get(app_label="test_app", model="article")
    # auth_permission_29.codename = u'change_article'
    # auth_permission_29 = importer.save_or_locate(auth_permission_29)

    # auth_permission_30 = Permission()
    # auth_permission_30.name = u'Can delete article'
    # auth_permission_30.content_type = ContentType.objects.get(app_label="test_app", model="article")
    # auth_permission_30.codename = u'delete_article'
    # auth_permission_30 = importer.save_or_locate(auth_permission_30)

    # auth_permission_31 = Permission()
    # auth_permission_31.name = u'Can add articles'
    # auth_permission_31.content_type = ContentType.objects.get(app_label="test_app", model="articles")
    # auth_permission_31.codename = u'add_articles'
    # auth_permission_31 = importer.save_or_locate(auth_permission_31)

    # auth_permission_32 = Permission()
    # auth_permission_32.name = u'Can change articles'
    # auth_permission_32.content_type = ContentType.objects.get(app_label="test_app", model="articles")
    # auth_permission_32.codename = u'change_articles'
    # auth_permission_32 = importer.save_or_locate(auth_permission_32)

    # auth_permission_33 = Permission()
    # auth_permission_33.name = u'Can delete articles'
    # auth_permission_33.content_type = ContentType.objects.get(app_label="test_app", model="articles")
    # auth_permission_33.codename = u'delete_articles'
    # auth_permission_33 = importer.save_or_locate(auth_permission_33)

    # auth_permission_34 = Permission()
    # auth_permission_34.name = u'Can add group'
    # auth_permission_34.content_type = ContentType.objects.get(app_label="test_app", model="group")
    # auth_permission_34.codename = u'add_group'
    # auth_permission_34 = importer.save_or_locate(auth_permission_34)

    # auth_permission_35 = Permission()
    # auth_permission_35.name = u'Can change group'
    # auth_permission_35.content_type = ContentType.objects.get(app_label="test_app", model="group")
    # auth_permission_35.codename = u'change_group'
    # auth_permission_35 = importer.save_or_locate(auth_permission_35)

    # auth_permission_36 = Permission()
    # auth_permission_36.name = u'Can delete group'
    # auth_permission_36.content_type = ContentType.objects.get(app_label="test_app", model="group")
    # auth_permission_36.codename = u'delete_group'
    # auth_permission_36 = importer.save_or_locate(auth_permission_36)

    # auth_permission_37 = Permission()
    # auth_permission_37.name = u'Can add membership'
    # auth_permission_37.content_type = ContentType.objects.get(app_label="test_app", model="membership")
    # auth_permission_37.codename = u'add_membership'
    # auth_permission_37 = importer.save_or_locate(auth_permission_37)

    # auth_permission_38 = Permission()
    # auth_permission_38.name = u'Can change membership'
    # auth_permission_38.content_type = ContentType.objects.get(app_label="test_app", model="membership")
    # auth_permission_38.codename = u'change_membership'
    # auth_permission_38 = importer.save_or_locate(auth_permission_38)

    # auth_permission_39 = Permission()
    # auth_permission_39.name = u'Can delete membership'
    # auth_permission_39.content_type = ContentType.objects.get(app_label="test_app", model="membership")
    # auth_permission_39.codename = u'delete_membership'
    # auth_permission_39 = importer.save_or_locate(auth_permission_39)

    # auth_permission_40 = Permission()
    # auth_permission_40.name = u'Can add person'
    # auth_permission_40.content_type = ContentType.objects.get(app_label="test_app", model="person")
    # auth_permission_40.codename = u'add_person'
    # auth_permission_40 = importer.save_or_locate(auth_permission_40)

    # auth_permission_41 = Permission()
    # auth_permission_41.name = u'Can change person'
    # auth_permission_41.content_type = ContentType.objects.get(app_label="test_app", model="person")
    # auth_permission_41.codename = u'change_person'
    # auth_permission_41 = importer.save_or_locate(auth_permission_41)

    # auth_permission_42 = Permission()
    # auth_permission_42.name = u'Can delete person'
    # auth_permission_42.content_type = ContentType.objects.get(app_label="test_app", model="person")
    # auth_permission_42.codename = u'delete_person'
    # auth_permission_42 = importer.save_or_locate(auth_permission_42)

    # auth_permission_43 = Permission()
    # auth_permission_43.name = u'Can add place'
    # auth_permission_43.content_type = ContentType.objects.get(app_label="test_app", model="place")
    # auth_permission_43.codename = u'add_place'
    # auth_permission_43 = importer.save_or_locate(auth_permission_43)

    # auth_permission_44 = Permission()
    # auth_permission_44.name = u'Can change place'
    # auth_permission_44.content_type = ContentType.objects.get(app_label="test_app", model="place")
    # auth_permission_44.codename = u'change_place'
    # auth_permission_44 = importer.save_or_locate(auth_permission_44)

    # auth_permission_45 = Permission()
    # auth_permission_45.name = u'Can delete place'
    # auth_permission_45.content_type = ContentType.objects.get(app_label="test_app", model="place")
    # auth_permission_45.codename = u'delete_place'
    # auth_permission_45 = importer.save_or_locate(auth_permission_45)

    # auth_permission_46 = Permission()
    # auth_permission_46.name = u'Can add publication'
    # auth_permission_46.content_type = ContentType.objects.get(app_label="test_app", model="publication")
    # auth_permission_46.codename = u'add_publication'
    # auth_permission_46 = importer.save_or_locate(auth_permission_46)

    # auth_permission_47 = Permission()
    # auth_permission_47.name = u'Can change publication'
    # auth_permission_47.content_type = ContentType.objects.get(app_label="test_app", model="publication")
    # auth_permission_47.codename = u'change_publication'
    # auth_permission_47 = importer.save_or_locate(auth_permission_47)

    # auth_permission_48 = Permission()
    # auth_permission_48.name = u'Can delete publication'
    # auth_permission_48.content_type = ContentType.objects.get(app_label="test_app", model="publication")
    # auth_permission_48.codename = u'delete_publication'
    # auth_permission_48 = importer.save_or_locate(auth_permission_48)

    # auth_permission_49 = Permission()
    # auth_permission_49.name = u'Can add reporter'
    # auth_permission_49.content_type = ContentType.objects.get(app_label="test_app", model="reporter")
    # auth_permission_49.codename = u'add_reporter'
    # auth_permission_49 = importer.save_or_locate(auth_permission_49)

    # auth_permission_50 = Permission()
    # auth_permission_50.name = u'Can change reporter'
    # auth_permission_50.content_type = ContentType.objects.get(app_label="test_app", model="reporter")
    # auth_permission_50.codename = u'change_reporter'
    # auth_permission_50 = importer.save_or_locate(auth_permission_50)

    # auth_permission_51 = Permission()
    # auth_permission_51.name = u'Can delete reporter'
    # auth_permission_51.content_type = ContentType.objects.get(app_label="test_app", model="reporter")
    # auth_permission_51.codename = u'delete_reporter'
    # auth_permission_51 = importer.save_or_locate(auth_permission_51)

    # auth_permission_52 = Permission()
    # auth_permission_52.name = u'Can add restaurant'
    # auth_permission_52.content_type = ContentType.objects.get(app_label="test_app", model="restaurant")
    # auth_permission_52.codename = u'add_restaurant'
    # auth_permission_52 = importer.save_or_locate(auth_permission_52)

    # auth_permission_53 = Permission()
    # auth_permission_53.name = u'Can change restaurant'
    # auth_permission_53.content_type = ContentType.objects.get(app_label="test_app", model="restaurant")
    # auth_permission_53.codename = u'change_restaurant'
    # auth_permission_53 = importer.save_or_locate(auth_permission_53)

    # auth_permission_54 = Permission()
    # auth_permission_54.name = u'Can delete restaurant'
    # auth_permission_54.content_type = ContentType.objects.get(app_label="test_app", model="restaurant")
    # auth_permission_54.codename = u'delete_restaurant'
    # auth_permission_54 = importer.save_or_locate(auth_permission_54)

    # auth_permission_55 = Permission()
    # auth_permission_55.name = u'Can add waiter'
    # auth_permission_55.content_type = ContentType.objects.get(app_label="test_app", model="waiter")
    # auth_permission_55.codename = u'add_waiter'
    # auth_permission_55 = importer.save_or_locate(auth_permission_55)

    # auth_permission_56 = Permission()
    # auth_permission_56.name = u'Can change waiter'
    # auth_permission_56.content_type = ContentType.objects.get(app_label="test_app", model="waiter")
    # auth_permission_56.codename = u'change_waiter'
    # auth_permission_56 = importer.save_or_locate(auth_permission_56)

    # auth_permission_57 = Permission()
    # auth_permission_57.name = u'Can delete waiter'
    # auth_permission_57.content_type = ContentType.objects.get(app_label="test_app", model="waiter")
    # auth_permission_57.codename = u'delete_waiter'
    # auth_permission_57 = importer.save_or_locate(auth_permission_57)

    # Processing model: django.contrib.auth.models.Group

    from django.contrib.auth.models import Group


    # Processing model: django.contrib.auth.models.User

    from django.contrib.auth.models import User

    # auth_user_1 = User()
    # auth_user_1.password = u'pbkdf2_sha256$20000$XrOrz28Gh0GP$Tg/d6pT86wBOzJOF33Nh6EXuiGTbSIW/XK7dlHw4gpI='
    # auth_user_1.last_login = dateutil.parser.parse("2017-08-08T01:47:22.848098+00:00")
    # auth_user_1.is_superuser = True
    # auth_user_1.username = u'admin'
    # auth_user_1.first_name = u''
    # auth_user_1.last_name = u''
    # auth_user_1.email = u'admin@gmail.com'
    # auth_user_1.is_staff = True
    # auth_user_1.is_active = True
    # auth_user_1.date_joined = dateutil.parser.parse("2017-07-13T02:03:07.418558+00:00")
    # auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$20000$SElIUk5eGT9u$eFK6Zksu6eqjL3y3TwlwQTl3HkK94+S2QGz0op9XHXE='
    auth_user_2.last_login = dateutil.parser.parse("2017-08-07T02:05:12.883850+00:00")
    auth_user_2.is_superuser = True
    auth_user_2.username = u'arjouth'
    auth_user_2.first_name = u''
    auth_user_2.last_name = u''
    auth_user_2.email = u''
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.date_joined = dateutil.parser.parse("2017-07-18T01:57:17+00:00")
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$20000$4zyBBcbOdEoq$Yjwou5b5dT/QvG1yzfph9+Lf9Y8dJsPWcq0PAofW/iI='
    auth_user_3.last_login = None
    auth_user_3.is_superuser = True
    auth_user_3.username = u'deepthi'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u'deepthi@gmail.com'
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.date_joined = dateutil.parser.parse("2017-07-18T02:33:32+00:00")
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$20000$BY1tDskzSfBt$UzwjG+pDjxW03WzTdGXv4KRpKdxYi0vrFvhttY4tDHI='
    auth_user_4.last_login = None
    auth_user_4.is_superuser = False
    auth_user_4.username = u'manpreeth'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.date_joined = dateutil.parser.parse("2017-07-19T01:53:00.269986+00:00")
    auth_user_4 = importer.save_or_locate(auth_user_4)

    auth_user_5 = User()
    auth_user_5.password = u'pbkdf2_sha256$20000$LRs1kcRyw7T2$khqfkfKwFoY13dmmAQAIqz89Tjl5VZYLgJm1v/J7CWg='
    auth_user_5.last_login = None
    auth_user_5.is_superuser = False
    auth_user_5.username = u'naresh'
    auth_user_5.first_name = u''
    auth_user_5.last_name = u''
    auth_user_5.email = u''
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.date_joined = dateutil.parser.parse("2017-07-19T01:53:23.563210+00:00")
    auth_user_5 = importer.save_or_locate(auth_user_5)

    auth_user_6 = User()
    auth_user_6.password = u'pbkdf2_sha256$20000$mjfxeOfEMpeb$sbCx1Of2+HkX6k5LBB3aHyv3BfFkI/OhUQR2pLKFQWs='
    auth_user_6.last_login = None
    auth_user_6.is_superuser = False
    auth_user_6.username = u'sivaram'
    auth_user_6.first_name = u''
    auth_user_6.last_name = u''
    auth_user_6.email = u''
    auth_user_6.is_staff = False
    auth_user_6.is_active = True
    auth_user_6.date_joined = dateutil.parser.parse("2017-07-19T02:02:19+00:00")
    auth_user_6 = importer.save_or_locate(auth_user_6)

    auth_user_7 = User()
    auth_user_7.password = u'pbkdf2_sha256$20000$Gggh2BsdVNf4$R/FLei9D3H7kdLeysBO5HQ/6CwXv7d/zyg86j+6HPIY='
    auth_user_7.last_login = None
    auth_user_7.is_superuser = True
    auth_user_7.username = u'govardhan'
    auth_user_7.first_name = u''
    auth_user_7.last_name = u''
    auth_user_7.email = u''
    auth_user_7.is_staff = False
    auth_user_7.is_active = True
    auth_user_7.date_joined = dateutil.parser.parse("2017-07-25T02:18:16+00:00")
    auth_user_7 = importer.save_or_locate(auth_user_7)

    auth_user_8 = User()
    auth_user_8.password = u'pbkdf2_sha256$20000$Ks2x3Utlvvci$i0VY89tKZmVMynfxk/hFwNVqyTORWoRjFtEnvjTsN8o='
    auth_user_8.last_login = None
    auth_user_8.is_superuser = False
    auth_user_8.username = u'ramanji'
    auth_user_8.first_name = u''
    auth_user_8.last_name = u''
    auth_user_8.email = u''
    auth_user_8.is_staff = False
    auth_user_8.is_active = True
    auth_user_8.date_joined = dateutil.parser.parse("2017-07-28T02:10:34.721453+00:00")
    auth_user_8 = importer.save_or_locate(auth_user_8)

    auth_user_9 = User()
    auth_user_9.password = u'pbkdf2_sha256$20000$kWNufiqcbDsF$ksnpz6m5jPTrsO9+vle6+tlm1GVcXArkYWx9RbNb38A='
    auth_user_9.last_login = dateutil.parser.parse("2017-08-03T02:39:47.269684+00:00")
    auth_user_9.is_superuser = False
    auth_user_9.username = u'kumar'
    auth_user_9.first_name = u''
    auth_user_9.last_name = u''
    auth_user_9.email = u'tuxfux.hlp@gmail.com'
    auth_user_9.is_staff = False
    auth_user_9.is_active = True
    auth_user_9.date_joined = dateutil.parser.parse("2017-08-03T02:30:53.902518+00:00")
    auth_user_9 = importer.save_or_locate(auth_user_9)

