from django.contrib import admin
from .models import Post
from .models import Publication,Article
from .models import Restaurant,Waiter,Place

# Register your models here.

admin.site.register(Post)
# admin.site.register(Publication)
# admin.site.register(Article)
admin.site.register(Restaurant)
admin.site.register(Waiter)
admin.site.register(Place)
