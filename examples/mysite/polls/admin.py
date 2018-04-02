from django.contrib import admin

from .models import Question


# Register your models here.
# Admin takes control of registered models to some extent

admin.site.register(Question)

