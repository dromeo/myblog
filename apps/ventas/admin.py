from django.contrib import admin
from myblog.apps.ventas.models import cliente,producto,artista,evento,Album,Tag,Image,AlbumAdmin,TagAdmin,ImageAdmin

admin.site.register(cliente)
admin.site.register(producto)
admin.site.register(artista)
admin.site.register(evento)
admin.site.register(Album, AlbumAdmin)
admin.site.register(Tag, TagAdmin)
admin.site.register(Image, ImageAdmin)
