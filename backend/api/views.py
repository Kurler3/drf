from django.http import JsonResponse

def api_home(req, *args, **kwargs):
    
    body = req.body
    
    print(body)
    
    return JsonResponse({"message": "Hi there, this is your Django API Response!!"})
    