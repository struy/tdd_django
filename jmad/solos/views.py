from django.shortcuts import render
from django.http import HttpResponse
from django.shortcuts import render_to_response
from solos.models import Solo


def index(request):
    # return HttpResponse()
    context = {'solos': Solo.objects.filter(
        instrument=request.GET.get(
        'instrument', None))}
    return render_to_response('solos/index.html', context)
    