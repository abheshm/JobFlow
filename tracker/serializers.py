from rest_framework import serializers
from .models import JobApplication
from django.contrib.auth.models import User

class JobApplicationSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobApplication
        fields = '__all__'


class RegisterSerializer(serializers.ModelSerializer):

    class Meta:

        model = User

        fields = ['username', 'password']

        extra_kwargs = {

            'password': {'write_only': True}
        }

    def create(self, validated_data):

        user = User.objects.create_user(

            username=validated_data['username'],

            password=validated_data['password']
        )

        return user