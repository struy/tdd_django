from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response

# Create your views here.
def index(request):
    # return HttpResponse()
    return render_to_response('solos/index.html')
    