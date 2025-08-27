from django.contrib import admin
from .models import Post
# Register your models here.

class PostAdmin(admin.ModelAdmin):
    pass

#regsitering the new model
admin.site.register(Post,PostAdmin)
   