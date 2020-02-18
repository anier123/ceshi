from django.contrib import admin
from django.contrib.admin import ModelAdmin
from .models import Vote, Option, User


# Register your models here.


class AdminInlines(admin.StackedInline):
    model = Option
    extra = 1


class VoteAdmin(ModelAdmin):
    inlines = [AdminInlines]


class OptionAdmin(ModelAdmin):
    pass


admin.site.register(Vote, VoteAdmin)
admin.site.register(Option, OptionAdmin)
admin.site.register(User)
