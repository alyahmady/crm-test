from rest_framework import serializers

from car_app.models import Car


class CarSerializer(serializers.ModelSerializer):
    body_style_name = serializers.CharField(
        source="get_body_style_display", read_only=True
    )

    class Meta:
        model = Car
        fields = [
            "id",
            "name",
            "plate",
            "body_style",
            "body_style_name",
            "created_at",
            "updated_at",
            "is_active",
        ]
        read_only_fields = ["id", "is_active", "created_at", "updated_at"]
        extra_kwargs = {
            "name": {"required": True},
            "body_style": {"write_only": True},
            "plate": {"required": True},
        }
