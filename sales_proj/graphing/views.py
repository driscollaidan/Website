from django.shortcuts import render
#from.models import Sale
from .graphs import get_plot
# Create your views here.

def main_view(request):
    chart = get_plot()
    return render(request, 'graphing/main.html', {'chart': chart})