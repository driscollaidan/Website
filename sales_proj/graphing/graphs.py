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

def get_plot():
    plt.switch_backend('AGG')



    # dictionaries containing metadata for plotting graphs
    Carson_dict = {'BS':['graphing\data\Carson Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Carson County (2019-Present)'],
                'DP':['graphing\data\Carson Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Carson County (2019-Present)'],
                'PENPET':['graphing\data\Carson Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Carson County (2019-Present)'],
                'TSP': ['graphing\data\Carson Avg Turf Soil Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Carson County (2019-Present)'],
                'WC': ['graphing\data\Carson Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Carson County (2019-Present)'],
                'WS': ['graphing\data\Carson Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Carson County (2019-Present)'],
                'AT': ['graphing\data\Carson AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Carson County (2019-Present)'],
                'MWS': ['graphing\data\Carson Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Carson County (2019-Present)'],
                'MaxT': ['graphing\data\Carson MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Carson County (2019-Present)'],
                'MinT': ['graphing\data\Carson MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Carson County (2019-Present)'],
                'TPP':['graphing\data\Carson Total Penman PET.csv','Inches', 'Average Penman PET for Mesonet Carson County (2019-Present)'],
                'TSR': ['graphing\data\Carson Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Carson County (2019-Present)']}


    Fort_Yates_dict = {'BS':['graphing\data\Fort Yates Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Fort Yates County (2019-Present)'],
                'DP':['graphing\data\Fort Yates Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Fort Yates County (2019-Present)'],
                'PENPET':['graphing\data\Fort Yates Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Fort Yates County (2019-Present)'],
                'TSP': ['graphing\data\Fort Yates Avg Turf Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Fort Yates County (2019-Present)'],
                'WC': ['graphing\data\Fort Yates Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Fort Yates County (2019-Present)'],
                'WS': ['graphing\data\Fort Yates Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Fort Yates County (2019-Present)'],
                'AT': ['graphing\data\Fort Yates AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Fort Yates County (2019-Present)'],
                'MWS': ['graphing\data\Fort Yates Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Fort Yates County (2019-Present)'],
                'MaxT': ['graphing\data\Fort Yates MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Fort Yates County (2019-Present)'],
                'MinT': ['graphing\data\Fort Yates MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Fort Yates County (2019-Present)'],
                'TPP':['graphing\data\Fort Yates Total Penman PET.csv','Inches', 'Total Penman PET for Mesonet Fort Yates County (2019-Present)'],
                'TSR': ['graphing\data\Fort Yates Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Fort Yates County (2019-Present)']}


    Linton_dict = {'BS':['graphing\data\Linton Avg Bare Soil Temp.csv', 'Temperature (F)', 'Average Bare Soil Temperature for Mesonet Linton County (2019-Present)'],
                'DP':['graphing\data\Linton Avg Dew Point.csv', 'Temperature (F)', 'Average Dew Point for Mesonet Linton County (2019-Present)'],
                'PENPET':['graphing\data\Linton Avg Penman PET.csv', 'Inches', 'Average Penman PET for Mesonet Linton County (2019-Present)'],
                'TSP': ['graphing\data\Linton Avg Turf Soil Temp.csv', 'Temperature (F)', 'Average Turf Soil Temperature for Mesonet Linton County (2019-Present)'],
                'WC': ['graphing\data\Linton Avg Wind Chill.csv', 'Temperature (F)', 'Average Wind Chill for Mesonet Linton County (2019-Present)'],
                'WS': ['graphing\data\Linton Avg Wind Speed.csv', 'Miles Per Hour', 'Average Wind Speed for Mesonet Linton County (2019-Present)'],
                'AT': ['graphing\data\Linton AvgTemp.csv', 'Temperature (F)', 'Average Temperature for Mesonet Linton County (2019-Present)'],
                'MWS': ['graphing\data\Linton Max Wind Speed.csv', 'Miles Per Hour', 'Maximum Wind Speed for Mesonet Linton County (2019-Present)'],
                'MaxT': ['graphing\data\Linton MaxTemp.csv', 'Temperature (F)', 'Maximum Temperature for Mesonet Linton County (2019-Present)'],
                'MinT': ['graphing\data\Linton MinTemp.csv', 'Temperature (F)', 'Minimum Temperature for Mesonet Linton County (2019-Present)'],
                'TPP':['graphing\data\Linton Total Penman PET.csv','Inches', 'Total Penman PET for Mesonet Linton County (2019-Present)'],
                'TSR': ['graphing\data\Linton Total Solar Radiation.csv', 'Lysine', 'Total Solar Radiation for Mesonet Linton County (2019-Present)']}


    num_graphs = input("How many data sets would you like to see? 1 or 2: \n") 

    if num_graphs == '1':
        
        location = input('Please select location Carson(C), Fort Yates(F), or Linton(L)\n')
        
        
        if location == 'C':
            location_dict = Carson_dict
        elif location == 'F':
            location_dict = Fort_Yates_dict
        elif location == 'L':
            location_dict = Linton_dict
        


        graph = input('select data set: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPET) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n')
        
        # extracts data from dictionary list
        data_list1 = location_dict[f'{graph}']
        data1 = pd.read_csv(data_list1[0])
        ylabel1 = data_list1[1]
        title1 = data_list1[2]
        
        x1 = data1['Period']
        y1 = data1['Value']
        
        # gets legend title from csv file name
        legend1 = data_list1[0]
        label1 = legend1.strip('graphing\data\.csv')
        
        
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
            location1 = input('Please select first location Carson(C), Fort Yates(F), or Linton(L)\n')   
            graph1 = input('select first data set: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPETc) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n')
            
            
            if location1 == 'C':
                location1_dict = Carson_dict
            elif location1 == 'F':
                location1_dict = Fort_Yates_dict
            elif location1 == 'L':
                location1_dict = Linton_dict
                
        
            # user input location and type of data 1
            location2 = input('Please select second location Carson(C), Fort Yates(F), or Linton(L)\n')
            graph2 = input('select second data set: \n Bare Soil(BS)  \n Temp Dew Point(DP) \n Penman PET(PENPET) \n Turf Soil Temp(TSP) \n Wind Chill(WC) \n Wind Speed(WS) \n Average Temp(AT) \n Max Wind Speed(MWS) \n Max Temp(MaxT) \n Min Temp(MinT) \n Total Penman PET(TPP) \n Total Solar Radiation(TSR)\n')
            
            
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
                data1 = pd.read_csv(data_list1[0])
                data2 = pd.read_csv(data_list2[0])
            
                x1 = data1['Period']
                y1 = data1['Value']
            
                x2 = data2['Period']
                y2 = data2['Value']
            
            
            
                ylabel1 = data_list1[1]
                title1 = data_list1[2]
            
            
                ylabel2 = data_list2[1]
                title2 = data_list2[2]
            
            
                legend1 = data_list1[0]
                label1 = legend1.strip('graphing\data\.csv')
            
                legend2 = data_list2[0]
                label2 = legend2.strip('graphing\data\.csv')
            
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
                data1 = pd.read_csv(data_list1[0])
                data2 = pd.read_csv(data_list2[0])
            
            
            
                x1 = data1['Period']
                y1 = data1['Value']
            
                x2 = data2['Period']
                y2 = data2['Value']
            
                ylabel1 = data_list1[1]
                title1 = data_list1[2]
            
            
                # ylabel2 = data_list2[1]
                title2 = data_list2[2]
            
            
                legend1 = data_list1[0]
                label1 = legend1.strip('graphing\data\.csv')
            
                legend2 = data_list2[0]
                label2 = legend2.strip('graphing\data\.csv')
            
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
        