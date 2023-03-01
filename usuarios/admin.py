from django.contrib import admin
from .views import Usuario


@admin.register(Usuario)
class UsuarioAdmin(admin.ModelAdmin):
    readonly_fields = ('nome', 'email', 'senha')
