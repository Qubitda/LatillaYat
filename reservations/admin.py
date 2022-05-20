from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from reservations.models import Yatch_Reservation,Yatch_Main


admin.site.site_header = 'Yatch App'
admin.site.index_title = 'Yatch App Admin Panel'
admin.site.site_title  = 'Yatch App Admin Panel'


# Register your models here.

class YatchAdmin(admin.TabularInline):
    model = Yatch_Reservation
    extra = 1
    fields = ["id_related" ,"reservation_date","pax","tour_code","customer","nofplace","tour_detail","yatch_name","guide","operation","updated_at","created_at", ]
    exclude = ("updated_at","created_at",)

    def get_readonly_fields(self, request, obj=None):
        if obj:
            return ["updated_at","created_at",]
        else:
            return ["updated_at","created_at",]


class MasterAdmin(ImportExportModelAdmin):
    # list_display = ["id",]
    # list_display_links = ["id",]
    #
    # fieldsets = (None, {'fields': ('"id",',)}),

    inlines = [YatchAdmin]

admin.site.register(Yatch_Main, MasterAdmin)