from rest_framework.serializers import HyperlinkedModelSerializer, ModelSerializer
from .models import Author, Book, Biography, Article


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"
        # fields = ['first_name']
        # exclude = ['first_name']


class BiographyModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Biography
        fields = "__all__"


class ArticleModelSerializer(HyperlinkedModelSerializer):
    author = AuthorModelSerializer()

    class Meta:
        model = Article
        fields = "__all__"


class BookModelSerializer(ModelSerializer):

    class Meta:
        model = Book
        fields = "__all__"
