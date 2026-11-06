from django.urls import path
from Employee_Management_App import views
urlpatterns = [
    path('',views.login_view,name='login'),

    path('logout/',views.logout_view,name='logout'),
    path('list/',views.employee_list_view,name='employee_list_view'),

    path('create/',views.create_employee_view,name='create_employee_view'),

    path('<int:pk>/detail/',views.employee_detail_view,name='employee_detail_view'),

    path('<int:pk>/update/',views.employee_update_view,name='employee_update_view'),

    path('<int:pk>/delete/',views.employee_delete_view,name='employee_delete_view'),

    path('register/',views.register_view,name='register_view'),

    path('about/',views.about_view,name='about_view'),



]