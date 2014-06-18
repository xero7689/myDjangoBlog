from django.shortcuts import render
from django.views.generic import ListView
from work.models import Image
from blog2.settings import MEDIA_URL
# Create your views here.

class work(ListView):
	model = Image
	image = Image.objects.all()
	template_name = "work/work.html"
	
	def get(self, request, *args, **kwargs):
		return render(request, self.template_name, {"image": self.image,"media_url": MEDIA_URL})
