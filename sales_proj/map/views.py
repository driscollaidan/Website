from django.shortcuts import render
from .graphs import get_plot
from .dictionary import Update_Dictionary, Get_Relevant_Maps
# Create your views here.

def main_view(request):

    #Uses most recently submitted data
    first_county = request.POST['first_county']
    second_county = request.POST['second_county']
    data1 = request.POST['data1']
    data2 = request.POST['data2']

    #Updates Dictionary Tracker
    Update_Dictionary(first_county, data1, second_county, data2)

    chart = get_plot(first_county, second_county, data1, data2, 0)
    return render(request, 'graphing/main.html', {'chart': chart})

def index(request):
    return render(request, 'map/index.html')

def Carson(request):

    chart1data, chart2data, chart3data = Get_Relevant_Maps("C")

    chart1 = get_plot(0, 0, 0, 0, chart1data)
    chart2 = get_plot(0, 0, 0, 0, chart2data)
    chart3 = get_plot(0, 0, 0, 0, chart3data)
    return render(request, 'extensions/Carson.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )

def Fort_Yates(request):

    chart1data, chart2data, chart3data = Get_Relevant_Maps("F")

    chart1 = get_plot(0, 0, 0, 0, chart1data)
    chart2 = get_plot(0, 0, 0, 0, chart2data)
    chart3 = get_plot(0, 0, 0, 0, chart3data)
    return render(request, 'extensions/Fort_Yates.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )

def Linton(request):
    
    chart1data, chart2data, chart3data = Get_Relevant_Maps("L")

    chart1 = get_plot(0, 0, 0, 0, chart1data)
    chart2 = get_plot(0, 0, 0, 0, chart2data)
    chart3 = get_plot(0, 0, 0, 0, chart3data)
    return render(request, 'extensions/Linton.html', {'chart1': chart1, 'chart2': chart2, 'chart3': chart3} )