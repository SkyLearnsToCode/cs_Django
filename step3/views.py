from django.shortcuts import render

#Create your views here.
from django.shortcuts import render
from django.http import HttpResponseRedirect, HttpResponse, JsonResponse
from django.core.urlresolvers import reverse
from django.db import models

from .models import Name_Entity, Context_Slice, Friends

# from .forms import NameForm

def index(request):
     return HttpResponse("Welcome to Step 3")

def workspace(request, slice_id):

	return render(request, 'step3/step3.html')
def result(request, slice_id):
 	return HttpResponse("Welcome to result")
def addLink(request):
	if request.method == 'POST':
		tmp = RequestContext(request)
		return HttpResponse(tmp)
	else:
		return render(request, 'step3/step3.html')
	

# def get_name(request):
#     # if this is a POST request we need to process the form data
#     if request.method == 'POST':
#         # create a form instance and populate it with data from the request:
#         form = NameForm(request.POST)
#         # check whether it's valid:
#         if form.is_valid():
#             # process the data in form.cleaned_data as required
#             # ...
#             # redirect to a new URL:
#             return HttpResponseRedirect('/thanks/')

#     # if a GET (or any other method) we'll create a blank form
#     else:
#         form = NameForm()

#     return render(request, 'name.html', {'form': form})

