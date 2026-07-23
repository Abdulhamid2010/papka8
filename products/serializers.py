from django.contrib.auth import get_user_model
from rest_framework import serializers

User = get_user_model()


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    class Meta:
        model = User
        fields = ["id", "phone_number", "currency", "language", "password"]
        read_only_fields = ["id"]

    def create(self, validated_data):
        user = User.objects.create_user(
            phone_number=validated_data["phone_number"],
            password=validated_data["password"],
            currency=validated_data.get("currency", "USD"),
            language=validated_data.get("language", "uz"),
        )
        return user