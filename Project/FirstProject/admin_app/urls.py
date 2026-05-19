from django.urls import path
from . import views

app_name = 'admin_app'

urlpatterns = [
    path('', views.admin_dashboard_view, name='dashboard'),
    path('login/', views.admin_login_view, name='login'),
    path('block/<int:user_id>/', views.block_user_view, name='block'),
    path('unblock/<int:user_id>/', views.unblock_user_view, name='unblock'),
    path('edit/<int:user_id>/', views.edit_user_view, name='edit'),
    path('notes/approve/<int:note_id>/', views.approve_note_view, name='approve_note'),
    path('notes/reject/<int:note_id>/', views.reject_note_view, name='reject_note'),
    path('messages/read/<int:msg_id>/', views.read_message_view, name='read_message'),
    path('messages/delete/<int:msg_id>/', views.delete_message_view, name='delete_message'),
]
