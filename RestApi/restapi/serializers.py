'''
The RegisterSerializer is a subclass of serializers.ModelSerializer that is used for creating new user accounts. The User model from django.contrib.auth.models is used as the base model for the serializer. The serializer defines two fields for the user password, password and password2, both of which are write-only and have a minimum length of 2 characters.
The Meta class of the serializer specifies that the username, password, password2, first_name, and last_name fields should be used for the serializer. The first_name and last_name fields are required and have the required attribute set to True.
The validate method of the serializer checks if the password and password2 fields match, and raises a serializers.ValidationError if they do not.
The create method of the serializer is responsible for creating a new user account, using the username, first_name, and last_name fields from the serializer. The set_password method is used to set the user's password, and the save method is used to save the new user account to the database. The newly created user is then returned by the method.
'''
from django.contrib.auth.models import User
from rest_framework import serializers, validators
MIN_LENGTH = 2


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        })
    password2 = serializers.CharField(
        write_only=True,
        min_length=MIN_LENGTH,
        error_messages={
            "min_length": f"Password must be longer than {MIN_LENGTH} characters."
        }
    )

    class Meta:
        model = User
        fields = ("username", "password", "password2",
                  "first_name", "last_name")
        extra_kwargs = {
            "first_name": {"required": True},
            "last_name": {"required": True}
        }

    def validate(self, data):
        if data["password"] != data["password2"]:
            raise serializers.ValidationError("Password does not match.")
        return data

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["username"],
            first_name=validated_data["first_name"],
            last_name=validated_data["last_name"]
        )
        user.set_password(validated_data["password"])
        user.save()
        return user
