from django.http import HttpResponse
from django.shortcuts import render, get_object_or_404
from django.views import generic
from .models import  Productos
from django.views import generic

from .serializer import ShopSerializer
from rest_framework.views import APIView
from rest_framework.parsers import MultiPartParser,FormParser
from rest_framework.response import Response
from rest_framework import status
# Create your views here.

productos =[
    {
        'sku': '65789452',
        'name': 'blusa blueline',
        'price': '250',
        'stock': '16',
    },
    {
        'sku': '16875421',
        'name': 'zapatos cocodrile',
        'price': '380',
        'stock': '5',
    },
    {
        'sku': '47865335',
        'name': 'bufanda skarlet',
        'price': '165',
        'stock': '25',
    },
]

#class IndexView(generic.TemplateView):
class IndexView(generic.ListView):
    template_name= "shop/index.html"
    context_object_name = "latest_product_list"
    
    def get_queryset(self):
        """return de last five published questions"""
        #traerlas desde las mas recientes hasta las mas antiguas con el -pub_date
        return Productos.objects.all()

def listado(request):
    #return render(request, 'shop/index.html')
    content=[]
    for items in productos:
        content.append(f"""
            <p> <strong> {items['name']} </strong> </p>
        """)
    post = 5
    return HttpResponse("<br>".join(content))

def listTemplate(request):
    return render(request, 'shop/index.html', {'productos': productos})

def crearProducto(request):
    return render(request, 'shop/crearproducto.html')

class ShopView(APIView):
    parser_classes = (MultiPartParser, FormParser)

    def get(self, request, *args, **kwargs):
        articulos = Productos.objects.all()
        serializer = ShopSerializer(articulos, many = True)
        return Response(serializer.data)

    def post(self, request,*args, **kwargs):
        print(request.data)
        print(request)
        shop_serializer = ShopSerializer(data=request.data)
        if shop_serializer.is_valid():
            #shop_serializer.save()
            print(shop_serializer.data)
            #print("we did it")
            

        #return Response(shop_serializer.data, status=status.HTTP_201_CREATED)
        return Response("listo")