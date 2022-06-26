from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registration', views.studentRegistration, name='registration'),
    path('receiver', views.receiver, name='receiver'),
    path('addSignatories', views.addSignatories, name='addSignatories'),
    path('application', views.application, name='application'),
    path('home', views.home, name='home'),
    path('admin', views.admin, name='admin'),
    path('update/<int:id>', views.update, name='update'),
    path('editProfile/<int:id>', views.editProfile, name='editProfile'),
    path('logout', views.logoutUser, name= 'logout'),
]
