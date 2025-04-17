from rest_framework import status, generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_200_OK

from library.models import Author
from library.serializers import AuthorSerializer

class AuthorAPiView(generics.ListAPIView):
    queryset = Author.objects.all()
    serializer_class = AuthorSerializer

@api_view(http_method_names=['GET'])
def get_all_authors(request):
    search_name = request.query_params.get("search_name")
    birth_date = request.query_params.get("birth_date")
    queryset = Author.objects.all()
    if search_name and not birth_date:
        queryset = Author.objects.filter(full_name__icontains=search_name)
    elif birth_date and not search_name:
        queryset = Author.objects.filter(birth_date=birth_date)
    elif search_name and birth_date:
        queryset = Author.objects.filter(full_name__icontains=search_name, birth_date=birth_date)
    serializer = AuthorSerializer(queryset, many=True)
    return Response(serializer.data, status=HTTP_200_OK)

@api_view(http_method_names=['GET'])
def get_author(request, pk):
    obj = Author.objects.get(id=pk)
    serializer = AuthorSerializer(obj)
    return Response(serializer.data)

#детализация