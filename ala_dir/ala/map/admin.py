from django.contrib import admin

from .models import DataSet,Variable, Breakpoint


class BreakpointInline(admin.TabularInline):
    model = Breakpoint
    extra = 5

class VariableAdmin(admin.ModelAdmin):
	inlines = [BreakpointInline,]

class DataSetAdmin(admin.ModelAdmin):
	pass

admin.site.register(DataSet, DataSetAdmin)
admin.site.register(Variable, VariableAdmin)
