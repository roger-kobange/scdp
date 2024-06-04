from django.urls import path
from . import views
from .views import CreateMachineView


urlpatterns = [
    path('', views.accueil, name='accueil'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('login/',views.login_views, name='login'),
    path('accounts/login/', views.login_user, name='accounts/login/'),
    path('logout/', views.logout_user, name='logout'),
    path('register/', views.register_user, name='register'),

    path('users/',views.user_list , name='user-list'),
    path('machines/', views.machine_list, name='machine-list'),
    path('create_machine', views.create_machine, name='create_machine'), 
    path('edit_machine/<int:id>/', views.edit_machine, name='edit_machine'),
    path('update_machine/<int:id>/', views.update_machine, name='update_machine'),
    path('delete_machine/<int:id>/', views.delete_machine, name='delete_machine'),# Ajoutez cette ligne

    path('techniciens/', views.technicien_list, name='technicien-list'),
    
]
