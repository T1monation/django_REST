from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, ArticleModelSerializer, BiographyModelSerializer, BookModelSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    # def get_queryset(self):
    #     # param = self.request.query_params.get('name')
    #     # print(self.request.query_params)
    #     param = self.request.headers.get('filter')
    #     print(self.headers)
    #     if param:
    #         return Author.objects.filter(first_name__contains=param[0])
    #     else:
    #         return super().get_queryset()

    filterset_fields = ['first_name', 'last_name', 'birthday_year']
    pagination_class = AuthorPaginator


class BookModelViewSet(ModelViewSet):
    queryset = Book.objects.all()
    serializer_class = BookModelSerializer


class ArticleModelViewSet(ModelViewSet):
    queryset = Article.objects.all()
    serializer_class = ArticleModelSerializer


class BiographyModelViewSet(ModelViewSet):
    queryset = Biography.objects.all()
    serializer_class = BiographyModelSerializer


# class MyAPIView(APIView):

#     def get(self, request):
#         return Response({'data': 'GET SUCCSESS'})

#     def post(self, request):
#         return Response({'dats': 'POST SUCCSESS'})

class MyAPIView(ViewSet):
    def list(self, request):
        authors = Author.objects.all()
        serializer = AuthorModelSerializer(authors, many=True)
        return Response(serializer.data)

    @action(detail=False, methods=['get'])
    def babayka(self, request):
        return Response({'data': 'RATATA'})
