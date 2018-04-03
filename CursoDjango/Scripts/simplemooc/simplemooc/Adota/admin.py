from django.contrib import admin

from .models import (Animal, AnimalManager)


class AnimalAdmin(admin.ModelAdmin):

    list_display = ['name','created_at','tipo','idade','porte', 'get_img', 'status' ]
    list_filter = ['tipo','idade','porte','status' ]
    search_fields = ['name','tipo','porte']
    ##prepopulated_fields = {'slug': ('name',)}

    def get_img(self, Animal):
        if Animal.image:
            return u'<img width="50px" height="50px" src="/media/%s" />' %Animal.image
        else:
            return u'Sem imagem'
    get_img.short_description = 'Imagem'
    get_img.allow_tags = True





admin.site.register(Animal, AnimalAdmin)
