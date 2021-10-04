from django.db.models import Count
from rest_framework.views import  APIView
from rest_framework import status
from rest_framework.response import Response
from .serializers import CartSerializer
from .models import Cart

class APIPrototype(APIView):
    reverse         = True
    SerializerClass = None
    many     = True
    queryset = ''
    order_by = ''

    def on_query_set(self):
        pass

    def list(self):
        self.on_query_set()
        serializer = self.SerializerClass(self.queryset, many=self.many)
        if len(self.order_by):
            list = sorted(
                serializer.data,
                key=lambda tup: tup[self.order_by],
                reverse=self.reverse)
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
    queryset         = Cart.objects

class CartListUser (APIPrototype):

    SerializerClass  = CartSerializer

    def on_query_set(self):
        ndata=[]
        data = Cart.objects.all()
        for el in data:
            lenght=len(el.dishs.annotate(cart_count=Count('cart_id')))
            if lenght>0:
                ndata.append(el)
        self.queryset=ndata

class CartListUserOrderBy (CartListUser):

    def get(self, request, *args, **kwargs):
        self.order_by=self.kwargs.get("orderby")
        return self.api_get(request)

class CartListUserSearch (CartListUser):

    def on_query_set(self):
        self.queryset = Cart.objects.filter(Cart__name=self.kwargs.get("name"))

