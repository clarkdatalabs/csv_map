from django.contrib import admin

from .models import DataSet, QuantitativeVariable, Breakpoint, QualitativeVariable, Category

class CSVMapAdmin(admin.AdminSite):
	site_header = "ALA Maps"
	site_url = "/map/"

class BreakpointInline(admin.TabularInline):
    model = Breakpoint
    extra = 5

class CategoryInline(admin.TabularInline):
 	model = Category
 	extra = 5

class Quant_Admin(admin.ModelAdmin):
	inlines = [BreakpointInline,]

class Qual_Admin(admin.ModelAdmin):
	inlines = [CategoryInline,]

class DataSetAdmin(admin.ModelAdmin):
	pass

admin_site = CSVMapAdmin(name='csv_admin')

admin_site.register(DataSet, DataSetAdmin)
admin_site.register(QuantitativeVariable, Quant_Admin)
admin_site.register(QualitativeVariable, Qual_Admin)

