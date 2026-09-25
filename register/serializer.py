from rest_framework import serializers
from .models import Register

class RegisterSerializer(serializers.ModelSerializer):

    class Meta:
        model = Register
        fields = ['firstName', 'lastName', 'mobile', 'email']

    def validate_firstName(self, value):
        if len(value) < 3:
            raise serializers.ValidationError(
                "First name must be at least 3 characters"
            )
        return value

    def validate_mobile(self, value):
        if not value.isdigit():
            raise serializers.ValidationError(
                "Mobile number should contain only numbers"
            )

        if len(value) != 10:
            raise serializers.ValidationError(
                "Mobile number must be 10 digits"
            )

        return value