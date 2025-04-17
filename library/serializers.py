from rest_framework import serializers

from library.models import Author


# class AuthorSerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Author
#         fields = "__all__"

class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()
    # birth_date = serializers.DateField(format="%Y-%m-%d")


    # def validate_birth_date(self, value):
    #     print(value)
    #     return value

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['birth_date'] = instance.birth_date if instance.birth_date else ""
        return representation

