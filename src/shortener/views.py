from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from django.views import View


from .forms import SubmitUrlForm
from .models import KirrURL
# Create your views here.
"""def Kirr_redirect_view(request, shortcode =None, *args, **kwargs):
	obj = get_object_or_404(KirrURL, shortcode=shortcode)
	return  HttpResponseRedirect(obj.url)
"""
def home_view_fbv(request, *args, **kwargs):
	if request.method =="POST":
		print (request.POST)
	return render(request, "shortener/home.html",{})

class HomeView(View):
	def get(self ,request ,*args, **kwargs):
		the_form = SubmitUrlForm()
		context = {
			"title" : "kirr.co",
			"form" : the_form
		}
		return render(request, "shortener/home.html",context)

	def post(self,request, *args, **kwargs):
		form = SubmitUrlForm(request.POST)
		if form.is_valid():
			print(form.cleaned_data)

		context = {
		"title" : "kirr.co",
		"form" : the_form
		}
		return render (request, "shortener/home.html",context)

class KirrCBView(View):
	def get(self,request, shortcode=None,*args,**kwargs):
		obj = get_object_or_404(KirrURL, shortcode=shortcode)
		return HttpResponseRedirect(obj.url)


