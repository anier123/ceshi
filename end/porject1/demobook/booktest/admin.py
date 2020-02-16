from django.contrib import admin
from django.contrib.admin import ModelAdmin
# Register your models here.

from .models import Book, Hero, User, Account, Concact


class AdminInlines(admin.StackedInline):
    model = Hero
    extra = 1


class BookAdmin(ModelAdmin):
    list_display = ('title', 'price', 'pub_date')
    search_fields = ('title', 'price')
    list_filter = ('title', 'price')
    inlines = [AdminInlines]


admin.site.register(Book, BookAdmin)


class HeroAdmin(ModelAdmin):
    list_filter = ('name', 'gender', 'conten', 'book')
    search_fields = ('name', 'book')


admin.site.register(Hero, HeroAdmin)
admin.site.register(User)
admin.site.register(Account)
admin.site.register(Concact)
