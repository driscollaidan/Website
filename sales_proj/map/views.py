from django.shortcuts import render
#from.models import Sale
from .graphs import get_plot
# Create your views here.


#Idea for relevance traacker. Add to running totals each time a specific graph is created for a certain area, 
# and display the most commonly produced graphs on the county pages
def main_view(request):
    first_county = request.POST['first_county']
    second_county = request.POST['second_county']
    data1 = request.POST['data1']
    data2 = request.POST['data2']

    chart = get_plot(first_county, second_county, data1, data2)
    return render(request, 'graphing/main.html', {'chart': chart})

def index(request):
    return render(request, 'map/index.html')

def Carson(request):
    chart1 = get_plot("C", "C", "BS", "N")
    chart2 = get_plot("C", "C", "AT", "N")
    chart3 = get_plot("C", "C", "DP", "N")
    return render(request, 'extensions/Carson.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )

def Fort_Yates(request):
    chart1 = get_plot("F", "F", "BS", "N")
    chart2 = get_plot("F", "F", "AT", "N")
    chart3 = get_plot("F", "F", "DP", "N")
    return render(request, 'extensions/Fort_Yates.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )

def Linton(request):
    chart1 = get_plot("L", "L", "BS", "N")
    chart2 = get_plot("L", "L", "AT", "N")
    chart3 = get_plot("L", "L", "DP", "N")
    return render(request, 'extensions/Linton.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )
