from django.contrib import admin

from .models import Producto,Categoria

admin.site.register(Categoria)
#admin.site.register(Producto)

@admin.register(Producto)
class ProductoAdmin(admin.ModelAdmin):
    list_display = ('nombre','precio','categoria','fecha_registro')
    list_editable =('precio',)