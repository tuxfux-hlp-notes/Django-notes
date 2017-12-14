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
# manage.py dumpscript auth.user
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

    # auth_user_1 = User()
    # auth_user_1.password = u'pbkdf2_sha256$20000$cANYMzMmFSxJ$6+IoG9oCPLvvsLNdD2U2rUuRKOQfCTgyEptT0/8H34Q='
    # auth_user_1.last_login = dateutil.parser.parse("2017-12-06T02:56:36.169303+00:00")
    # auth_user_1.is_superuser = True
    # auth_user_1.username = u'admin'
    # auth_user_1.first_name = u''
    # auth_user_1.last_name = u''
    # auth_user_1.email = u'admin@gmail.com'
    # auth_user_1.is_staff = True
    # auth_user_1.is_active = True
    # auth_user_1.date_joined = dateutil.parser.parse("2017-10-27T01:51:33.041366+00:00")
    # auth_user_1 = importer.save_or_locate(auth_user_1)

    auth_user_2 = User()
    auth_user_2.password = u'pbkdf2_sha256$20000$mEaPBTGSpT18$9SpRun8ulgQEmiU18Cuw0kG3ZQMMVH1dwdhXR9Ozo/8='
    auth_user_2.last_login = dateutil.parser.parse("2017-12-08T02:21:33.636683+00:00")
    auth_user_2.is_superuser = False
    auth_user_2.username = u'rama'
    auth_user_2.first_name = u'Rama'
    auth_user_2.last_name = u'Krishna'
    auth_user_2.email = u''
    auth_user_2.is_staff = True
    auth_user_2.is_active = True
    auth_user_2.date_joined = dateutil.parser.parse("2017-11-17T02:06:24+00:00")
    auth_user_2 = importer.save_or_locate(auth_user_2)

    auth_user_3 = User()
    auth_user_3.password = u'pbkdf2_sha256$20000$feEiyBWcZ85p$w06/3Wb6o6sVTr/xY1q/hUCZ1qWO7mImb0pBljtzP40='
    auth_user_3.last_login = None
    auth_user_3.is_superuser = False
    auth_user_3.username = u'kumar'
    auth_user_3.first_name = u''
    auth_user_3.last_name = u''
    auth_user_3.email = u''
    auth_user_3.is_staff = True
    auth_user_3.is_active = True
    auth_user_3.date_joined = dateutil.parser.parse("2017-11-30T02:52:58+00:00")
    auth_user_3 = importer.save_or_locate(auth_user_3)

    auth_user_4 = User()
    auth_user_4.password = u'pbkdf2_sha256$20000$p9n5T7rvNexH$18ZZKTNFwl+CgbZfhXAwogOTucQTcsi4VR8S2MzOEd0='
    auth_user_4.last_login = None
    auth_user_4.is_superuser = False
    auth_user_4.username = u'keethu'
    auth_user_4.first_name = u''
    auth_user_4.last_name = u''
    auth_user_4.email = u''
    auth_user_4.is_staff = False
    auth_user_4.is_active = True
    auth_user_4.date_joined = dateutil.parser.parse("2017-12-02T01:54:45+00:00")
    auth_user_4 = importer.save_or_locate(auth_user_4)

    auth_user_5 = User()
    auth_user_5.password = u'pbkdf2_sha256$20000$5uDdPIEOBVsl$GOY2eD7cbNg8T+uipS2CkaHOP6arhEsM/rvm0uDuPL8='
    auth_user_5.last_login = None
    auth_user_5.is_superuser = False
    auth_user_5.username = u'ramya'
    auth_user_5.first_name = u''
    auth_user_5.last_name = u''
    auth_user_5.email = u'ramya@khyaathi.com'
    auth_user_5.is_staff = False
    auth_user_5.is_active = True
    auth_user_5.date_joined = dateutil.parser.parse("2017-12-06T02:53:56.859419+00:00")
    auth_user_5 = importer.save_or_locate(auth_user_5)

    auth_user_6 = User()
    auth_user_6.password = u'pbkdf2_sha256$20000$DmDiPoW6VwiN$SrZPOoDGZwRbtWmrrNmmgiLLYba9+T5NuOXKxeBpn34='
    auth_user_6.last_login = None
    auth_user_6.is_superuser = False
    auth_user_6.username = u'chatarji'
    auth_user_6.first_name = u''
    auth_user_6.last_name = u''
    auth_user_6.email = u'tuxfux.hlp@gmail.com'
    auth_user_6.is_staff = False
    auth_user_6.is_active = True
    auth_user_6.date_joined = dateutil.parser.parse("2017-12-06T02:55:22.285801+00:00")
    auth_user_6 = importer.save_or_locate(auth_user_6)

    # Re-processing model: django.contrib.auth.models.User







