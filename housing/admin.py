from django.contrib import admin

# Register your models here.
from .models import Comunidad, RepresentanteFamilia, ProgresoVivienda

admin.site.register(Comunidad)
admin.site.register(RepresentanteFamilia)
admin.site.register(ProgresoVivienda)