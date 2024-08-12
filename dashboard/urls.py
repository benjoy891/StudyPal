from django.urls import path
from dashboard import views

urlpatterns = [
    path('user_dashboard/', views.user_dashboard, name="user_dashboard"),
    path('user_contact/', views.user_contact, name="user_contact"),
    path('user_profile/', views.user_profile, name="user_profile"),
    path('change_password/', views.change_password, name="change_password"),
    path('pdf_data/', views.pdf_data, name='pdf_data'),
]
