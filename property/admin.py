from django.contrib import admin
from .models import Tombstone, User, Comment


@admin.register(
    User,
    Tombstone,
    Comment,
)
class User(admin.ModelAdmin):
    def queryset(self, request):
        queryset = User.objects.all()
        return queryset


class Tombstone(admin.ModelAdmin):
    def queryset(self, request):
        queryset = Tombstone.objects.all()
        return queryset


class Comment(admin.ModelAdmin):
    def queryset(self, request):
        queryset = Comment.objects.all()
        return queryset