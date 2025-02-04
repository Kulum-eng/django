from typing import Any
from django.http import HttpResponse
from django.views.generic import TemplateView
from .models import Carrera
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

def index(request):
    return HttpResponse ("Hola mundo")

class HomePageView(TemplateView):
    template_name='home.html'
    model= Carrera
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["saludo"]="hola de nuevo"
        context["lista"]=self.model.objects.all()
        return context

class AboutPageView(TemplateView):
    template_name='about.html'