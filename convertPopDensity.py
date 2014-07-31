"""convert CSV to JSON  - of a table made up of continents->countries
Kamile Matulenaite 30.07.14
data from geohi& world bank
create
 json file for population density
 """

import json

def convert(f):
    lines = f.split("\n")
    
    result = {}
    
    Continents = []
    Countries = []
    
    country = {}
    continentsObj ={}
    continent = ""

    
    lineLength = len(lines)
    
    
    for line in lines[1:]: #because the first line contains headers
        
        currentLine = line.split(",")
        
        if (currentLine[0] == "Africa" or currentLine[0] == "Asia" or currentLine[0] == "Europe" or currentLine[0] == "Latin America and the Caribbean" or currentLine[0] == "Northern America" or currentLine[0] == "Oceania"):
             if currentLine[0] != "Africa":
                 print(currentLine[0])
                 continentsObj["name"] = continent
                 continentsObj["children"] = Countries
                 Continents.append(continentsObj)
                 continentsObj = {}
                 Countries = []

                 
             continent = currentLine[0]
        
        else:
            country["name"] = currentLine[0]

            population = float(currentLine[1])
            area = float(currentLine[2])
            density = population/area

            
            country["size"] = density

            Countries.append(country)
            #print(country)

            if currentLine[0] == "Wallis and Futuna Islands":

                continentsObj["name"] = continent
                continentsObj["children"] = Countries
                Continents.append(continentsObj)
            
            country = {}
        
        
    
    
    result["name"] = "flare"
    #print(Continents)
    result["children"] = Continents
    #print(result)
    
    return json.dumps(result)
    


#print("yahoo")   
f = open("populationByContinent.csv","r")

contents = f.read()
f.close()

data = convert(contents)

f = open("flare2.json","w")
f.write(data)
f.close()

#print(json)
    


