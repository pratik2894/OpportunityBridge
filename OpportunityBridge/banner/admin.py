from django.contrib import admin
from banner.models import Banner
# Register your models here.
class BannerAdmin(admin.ModelAdmin):
    list_display=('title','subtitle', 'bannerimage1','bannerimage2','bannerimage3')

admin.site.register(Banner,BannerAdmin)
