import numpy as np
import pandas as pd
from io import BytesIO
import base64
import matplotlib
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches
import statistics as stat

def get_graph():
    buffer = BytesIO()
    plt.savefig(buffer, format='png', bbox_inches='tight')
    buffer.seek(0)
    image_png = buffer.getvalue()
    graph = base64.b64encode(image_png)
    graph = graph.decode('utf-8')
    buffer.close()
    return graph

def get_plot(first_county, second_county, data1, data2, special):
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

    #Checks for Special Variable, one that is used for the generation of relevancy graphs
    if special == 0:    
        if data2 == "N":
            num_graphs = '1'

        else:
            num_graphs = '2'
    
    else:
        index = 0
        for letter in special:
            index += 1
            if index == 1:
                first_county = letter
            elif index == 2:
                data1 = letter
            elif index == 3:
                second_county = letter
            elif index == 4:
                data2 = letter

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
        
        
        # hardcodes x axis elements. will need to be changed later
        objects = ('Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020','Dec 2020', 'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021')
        x_ticks = np.arange(len(objects))
        
        
        red_patch = mpatches.Patch(color = 'r', label = f'{label1}')
        # uses subplots to plot graph
        fig, ax1 = plt.subplots()
        ax1.plot(x1, y1, color='r')
        ax1.set_ylabel(ylabel1, color = 'r')
        ax1.set_xlabel('Months')
        ax1.set_xticks(x_ticks)
        ax1.set_xticklabels(objects, rotation=90)
        ax1.tick_params(axis = 'y', colors='r')
        plt.legend(handles = [red_patch], loc = 'lower right')
        ax1.set_title(title1)
        ax1.grid()

        
        
        mean = round(stat.mean(y1),2)
        median = round(stat.median(y1),2)
        mini = round(min(y1),2)
        maxi = round(max(y1),2)
        st_dev = round(stat.stdev(y1),2)
        Range = round(maxi - mini,2)
        


        name_elements = ['Mean\n', 'Median\n', 'Min\n', 'Max\n', 'Range\n', 'St Dev\n']
        stats_elements = [f'{mean}\n', f'{median}\n', f'{mini}\n', f'{maxi}\n', f'{Range}\n', f'{st_dev}\n']
        y = 0.70
        
        
        plt.figtext(0.95, 0.79, label1, {'multialignment':'left'}, color = 'r')
        for i in range(0,6):

            plt.figtext(.95, y, name_elements[i], {'multialignment':'left'}, color = 'r')
            plt.figtext(1.05, y, stats_elements[i], {'multialignment':'right'}, color = 'r')
            y=y-0.05
        
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
            
            # user input location and type of data 2
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
            
                legend2 = data_list2[0]
                label2 = legend2.strip('map\data\.csv')
            
            
            
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
            
                red_patch = mpatches.Patch(color = 'r', label = f'{label1}')
                blue_patch = mpatches.Patch(color = 'b', label = f'{label2}') 
                plt.legend(handles = [red_patch, blue_patch], loc = 'lower right')
                
                
                # uses subplots to plot second data set
                ax2 = ax1.twinx()
                ax2.plot(x2, y2, color = 'b')
                ax2.set_ylabel(ylabel2, color = 'b')
                ax2.tick_params(colors='b')
                ax2.grid()
                
                
                
                
                
                
                mean1 = round(stat.mean(y1),2)
                median1 = round(stat.median(y1),2)
                mini1 = round(min(y1),2)
                maxi1 = round(max(y1),2)
                st_dev1 = round(stat.stdev(y1),2)
                Range1 = round(maxi1 - mini1,2)
                
                mean2 = round(stat.mean(y2),2)
                median2 = round(stat.median(y2),2)
                mini2 = round(min(y2),2)
                maxi2 = round(max(y2),2)
                st_dev2 = round(stat.stdev(y2),2)
                Range2 = round(maxi2 - mini2,2)


                name_elements1 = ['Mean\n', 'Median\n', 'Min\n', 'Max\n', 'Range\n', 'St Dev\n']
                stats_elements1 = [f'{mean1}\n', f'{median1}\n', f'{mini1}\n', f'{maxi1}\n', f'{Range1}\n', f'{st_dev1}\n']
                name_elements2 = ['Mean\n', 'Median\n', 'Min\n', 'Max\n', 'Range\n', 'St Dev\n']
                stats_elements2 = [f'{mean2}\n', f'{median2}\n', f'{mini2}\n', f'{maxi2}\n', f'{Range2}\n', f'{st_dev2}\n']
                
                y_1 = 0.70
                y_2 = 0.30
                
                
                plt.figtext(1.02, 0.79, label1, {'multialignment':'left'}, color = 'r')
                for i in range(0,6):

                    plt.figtext(1.02, y_1, name_elements1[i], {'multialignment':'left'}, color = 'r')
                    plt.figtext(1.12, y_1, stats_elements1[i], {'multialignment':'right'}, color = 'r')
                    y_1 = y_1 - 0.05
                
                
                plt.figtext(1.02, 0.39, label2, {'multialignment':'left'}, color = 'b')
                for i in range(0,6):

                    plt.figtext(1.02, y_2, name_elements2[i], {'multialignment':'left'}, color = 'b')
                    plt.figtext(1.12, y_2, stats_elements2[i], {'multialignment':'right'}, color = 'b')
                    y_2 = y_2 - 0.05
                    
                
            #plot when both variables have the same units of measurements
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
            
                ylabel2 = data_list2[1]
                title2 = data_list2[2]
            
                legend1 = data_list1[0]
                label1 = legend1.strip('map\data\.csv')
            
                legend2 = data_list2[0]
                label2 = legend2.strip('map\data\.csv')
            
            
            
                # hardodes x axis elements. will need to change later
                objects = ('Nov 2019', 'Dec 2019', 'Jan 2020', 'Feb 2020', 'Mar 2020', 'Apr 2020', 'May 2020', 'Jun 2020', 'Jul 2020', 'Aug 2020', 'Sep 2020', 'Oct 2020', 'Nov 2020','Dec 2020', 'Jan 2021', 'Feb 2021', 'Mar 2021', 'Apr 2021', 'May 2021', 'Jun 2021', 'Jul 2021', 'Aug 2021', 'Sep 2021', 'Oct 2021')
                x_ticks = np.arange(len(objects))
            
            
                # plots both data sets on same fig, one y axis
                fig, ax1 = plt.subplots()
                ax1.plot(x1, y1, color='r')
                
                red_patch = mpatches.Patch(color = 'r', label = f'{label1}')
                blue_patch = mpatches.Patch(color = 'b', label = f'{label2}') 
                
                ax1.plot(x2, y2, color = 'b')
        
                
                
                ax1.set_ylabel(ylabel1)
                ax1.set_xlabel('Months')
                ax1.set_xticks(x_ticks)
                ax1.set_xticklabels(objects, rotation=90)
                
                plt.legend(handles = [red_patch, blue_patch], loc = 'lower right')

                ax1.set_title(f'{label1} and {label2} (2019-present)')
                ax1.grid()
            
            
            
                mean1 = round(stat.mean(y1),2)
                median1 = round(stat.median(y1),2)
                mini1 = round(min(y1),2)
                maxi1 = round(max(y1),2)
                st_dev1 = round(stat.stdev(y1),2)
                Range1 = round(maxi1 - mini1,2)
                
                mean2 = round(stat.mean(y2),2)
                median2 = round(stat.median(y2),2)
                mini2 = round(min(y2),2)
                maxi2 = round(max(y2),2)
                st_dev2 = round(stat.stdev(y2),2)
                Range2 = round(maxi2 - mini2,2)


                name_elements1 = ['Mean\n', 'Median\n', 'Min\n', 'Max\n', 'Range\n', 'St Dev\n']
                stats_elements1 = [f'{mean1}\n', f'{median1}\n', f'{mini1}\n', f'{maxi1}\n', f'{Range1}\n', f'{st_dev1}\n']
                name_elements2 = ['Mean\n', 'Median\n', 'Min\n', 'Max\n', 'Range\n', 'St Dev\n']
                stats_elements2 = [f'{mean2}\n', f'{median2}\n', f'{mini2}\n', f'{maxi2}\n', f'{Range2}\n', f'{st_dev2}\n']
                
                y_1 = 0.70
                y_2 = 0.30
                
                
                plt.figtext(1.02, 0.79, label1, {'multialignment':'left'}, color = 'r')
                for i in range(0,6):

                    plt.figtext(1.02, y_1, name_elements1[i], {'multialignment':'left'}, color = 'r')
                    plt.figtext(1.12, y_1, stats_elements1[i], {'multialignment':'right'}, color = 'r')
                    y_1 = y_1 - 0.05
                
                
                plt.figtext(1.02, 0.39, label2, {'multialignment':'left'}, color = 'b')
                for i in range(0,6):

                    plt.figtext(1.02, y_2, name_elements2[i], {'multialignment':'left'}, color = 'b')
                    plt.figtext(1.12, y_2, stats_elements2[i], {'multialignment':'right'}, color = 'b')
                    y_2 = y_2 - 0.05
                

    graph = get_graph()
    return graph