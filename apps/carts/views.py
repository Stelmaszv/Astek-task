from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CartSerializer
from .models import Cart

class APIPrototype(APIView):

    SerializerClass = None
    many     = True
    queryset = ''
    order_by = ''

    def list(self):
        serializer = self.SerializerClass(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(
                serializer.data,
                key=lambda tup: tup[self.order_by],
                reverse=True)
        else:
            list= serializer.data
        return list

    def post(self, request, *args, **kwargs):
        serializer = self.SerializerClass(data=request.data, many=False)
        if serializer.is_valid():
            serializer.save()
            return Response(data=self.list(), status=status.HTTP_201_CREATED)
        return self.api_get(request)

    def api_get(self, request, *args, **kwargs):
        return Response(data=self.list(), status=status.HTTP_200_OK)

    def get(self, request, *args, **kwargs):
        return self.api_get(request)

class CartList (APIPrototype):

    SerializerClass  = CartSerializer
    queryset          = Cart.objects
    order_by          = 'avg_rating'