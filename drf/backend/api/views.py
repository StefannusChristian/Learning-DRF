import json
from django.http import JsonResponse

def api_home(request, *args, **kwargs):
    body = request.body # byte string of JSON Data
    data = {}
    try:
        data = json.loads(body) # tsring of json data --> python dict
    except: pass
    data['params'] = dict(request.GET)
    data['headers'] = dict(request.headers)
    data['content_type'] = request.content_type
    print(data)
    return JsonResponse(data)