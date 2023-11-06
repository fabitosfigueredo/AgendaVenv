from django.contrib import admin
from AgendaApp.models import Contato, Cidade, Telefone, Interesse


# Register your models here.
#classe para exibir telefones no cadastro de contato:
class Telefones(admin.TabularInline):
    model = Telefone
    extra = 1

class ContatoAdmin(admin.ModelAdmin):
    list_display = ['id', 'nome', 'apelido', 'data_nascimento']
    list_filter = ['data_nascimento', 'cidade' ,'estado']
    list_display_links = ['nome']
    search_fields = ['nome', 'apelido']
    inlines = [Telefones]
    filter_horizontal = ['interesses']

admin.site.register(Contato, ContatoAdmin)
admin.site.register(Cidade)
admin.site.register(Telefone)
admin.site.register(Interesse)