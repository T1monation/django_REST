from rest_framework.viewsets import ModelViewSet
from .models import Author, Book, Article, Biography
from .serializers import AuthorModelSerializer, AuthorModelSerializer2, ArticleModelSerializer, BiographyModelSerializer, BookModelSerializer
from rest_framework.serializers import Serializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.generics import CreateAPIView
from rest_framework.generics import ListAPIView
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ViewSet
from rest_framework.decorators import action
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.permissions import AllowAny, IsAuthenticated
from rest_framework import generics


class AuthorPaginator(LimitOffsetPagination):
    default_limit = 10


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer
    # permission_classes = [IsAuthenticated]
    # def get_queryset(self):
    #     # param = self.request.query_params.get('name')
    #     # print(self.request.query_params)
    #     param = self.request.headers.get('filter')
    #     print(self.headers)
    #     if param:
    #         return Author.objects.filter(first_name__contains=param[0])
    #     else:
    #         return super().get_queryset()

    # filterset_fields = ['first_name', 'last_name', 'birthday_year']
    # pagination_class = AuthorPaginator


class BookModelViewSet(ModelViewSet):
    permission_classes = [AllowAny]
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

class MyAPIView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer = AuthorModelSerializer

    def get_serializer_class(self):
        if self.request.version == '1':
            return AuthorModelSerializer
        return AuthorModelSerializer2


# def authenticate_user(request):
#     try:
#         email = request.data['email']
#         password = request.data['password']
#         user = User.objects.get(email=email, password=password)
#         if user:
#             try:
#                 payload = jwt_payload_handler(user)
#                 token = jwt.encode(payload, settings.SECRET_KEY)
#                 user_details = {}
#                 user_details['name'] = "%s %s" % (
#                     user.first_name, user.last_name)
#                 user_details['token'] = token
#                 user_logged_in.send(sender=user.__class__,
#                                     request=request, user=user)
#                 return Response(user_details, status=status.HTTP_200_OK)
#             except Exception as e:
#                 raise e
#         else:
#             res = {
#                 'error': 'can not authenticate with the given credentials or the account has been deactivated'}
#             return Response(res, status=status.HTTP_403_FORBIDDEN)
#     except KeyError:
#         res = {'error': 'please provide a email and a password'}
#         return Response(res)
