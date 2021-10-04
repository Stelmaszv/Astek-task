from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.response import Response

class APIPrototypeGet(APIView):

    SerializerClass=None
    queryset=None

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        serializer = self.SerializerClass(self.queryset)
        return Response(data=serializer.data, status=status.HTTP_200_OK)