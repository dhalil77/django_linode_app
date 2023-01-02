from django.urls import path
from . import views



urlpatterns = [
    
    path('', views.signin, name='signin'),
    path('election', views.election, name='election'),
    path('rencotre', views.rencontre, name='rencontre'),

    path('adhesion_aff', views.adhesion_aff, name='adhesion_aff'),
    path('adhesion_codefo', views.adhesion_codefo, name='adhesion_codefo'),

    path('vote', views.vote, name='vote'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('all_users', views.all_users, name='all_users'),
    path('signup', views.signup, name='signup'),

]