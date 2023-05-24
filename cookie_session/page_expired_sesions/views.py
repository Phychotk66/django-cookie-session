from django.shortcuts import render, HttpResponse

# Create your views here.
def sessionset(request):
    request.session['name'] = 'tareq'
    return render (request, 'sessionset.html')

def sessionget(request):
    if 'name' in request.session:
        name = request.session ['name']
        request.session.modified = True
        return render (request, 'sessionget.html', {'name':name})
    else:
        return HttpResponse('Your session expired')
        
def sessiondlt(request):
    request.session.flush()
    request.session.clear_expired()
    return render (request, 'sessiondlt.html')
    