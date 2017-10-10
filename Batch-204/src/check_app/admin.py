from django.contrib import admin


# Register your models here.

# many to one relationship
# from .models import Reporter,Article
# admin.site.register(Reporter)
# admin.site.register(Article)

from .models import Place,Restaurant,Waiter
admin.site.register(Place)
admin.site.register(Restaurant)
admin.site.register(Waiter)
