from django.urls import path
from django.contrib.auth import views as auth_views

from . import views
from .forms import LoginForm, UserSettingsForm

app_name = 'vendor'

urlpatterns = [
    path('', views.index, name='index'),
    #path('contact/', views.contact, name='contact'),
    path('signup/', views.signup, name='signup'),
    path('logout/', views.logout, name='logout'),
    path('login/', auth_views.LoginView.as_view(template_name='vendor/login.html',authentication_form=LoginForm), name='login'),
    path('reviewNew/<int:stores_pk>/', views.review_new, name='reviewNew'),
    path('reviewInbox/', views.reviewInbox, name='reviewInbox'),
    path('userSettingsPage/', views.userSettingsPage, name='userSettingsPage'),
    path('reviewInbox/<int:pk>/', views.reviewDetail, name='reviewDetail'),
]