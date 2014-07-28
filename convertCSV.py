"""convert CSV to JSON  - of a table made up of continents->regions->countries
Kamile Matulenaite 28.07.14

ps you could add mentions of these countries on twitter in real-time :-))

"""

import json

def convert(f):
    lines = f.split("\n")
    
    result = {}
    
    Continents = []
    Regions = []
    Countries = []
    
    country = {}
    regionObj = {}
    continentsObj ={}
    
    continent = ""
    region = ""
    
    lineLength = len(lines)
    i=1
    
    while i < lineLength:
        
        currentLine = lines[i].split(",")
        
        if (currentLine[0] == "Africa" or currentLine[0] == "Asia" or currentLine[0] == "Europe" or currentLine[0] == "Latin America and Caribbean" or currentLine[0] == "Northern America" or currentLine[0] == "Oceania"):
             if (Regions != {}): #Continents holds Regions which holds countries
                 if continent =="":
                     continent = currentLine[0]
                     
                 continentsObj["name"] = continent
                 continentsObj["children"] = Regions
                 Continents.append(continentsObj)
                 #print(Continents)
                 
                 continentsObj = {}
                 
            
            
             continent = currentLine[0]  
        
            
        elif (currentLine[0] == "Eastern Africa" or currentLine[0] ==  "Central Africa" or currentLine[0] == "Northern Africa" or currentLine[0] == "Southern Africa" or currentLine[0] == "Western Africa" or currentLine[0] == "Eastern Asia" or currentLine[0] == "South-Central Asia" or currentLine[0] == "South-Eastern Asia" or currentLine[0] == "Western Asia" or currentLine[0] == "Eastern Europe" or currentLine[0] == "Northern Europe" or currentLine[0] == "Southern Europe" or currentLine[0] == "Western Europe" or currentLine[0] == "Caribbean" or currentLine[0] == "Central America" or currentLine[0] == "South America" or currentLine[0] == "Australia/New Zealand" or currentLine[0] == "Melanesia" or currentLine[0] == "Micronesia" or currentLine[0] == "Polynesia"):
            if (Countries != {}): 


                 print(currentLine[0])

                 if region =="":
                     region = currentLine[0]
                 
                 regionObj["name"] = region
                 regionObj["children"] = Countries
                 Regions.append(regionObj)
                
                 regionObj = {}
                 
            
            
            region = currentLine[0]
        
        else:
            country["name"] = currentLine[0]
            country["size"] = int(currentLine[1])

            
            
            Countries.append(country)
            
            country = {}


        i+=1
        
        
    
    
    result["name"] = "flare"
    result["children"] = Continents
    print(result)
    
    return json.dumps(result)
    


#print("yahoo")   
f = open("populationByContinent.csv","r")

contents = f.read()
f.close()

data = convert(contents)

f = open("flare.json","w")
f.write(data)
f.close()

#print(json)
    


