from django.contrib import admin
from .models import kategorija, posetitel_na_aplikacijata, kupuvac, avtor, umetnicko_delo, naracka, kupuvac_kupuva_umetnicko_delo

# Register your models here.

class kategorijaAdmin(admin.ModelAdmin):
    pass
admin.site.register(kategorija, kategorijaAdmin)



class posetitel_na_aplikacijataAdmin(admin.ModelAdmin):
    pass
admin.site.register(posetitel_na_aplikacijata, posetitel_na_aplikacijataAdmin)



class kupuvacAdmin(admin.ModelAdmin):
    pass
admin.site.register(kupuvac, kupuvacAdmin)


class avtorAdmin(admin.ModelAdmin):
    pass
admin.site.register(avtor, avtorAdmin)



class umetnicko_deloAdmin(admin.ModelAdmin):
    pass
admin.site.register(umetnicko_delo, umetnicko_deloAdmin)


class narackaAdmin(admin.ModelAdmin):
    pass
admin.site.register(naracka, narackaAdmin)



class kupuvac_kupuva_umetnicko_deloAdmin(admin.ModelAdmin):
    pass
admin.site.register(kupuvac_kupuva_umetnicko_delo, kupuvac_kupuva_umetnicko_deloAdmin)