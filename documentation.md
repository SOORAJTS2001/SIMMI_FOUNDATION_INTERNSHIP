# Django REST API

This is a Django REST API for handling user registration and authentication. The API uses the `django.contrib.auth.models.User` model to represent users and the `django-rest-framework` library to handle the API endpoints and serialization. The `knox` package is used for handling authentication and token management.

## Serializers

### `RegisterSerializer`

This serializer is used for creating new user accounts. It is a subclass of `serializers.ModelSerializer` that is used for creating new user accounts. The `User` model from `django.contrib.auth.models` is used as the base model for the serializer. The serializer defines two fields for the user password, `password` and `password2`, both of which are write-only and have a minimum length of 2 characters.

The `Meta` class of the serializer specifies that the `username`, `password`, `password2`, `first_name`, and `last_name` fields should be used for the serializer. The `first_name` and `last_name` fields are required and have the `required` attribute set to `True`.

The `validate` method of the serializer checks if the `password` and `password2` fields match, and raises a `serializers.ValidationError` if they do not.

The `create` method of the serializer is responsible for creating a new user account, using the `username`, `first_name`, and `last_name` fields from the serializer. The `set_password` method is used to set the user's password, and the `save` method is used to save the new user account to the database. The newly created user is then returned by the method.

## URLs

The `urls.py` file contains the URLs for the Django REST API. The `urlpatterns` list is used to define the different endpoints of the API. 

- The `path('user/', views.get_user)` endpoint is used to retrieve the currently authenticated user's information.
- The `path('login/', views.login)` endpoint is used for handling user login requests.
- The `path('register/', views.register)` endpoint is used for handling user registration requests.
- The `path('logout/', knox_views.LogoutView.as_view(), name='knox_logout')` endpoint is used for handling user logout requests. This logout request only logout the current session
- The `path('logoutall/', knox_views.LogoutAllView.as_view(), name='knox_logoutall')` endpoint is used for handling user logout requests. This logout request logout the user from all the active sessions.

## Views

The `views.py` file contains views for the Django REST API. Each view is decorated with the `@api_view` decorator, which specifies the HTTP methods that the view will handle. 

- The `login` view is used to handle user login requests. It uses the `AuthTokenSerializer` to validate the incoming request data and create an authentication token for the user. The user's data is then serialized using the `serialize_user` function and returned as a response along with the token.
- The `register` view is used to handle user registration requests. It uses the `RegisterSerializer`
