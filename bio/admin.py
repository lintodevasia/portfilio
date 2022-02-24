from django.contrib import admin

from . models import project
from. models import Experience
from . models import skill
from . models import who
from . models import profile

# Register your models here.
admin.site.register(project)
admin.site.register(Experience)
admin.site.register(skill)
admin.site.register(who)
admin.site.register(profile)