from django.contrib import admin
from cms.models import ACL

# Register your models here.

class ACLAdmin(admin.ModelAdmin):
    list_display = ('vlan','protocol','src_ip','src_wc','src_port','dst_ip','dst_wc','dst_port')
    list_display_links = ('vlan','protocol','src_ip','src_wc','src_port','dst_ip','dst_wc','dst_port')

admin.site.register(ACL,ACLAdmin)
