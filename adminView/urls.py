from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='admin/login.html'), name='adminlogin'),
    path('admin_dashboard/', views.admin_dashboard, name='admin_dashboard'),
    path('bloodbank_index/', views.bloodbank_index, name='bloodbank_index'),
    path('donation/requests/', views.admin_view_donation_requests, name='admin_view_donation_requests'),
    path('receiver-request/list/', views.admin_receiver_request_list, name='admin_receiver_request_list'),
    path('donation-request/edit/<int:request_id>/',views.admin_edit_donation_request, name='admin_edit_donation_request'),
    path('receiver-request/edit/<int:request_id>/',views.admin_edit_receiver_request, name='admin_edit_receiver_request'),
    path('admin-blood', views.admin_blood_view,name='admin-blood'),
    path('about/', views.about, name='admin_about'),

]
