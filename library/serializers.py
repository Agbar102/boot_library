from django.utils.http import escape_leading_slashes
from rest_framework import serializers

from library.models import Author, Book, Image



class AuthorSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    full_name = serializers.CharField()


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['birth_date'] = instance.birth_date if instance.birth_date else ""
        if instance.books.exists():
            book_serializer = BookSerializer(instance.books.all(), many=True)
            representation['books'] = book_serializer.data
        else:
            representation['books'] = []
        return representation


class ImageSerializer(serializers.ModelSerializer):

    class Meta:
        model = Image
        fields = '__all__'

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['image'] = f"http://127.0.0.1:8000{instance.image.url}" \
            if instance.image else None
        return representation


class BookSerializer(serializers.ModelSerializer):
    author = serializers.CharField(source='author.full_name')

    class Meta:
        model = Book
        fields = ('id','title', 'isdn', 'author')


    def to_representation(self, instance):
        representation = super().to_representation(instance)
        if instance.images.exists():
            image_serializer = ImageSerializer(instance.images.all(), many=True)
            representation['images'] = image_serializer.data
        else:
            representation['images'] = []
        return representation

    

