import os
import requests
from django.http import HttpResponse

def user_token_athenticated(function):
    def wrap(request, *args, **kwargs):
        
        if len(args)==0: #Length of args is 0 if the decorator is applied to function based View. In that case header lies in request variable
            tok_header = request 
        else:
            tok_header = args[0] #If decorator applied to class based view. Pickup header from args[0] variable
        
        if tok_header.META.get('HTTP_AUTHORIZATION') is not None:
            token = tok_header.META.get('HTTP_AUTHORIZATION') #Format: Bearer <token>
            token = token.split(' ')
            url = os.environ["VERIFY_URL"]
            data = {'auth':token[1]}
            res = requests.post(url, data=data, verify=False)
            if res.status_code!=200:
                return HttpResponse("Auth token invalid", status=400)
            tok_header.session["userID"]=res.json()["user"]["id"]
        else:
            return HttpResponse("No Auth token provided", status=400)
        
        return function(tok_header, *args, **kwargs)
    wrap.__doc__ = function.__doc__
    wrap.__name__ = function.__name__
    return wrap