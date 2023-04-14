from django.contrib import admin
from .models import Person, Discipline, Work, Team, Institute, News, EdSource

# Register your models here.

admin.site.register(Person)
admin.site.register(Discipline)
admin.site.register(Work)
admin.site.register(Team)
admin.site.register(Institute)
admin.site.register(News)
admin.site.register(EdSource)