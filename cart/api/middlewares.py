from rest_framework.exceptions import AuthenticationFailed
import requests
from django.http import HttpResponse
import os

class TokenMiddleware:
    def __init__(self, get_response):
        self.get_response = get_response
        
    def __call__(self, request):
        allowed_url = ['/login/', '/verify/', '/register/', '/']
        
        # if request.path not in allowed_url and not request.path.startswith('/admin/'):
        if not request.path.startswith('/admin/'):
        
        
            if request.META.get('HTTP_AUTHORIZATION') is not None:
                token = request.META.get('HTTP_AUTHORIZATION')
                token = token.split(' ')
                # url = "https://127.0.0.1:8000/validate/"
                url = os.environ["VERIFY_URL"]
                print(url)
                headers = {"Authorization": "Token " + token[1]}
                data = {'auth':token[1]}
                res = requests.post(url, data=data, verify=False)
                # print(res.json())
                if res.status_code!=200:
                    return HttpResponse("Auth token invalid", status=400)
                request.session["userID"]=res.json()["user"]["id"]
            else:
                return HttpResponse("No Auth token provided", status=400)
        
        response = self.get_response(request)
        return response
    


class TestMiddleware:
    def __init__(self, get_response):
        print("In init")
        
        self.get_response = get_response
        
    def __call__(self, request):
        print("In call")
        response = self.get_response(request)
        return response



    