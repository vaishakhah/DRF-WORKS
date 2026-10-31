#using model serializer
from rest_framework import serializers

from MovieAPP.models import CustomUser
from MovieAPP.models import Movie
from django.contrib.auth.models import User
from django.core.mail import send_mail
class MovieSerializer(serializers.ModelSerializer):
    class Meta:
        model= Movie
        fields = "__all__"
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['username','password','first_name','last_name','email','phone','address']
    # to encrypt password /password hashing we redefine create() in our UserSerializer class
    def create(self, validated_data):
        # for creating a user account uses create_user
        u = CustomUser.objects.create_user(**validated_data) # to encrypt password
        # /password hashing
        # for creating a superuser
        # user.objects.create_superuser(**validated_data)
        u.save()
        send_mail(
            subject = "Welcome to our app",
            message = "Thank you for signing up for App",
            from_email= "vaishakhah1@gmail.com",
            recipient_list= [u.email,],
            fail_silently= True)
        return u



