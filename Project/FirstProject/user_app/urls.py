from django.urls import path
from . import views

app_name = 'user_app'

urlpatterns = [
    path('', views.dashboard_view, name='dashboard_root'),
    path('dashboard/', views.dashboard_view, name='dashboard'),
    path('register/', views.register_view, name='register'),
    path('verify-otp/', views.verify_otp_view, name='verify_otp'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('notes/submit/', views.submit_note_view, name='submit_note'),
    path('notes/edit/<int:note_id>/', views.update_note_view, name='edit_note'),
    path('forgot-password/', views.forgot_password_view, name='forgot_password'),
    path('reset-password/', views.reset_password_view, name='reset_password'),
    path('about/', views.about_view, name='about'),
    path('contact/', views.contact_view, name='contact'),
]
