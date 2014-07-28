"""convert CSV to JSON  - of a table made up of continents->regions->countries
Kamile Matulenaite 28.07.14"""

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
        
        if (currentLine[0] == "Africa" or "Asia" or "Europe" or "Latin America and Caribbean" or "Northern America" or "Oceania"):
             if (Regions != {}): #Continents holds Regions which holds countries
                
                 continentsObj["name"] = continent
                 continentsObj["children"] = Regions
                 Continents.append(continentsObj)
                 
                 continentsObj = {}
                 
            
            
             continent = currentLine[0]  
        
            
        elif (currentLine[0] == "Eastern Africa" or "Central Africa" or "Northern Africa" or "Southern Africa" or "Western Africa" or "Eastern Asia" or "South-Central Asia" or "South-Eastern Asia" or "Western Asia" or "Eastern Europe" or "Northern Europe" or "Southern Europe" or "Western Europe" or "Caribbean" or "Central America" or "South America" or "Australia/New Zealand" or "Melanesia" or "Micronesia" or "Polynesia"):
            if (Countries != {}): 
                
                 regionObj["name"] = region
                 regionObj["children"] = Countries
                 Regions.append(regionObj)
                
                 regionObj = {}
                 
            
            
            region = currentLine[0]
        
        else:
            country["name"] = currentLine[0]
            country["size"] = int(currentLine[1])

            print(country +"\n")
            
            Countries.append(country)
            
            country = {}


        i+=1
        
        
    
    
    result["name"] = "flare"
    result["children"] = Continents
    
    return json.dumps(result)
    


#print("yahoo")   
f = open("populationByContinent.csv","r")
contents = f.read()


json = convert(contents)

print(json)
    


