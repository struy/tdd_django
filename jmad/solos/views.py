from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response


def index(request):
    # return HttpResponse()
    return render_to_response('solos/index.html')
    