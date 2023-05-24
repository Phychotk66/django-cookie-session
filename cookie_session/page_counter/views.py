from django.shortcuts import render

# Create your views here.
def pagecounte(request):
    ct = request.session.get('count', 0)
    newct = ct + 1
    request.session['count'] = newct
    return render(request, "home.html", {'c':newct})