'''
This file contains the URLs for the Django REST API. The urlpatterns list is used to define the different endpoints of the API.
The path('user/', views.get_user) endpoint is used to retrieve the currently authenticated user's information.
The path('login/', views.login) endpoint is used for handling user login requests.
The path('register/', views.register) endpoint is used for handling user registration requests.
The path('logout/', knox_views.LogoutView.as_view(), name='knox_logout') endpoint is used for handling user logout requests. This logout request only logout the current session
The path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall') endpoint is used for handling user logout requests. This logout request logout the user from all the active sessions.
The knox package is used for handling authentication and token management. The knox_logout and knox_logoutall views provided by the package are used to handle logout requests for the API.
'''
from django.urls import path
from knox import views as knox_views
from . import views
urlpatterns = [
    path('user/', views.get_user),
    path('login/', views.login),
    path('register/', views.register),
    path('logout/', knox_views.LogoutView.as_view(), name='knox_logout'),
    path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')
]