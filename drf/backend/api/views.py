import json
from django.http import JsonResponse
from django.forms.models import model_to_dict
from products.models import Product
from rest_framework.response import Response
from rest_framework.decorators import api_view
from products.serializers import ProductSerializer

@api_view(["POST","GET"])
def api_home(request, *args, **kwargs):
    # <-- GET ECHO DATA SECTION -->
    # body = request.body # byte string of JSON Data
    # data = {}
    # try:
    #     data = json.loads(body) # tsring of json data --> python dict
    # except: pass
    # data['params'] = dict(request.GET)
    # data['headers'] = dict(request.headers)
    # data['content_type'] = request.content_type
    # print(data)
    # <-- GET ECHO DATA SECTION -->

    """
    DRF API VIEW
    """
    serializer = ProductSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        data = serializer.save()
        print(data)
        return Response(serializer.data)
    return Response({"invalid":"not good data"},status=400)

    # <-- Django Model Instance as API Response -->
    instance = Product.objects.all().order_by("?").first()
    data = {}
    if instance:
        # data['id'] = instance.id
        # data['title'] = instance.title
        # data['content'] = instance.content
        # data['price'] = instance.price
        # model instance (instance)
        # turn a Python dict
        # return JSON to my client
    # <-- Django Model Instance as API Response -->

   # <-- Django Model Instance to Dictionary -->
        # data = model_to_dict(instance, fields=['id', 'title','sale_price'])
        data = ProductSerializer(instance).data

    return JsonResponse(data)