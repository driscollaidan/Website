import numpy as np
import pandas as pd
from io import BytesIO
import base64
import matplotlib
import matplotlib.pyplot as plt


def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(first_county, second_county, data1, data2):
    plt.switch_backend('AGG')



    # dictionaries containing metadata for plotting graphs
    Carson_dict = {'BS':['map\data\Carson Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Carson County (2019-Present)'],
                'DP':['map\data\Carson Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Carson County (2019-Present)'],
                'PENPET':['map\data\Carson Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Carson County (2019-Present)'],
                'TSP': ['map\data\Carson Avg Turf Soil Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Carson County (2019-Present)'],
                'WC': ['map\data\Carson Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Carson County (2019-Present)'],
                'WS': ['map\data\Carson Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Carson County (2019-Present)'],
                'AT': ['map\data\Carson AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Carson County (2019-Present)'],
                'MWS': ['map\data\Carson Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Carson County (2019-Present)'],
                'MaxT': ['map\data\Carson MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Carson County (2019-Present)'],
                'MinT': ['map\data\Carson MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Carson County (2019-Present)'],
                'TPP':['map\data\Carson Total Penman PET.csv','Inches', 'Average Penman PET for Mesonet Carson County (2019-Present)'],
                'TSR': ['map\data\Carson Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Carson County (2019-Present)']}


    Fort_Yates_dict = {'BS':['map\data\Fort Yates Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Fort Yates County (2019-Present)'],
                'DP':['map\data\Fort Yates Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Fort Yates County (2019-Present)'],
                'PENPET':['map\data\Fort Yates Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Fort Yates County (2019-Present)'],
                'TSP': ['map\data\Fort Yates Avg Turf Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Fort Yates County (2019-Present)'],
                'WC': ['map\data\Fort Yates Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Fort Yates County (2019-Present)'],
                'WS': ['map\data\Fort Yates Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Fort Yates County (2019-Present)'],
                'AT': ['map\data\Fort Yates AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Fort Yates County (2019-Present)'],
                'MWS': ['map\data\Fort Yates Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Fort Yates County (2019-Present)'],
                'MaxT': ['map\data\Fort Yates MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Fort Yates County (2019-Present)'],
                'MinT': ['map\data\Fort Yates MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Fort Yates County (2019-Present)'],
                'TPP':['map\data\Fort Yates Total Penman PET.csv','Inches', 'Total Penman PET for Mesonet Fort Yates County (2019-Present)'],
                'TSR': ['map\data\Fort Yates Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Fort Yates County (2019-Present)']}


    Linton_dict = {'BS':['map\data\Linton Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Linton County (2019-Present)'],
                'DP':['map\data\Linton Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Linton County (2019-Present)'],
                'PENPET':['map\data\Linton Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Linton County (2019-Present)'],
                'TSP': ['map\data\Linton Avg Turf Soil Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Linton County (2019-Present)'],
                'WC': ['map\data\Linton Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Linton County (2019-Present)'],
                'WS': ['map\data\Linton Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Linton County (2019-Present)'],
                'AT': ['map\data\Linton AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Linton County (2019-Present)'],
                'MWS': ['map\data\Linton Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Linton County (2019-Present)'],
                'MaxT': ['map\data\Linton MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Linton County (2019-Present)'],
                'MinT': ['map\data\Linton MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Linton County (2019-Present)'],
                'TPP':['map\data\Linton Total Penman PET.csv','Inches', 'Total Penman PET for Mesonet Linton County (2019-Present)'],
                'TSR': ['map\data\Linton Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Linton County (2019-Present)']}

    if data2 == "N":
        num_graphs = '1'

    else:
        num_graphs = '2'

    if num_graphs == '1':
        
        location = first_county
        
        
        if location == 'C':
            location_dict = Carson_dict
        elif location == 'F':
            location_dict = Fort_Yates_dict
        elif location == 'L':
            location_dict = Linton_dict
        


        graph = data1
        
        # extracts data from dictionary list
        data_list1 = location_dict[f'{graph}']
        dataa = pd.read_csv(data_list1[0])
        ylabel1 = data_list1[1]
        title1 = data_list1[2]
        
        x1 = dataa['Period']
        y1 = dataa['Value']
        
        # gets legend title from csv file name
        legend1 = data_list1[0]
        label1 = legend1.strip('map\data\.csv')
        label1 = label1.strip('map\data\.csv')
        print(label1)
        
        
        # hardcodes x axis elements. will need to be changed later
        objects = ('Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020','Dec 2020', 'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021')
        x_ticks = np.arange(len(objects))
        
        # uses subplots to plot graph
        fig, ax1 = plt.subplots()
        ax1.plot(x1, y1, color='r')
        ax1.set_ylabel(ylabel1, color = 'r')
        ax1.set_xlabel('Months')
        ax1.set_xticks(x_ticks)
        ax1.set_xticklabels(objects, rotation=90)
        ax1.tick_params(axis = 'y', colors='r')
        ax1.set_title(title1)
        ax1.grid()

        
    if num_graphs == '2': 

            # user input location and type of data 1
            location1 = first_county
            graph1 = data1
            
            
            if location1 == 'C':
                location1_dict = Carson_dict
            elif location1 == 'F':
                location1_dict = Fort_Yates_dict
            elif location1 == 'L':
                location1_dict = Linton_dict
                
        
            # user input location and type of data 1
            location2 = second_county
            graph2 = data2
            
            
            if location2 == 'C':
                location2_dict = Carson_dict
            elif location2 == 'F':
                location2_dict = Fort_Yates_dict
            elif location2 == 'L':
                location2_dict = Linton_dict
            
            
    
            # extracts data from dictionary list
            data_list1 = location1_dict[f'{graph1}']
            data_list2 = location2_dict[f'{graph2}']
            
            # for data with different unit of measurements
            if data_list1[1] != data_list2[1]:         
            # breaks down data from dictionary
                dataa = pd.read_csv(data_list1[0])
                datab = pd.read_csv(data_list2[0])
            
                x1 = dataa['Period']
                y1 = dataa['Value']
            
                x2 = datab['Period']
                y2 = datab['Value']
            
            
            
                ylabel1 = data_list1[1]
                title1 = data_list1[2]
            
            
                ylabel2 = data_list2[1]
                title2 = data_list2[2]
            
            
                legend1 = data_list1[0]
                label1 = legend1.strip('map\data\.csv')
                label1 = label1.strip('map\data\.csv')
            
                legend2 = data_list2[0]
                label2 = legend2.strip('map\data\.csv')
                label2 = label2.strip('map\data\.csv')
            
                # hardcodes x axis elements. will need to change later
                objects = ('Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020','Dec 2020', 'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021')
                x_ticks = np.arange(len(objects))
            
                # plots data set one
                fig, ax1 = plt.subplots()
                ax1.plot(x1, y1, color='r')
                ax1.set_ylabel(ylabel1, color = 'r')
                ax1.set_xlabel('Months')
                ax1.set_xticks(x_ticks)
                ax1.set_xticklabels(objects, rotation=90)
                ax1.tick_params(axis = 'y', colors='r')
                ax1.set_title(f'{label1} and {label2} (2019-present)')
                ax1.grid()
            
                # uses subplots to plot second data set
                ax2 = ax1.twinx()
                ax2.plot(x2, y2, color = 'b')
                ax2.set_ylabel(ylabel2, color = 'b')
                ax2.tick_params(colors='b')
                ax2.grid()

            #plot when both variables have the same units of measurement
            if data_list1[1] == data_list2[1]: 
                # breaks down data from dictionary
                dataa = pd.read_csv(data_list1[0])
                datab = pd.read_csv(data_list2[0])
            
            
            
                x1 = dataa['Period']
                y1 = dataa['Value']
            
                x2 = datab['Period']
                y2 = datab['Value']
            
                ylabel1 = data_list1[1]
                title1 = data_list1[2]
            
            
                # ylabel2 = data_list2[1]
                title2 = data_list2[2]
            
            
                legend1 = data_list1[0]
                label1 = legend1.strip('graphing\data\.csv')
                label1 = label1.strip('map\data\.csv')
            
                legend2 = data_list2[0]
                label2 = legend2.strip('graphing\data\.csv')
                label2 = label2.strip('map\data\.csv')
            
                # hardodes x axis elements. will need to change later
                objects = ('Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020','Dec 2020', 'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021')
                x_ticks = np.arange(len(objects))
            
                # plots both data sets on same fig, one y axis
                fig, ax1 = plt.subplots()
                ax1.plot(x1, y1, color='r')
                ax1.plot(x2, y2, color = 'b')
                ax1.set_ylabel(ylabel1)
                ax1.set_xlabel('Months')
                ax1.set_xticks(x_ticks)
                ax1.set_xticklabels(objects, rotation=90)

                ax1.set_title(f'{label1} and {label2} (2019-present)')
                ax1.grid()
        
    graph = get_graph()
    return graph
        