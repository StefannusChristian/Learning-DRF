import json
from django.http import JsonResponse
from products.models import Product

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

    # <-- Django Model Instance as API Response -->
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # model instance (model_data)
        # turn a Python dict
        # return JSON to my client
    return JsonResponse(data)