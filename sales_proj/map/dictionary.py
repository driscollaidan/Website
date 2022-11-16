import json

#These three lines of code reset the dictionary. Only run them when FIRST setting up program
#Relevancey_Dictionary = {}
#with open('dictionary.txt', 'w') as file:
#       file.write(json.dumps(Relevancey_Dictionary))
  
def Update_Dictionary(first_county, data1, second_county, data2):
    
    with open('dictionary.txt', 'r') as file:
        data = file.read()
    Relevancey_Dictionary = json.loads(data)
    
    #Creates a key based off of imported data
    if second_county != "N":
        Key = first_county + " " + data1 + " " + second_county  + " " + data2
    else:
        Key = first_county + " " + data1 + " " + "N" + " " + "N"
        
    #If no graph data is stored, set to 1
    if Relevancey_Dictionary.get(Key, 0) == 0:
        Relevancey_Dictionary[Key] = 1
        
        with open ('keys.txt', 'a') as file:
            file.write(f"{Key}\n")
        
    #If data is stored, increase by 1
    elif Relevancey_Dictionary.get(Key,0) != 0:
        Relevancey_Dictionary[Key] = (Relevancey_Dictionary[Key] + 1)
        
    with open('dictionary.txt', 'w') as file:
          file.write(json.dumps(Relevancey_Dictionary))
    
def Get_Relevant_Maps(county):
    
    with open('dictionary.txt', 'r') as file:
        data = file.read()
    Relevancey_Dictionary = json.loads(data)
    
    Keys = []
    
    with open ('keys.txt', 'r') as file:
        for line in file:
            Keys.append(line.strip(""" \n"""))

    #Initial Values
    KeysforCounty = []
    Values = []
    OutportKeys = []
    
    #Narrows down selection for relevant maps by only including keys that match the chosen county
    for Key in Keys:
        for Letter in Key:
            if Letter == county:
                KeysforCounty.append(Key)
            break
    
    #Creates list of all values recorded in dictionary with remaining kys
    for Key in KeysforCounty:
        Values.append(Relevancey_Dictionary[Key])
        
    #Sorts the values into ascending order numerically
    Values.sort()
    
    #Creates list of the three greatest values (number of times created)
    RelevantValues = [Values[-1], Values[-2], Values[-3]]
    
    #Tries each key in dictionary until the right three are found
    index = 0
    for Key in KeysforCounty:
        for Value in RelevantValues:
            if Relevancey_Dictionary[Key] == Value:
                OutportKeys.append(Key)
                break
                
        index += 1
    
    index = 0
    for Key in OutportKeys: 
        for letter in Key:
            if index == 0:
                chart1data = "".join(Key)
                chart1data = chart1data.split(" ")
            if index == 1:
                chart2data = "".join(Key)
                chart2data = chart2data.split(" ")
            if index == 2:
                chart3data = "".join(Key)
                chart3data = chart3data.split(" ")
        index += 1
    
    #Returns three keys
    return chart1data, chart2data, chart3data 