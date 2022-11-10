from django.http import JsonResponse
import json

def api_home(req, *args, **kwargs):
    
    # BYTE STRING OF JSON DATA
    body = req.body
    
    data = {}
    
    try:
        data = json.loads(body)
    except:
        pass
    
    # HEADERS
    data['params'] = dict(req.GET)
    data['headers'] = dict(req.headers)
    data['content_type'] = req.content_type
    
    return JsonResponse(data)
    