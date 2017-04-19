from django.shortcuts import render
from django.views.generic.detail import DetailView
from django.views.generic.list import ListView
from clients.models import Clients_det
# Create your views here.

class Clints_det_DetailView(DetailView):
    model = Clients_det
    def get_context_data(self, **kwargs):
        context = super(Clints_det_DetailView, super).get_context_data(**kwargs)
        return context
    
    

class Clients_list(ListView):
    model = Clients_det
    def get_context_data(self, **kwargs):
        return ListView.get_context_data(self, **kwargs)
    
    
class Clients_search(ListView):
    model = Clients_det
    
    
    def get_queryset(self):
        return ListView.get_queryset(self)
    