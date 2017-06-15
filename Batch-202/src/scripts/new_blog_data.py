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
# ./manage.py dumpscript blog
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
from  django.utils import timezone 
#django.utils.timezone.get_default_timezone()


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
    blog_post_1.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$oJcDd9UmNsJC$N1TM50Pb4acF8hkGfHi9toc1kdcfHqE1qG55+zBJYVQ=', 'email': u'', 'date_joined': datetime.datetime(2017, 5, 30, 1, 23, 8, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_1.email = u'tuxfux.hlp@gmail.com'
    blog_post_1.title = u'My first post'
    blog_post_1.text = u'Today we are learning about the django static files. we learned lot of good information which was relative to how to display the static files like css and java script. we learned about STATICFILES_DIR and we also learned about the STATIC_ROOT.'
    blog_post_1.created_date = dateutil.parser.parse("2017-06-02T05:02:35+00:00")
    blog_post_1.published_date = dateutil.parser.parse("2017-06-03T05:03:20+00:00")
    blog_post_1 = importer.save_or_locate(blog_post_1)

    blog_post_2 = Post()
    blog_post_2.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$oJcDd9UmNsJC$N1TM50Pb4acF8hkGfHi9toc1kdcfHqE1qG55+zBJYVQ=', 'email': u'', 'date_joined': datetime.datetime(2017, 5, 30, 1, 23, 8, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_2.email = u'tuxfux.hlp@gmail.com'
    blog_post_2.title = u' My second post'
    blog_post_2.text = u'we have already learned about templates. We are tyring to integrate the ORM backend data into our html pages.\r\nLets hope we will get the data from the backend database into our html pages.'
    blog_post_2.created_date = dateutil.parser.parse("2017-06-03T05:03:25+00:00")
    blog_post_2.published_date = dateutil.parser.parse("2017-06-03T05:03:53+00:00")
    blog_post_2 = importer.save_or_locate(blog_post_2)

    blog_post_3 = Post()
    blog_post_3.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$oJcDd9UmNsJC$N1TM50Pb4acF8hkGfHi9toc1kdcfHqE1qG55+zBJYVQ=', 'email': u'', 'date_joined': datetime.datetime(2017, 5, 30, 1, 23, 8, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_3.email = u'tuxfux.hlp@gmail.com'
    blog_post_3.title = u'third title'
    blog_post_3.text = u'This is the content for the django ORM shell'
    blog_post_3.created_date = dateutil.parser.parse("2017-06-03T05:19:44+00:00")
    blog_post_3.published_date = None
    blog_post_3 = importer.save_or_locate(blog_post_3)

    blog_post_4 = Post()
    blog_post_4.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$oJcDd9UmNsJC$N1TM50Pb4acF8hkGfHi9toc1kdcfHqE1qG55+zBJYVQ=', 'email': u'', 'date_joined': datetime.datetime(2017, 5, 30, 1, 23, 8, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_4.email = u'tuxfux.hlp@gmail.com'
    blog_post_4.title = u'Fourth Post'
    blog_post_4.text = u'This is my fourth post'
    blog_post_4.created_date = dateutil.parser.parse("2017-06-04T05:07:20+00:00")
    blog_post_4.published_date = None
    blog_post_4 = importer.save_or_locate(blog_post_4)

    blog_post_5 = Post()
    blog_post_5.author =  importer.locate_object(User, "id", User, "id", 1, {'username': u'admin', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2017, 6, 3, 5, 2, 3, 723738, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$6SaVs1IyS9s5$s9h6o/ZZjpU1QYLICsYAChz22YN/2q+DR6lTpbkbCzU=', 'email': u'admin@gmail.com', 'date_joined': datetime.datetime(2017, 5, 30, 0, 50, 23, 376400, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_5.email = u'admin@gmail.com'
    blog_post_5.title = u'Fifth Post'
    blog_post_5.text = u'I am good with the content writing. I am tying to test my django pages.'
    blog_post_5.created_date = dateutil.parser.parse("2017-06-04T05:29:33+00:00")
    blog_post_5.published_date = dateutil.parser.parse("2017-06-04T05:29:55+00:00")
    blog_post_5 = importer.save_or_locate(blog_post_5)

    blog_post_6 = Post()
    blog_post_6.author =  importer.locate_object(User, "id", User, "id", 2, {'username': u'kumar', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 2, 'is_superuser': False, 'is_staff': True, 'last_login': None, 'password': u'pbkdf2_sha256$20000$oJcDd9UmNsJC$N1TM50Pb4acF8hkGfHi9toc1kdcfHqE1qG55+zBJYVQ=', 'email': u'', 'date_joined': datetime.datetime(2017, 5, 30, 1, 23, 8, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_6.email = u'kiran@gmail.com'
    blog_post_6.title = u'hello there'
    blog_post_6.text = u'hello there how are you doing.'
    blog_post_6.created_date = dateutil.parser.parse("2017-06-10T05:34:12+00:00")
    blog_post_6.published_date = None
    blog_post_6 = importer.save_or_locate(blog_post_6)

    blog_post_7 = Post()
    blog_post_7.author =  importer.locate_object(User, "id", User, "id", 1, {'username': u'admin', 'first_name': u'', 'last_name': u'', 'is_active': True, 'id': 1, 'is_superuser': True, 'is_staff': True, 'last_login': datetime.datetime(2017, 6, 3, 5, 2, 3, 723738, tzinfo=timezone.get_default_timezone()), 'password': u'pbkdf2_sha256$20000$6SaVs1IyS9s5$s9h6o/ZZjpU1QYLICsYAChz22YN/2q+DR6lTpbkbCzU=', 'email': u'admin@gmail.com', 'date_joined': datetime.datetime(2017, 5, 30, 0, 50, 23, 376400, tzinfo=timezone.get_default_timezone())} ) 
    blog_post_7.email = u'keerthan@edu.com'
    blog_post_7.title = u'First blog of keethan'
    blog_post_7.text = u'Hey i am keerthan.'
    blog_post_7.created_date = dateutil.parser.parse("2017-06-11T05:30:26+00:00")
    blog_post_7.published_date = None
    blog_post_7 = importer.save_or_locate(blog_post_7)

    # Processing model: blog.models.Publication

    from blog.models import Publication

    blog_publication_1 = Publication()
    blog_publication_1.title = u'ABC Publication'
    blog_publication_1 = importer.save_or_locate(blog_publication_1)

    blog_publication_2 = Publication()
    blog_publication_2.title = u'BCD Publication'
    blog_publication_2 = importer.save_or_locate(blog_publication_2)

    blog_publication_3 = Publication()
    blog_publication_3.title = u'CDE publication'
    blog_publication_3 = importer.save_or_locate(blog_publication_3)

    # Processing model: blog.models.Article

    from blog.models import Article

    blog_article_1 = Article()
    blog_article_1.headline = u'Bahubali'
    blog_article_1 = importer.save_or_locate(blog_article_1)

    blog_article_1.publications.add(blog_publication_1)
    blog_article_1.publications.add(blog_publication_2)
    blog_article_1.publications.add(blog_publication_3)

    blog_article_2 = Article()
    blog_article_2.headline = u'Sultan'
    blog_article_2 = importer.save_or_locate(blog_article_2)

    blog_article_2.publications.add(blog_publication_1)

    blog_article_3 = Article()
    blog_article_3.headline = u'Tubelight'
    blog_article_3 = importer.save_or_locate(blog_article_3)

    blog_article_3.publications.add(blog_publication_1)
    blog_article_3.publications.add(blog_publication_2)

    # Processing model: blog.models.Place

    from blog.models import Place

    blog_place_1 = Place()
    blog_place_1.name = u'Raghavendra'
    blog_place_1.address = u'Ameerpet'
    blog_place_1 = importer.save_or_locate(blog_place_1)

    blog_place_2 = Place()
    blog_place_2.name = u'Santosh Dhaba'
    blog_place_2.address = u'Paradise'
    blog_place_2 = importer.save_or_locate(blog_place_2)

    blog_place_3 = Place()
    blog_place_3.name = u'chutneys'
    blog_place_3.address = u'kukatpally'
    blog_place_3 = importer.save_or_locate(blog_place_3)

    # Processing model: blog.models.Restaurant

    from blog.models import Restaurant

    blog_restaurant_1 = Restaurant()
    blog_restaurant_1.place = blog_place_1
    blog_restaurant_1.serves_hot_dogs = True
    blog_restaurant_1.serves_pizza = False
    blog_restaurant_1 = importer.save_or_locate(blog_restaurant_1)

    blog_restaurant_2 = Restaurant()
    blog_restaurant_2.place = blog_place_2
    blog_restaurant_2.serves_hot_dogs = True
    blog_restaurant_2.serves_pizza = True
    blog_restaurant_2 = importer.save_or_locate(blog_restaurant_2)

    blog_restaurant_3 = Restaurant()
    blog_restaurant_3.place = blog_place_3
    blog_restaurant_3.serves_hot_dogs = False
    blog_restaurant_3.serves_pizza = True
    blog_restaurant_3 = importer.save_or_locate(blog_restaurant_3)

    # Processing model: blog.models.Waiter

    from blog.models import Waiter

    blog_waiter_1 = Waiter()
    blog_waiter_1.restaurant = blog_restaurant_2
    blog_waiter_1.name = u'kumar'
    blog_waiter_1 = importer.save_or_locate(blog_waiter_1)

    blog_waiter_2 = Waiter()
    blog_waiter_2.restaurant = blog_restaurant_2
    blog_waiter_2.name = u'santosh'
    blog_waiter_2 = importer.save_or_locate(blog_waiter_2)

    blog_waiter_3 = Waiter()
    blog_waiter_3.restaurant = blog_restaurant_3
    blog_waiter_3.name = u'santosh'
    blog_waiter_3 = importer.save_or_locate(blog_waiter_3)

