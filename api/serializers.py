from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from rest_framework.validators import UniqueValidator
from django.contrib.auth.models import User


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True, validators=[UniqueValidator(queryset=User.objects.all())])
    password = serializers.CharField(write_only=True, required=True, validators = [validate_password])

    class Meta:
        model = User
        fields = ['id', 'username', 'email','password', 'first_name', 'last_name']
        extra_kwargs = {
            'username': {'required': True},
        }

    def create(self, validated_data):
        user = User.objects.create(
            username = validated_data['username'],
            email = validated_data['email'],           
        )
        user.set_password(validated_data['password'])
        user.save()
        return user
        



# .data - Returns the outgoing primitive representation.
# .is_valid() - Deserializes and validates incoming data.
# .validated_data - Returns the validated incoming data.
# .errors - Returns any errors during validation.
# .save() - Persists the validated data into an object instance.