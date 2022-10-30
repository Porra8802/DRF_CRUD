from django.contrib import admin

from orgmatrixnumbers.models import OrgMatrixNumbers


# @admin.register(OrgMatrixNumbers)
# class OrgMatrixNumbersAdmin(admin.ModelAdmin):
#     list_display=('field1', 'field2', 'field3')
admin.site.register(OrgMatrixNumbers)
