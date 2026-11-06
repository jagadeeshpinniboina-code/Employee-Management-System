from django.contrib import admin
from Employee_Management_App.models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'email','mobile','department','destination','salary','city','status')
    list_filter = ('status',)
    search_fields = ('department',)


