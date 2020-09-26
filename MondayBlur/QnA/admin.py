from django.contrib import admin
from .models import question,category,comment


class CategoryAdmin(admin.ModelAdmin):
    prepopulated_fields = {"slug": ("category",)}


admin.site.register(question)
admin.site.register(category,CategoryAdmin)
admin.site.register(comment)



