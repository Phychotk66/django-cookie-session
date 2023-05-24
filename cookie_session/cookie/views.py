from django.shortcuts import render
from datetime import datetime, timedelta
# Create your views here.
#set cookies fuction
def cookieset(request):
    response = render(request, 'set.html')
    response.set_signed_cookie('name', 'tareq', salt='nm', 
    expires = datetime.utcnow()+timedelta(days=2))
    return response
#get cookies funtion
def cookieget(request):
    name = request.get_signed_cookie('name', default="Guest", salt='nm')
    return render(request, 'get.html', {'name':'name'})

#delet cookie function
def cookiedlt(request):
    response = render(request, 'dlt.html')
    response.delete_cookie('name')
    return response

