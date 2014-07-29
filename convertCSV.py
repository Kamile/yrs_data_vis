"""convert CSV to JSON  - of a table made up of continents->regions->countries
Kamile Matulenaite 28.07.14

ps you could add mentions of these countries on twitter in real-time :-))

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
        
        if (currentLine[0] == "Africa" or currentLine[0] == "Asia" or currentLine[0] == "Europe" or currentLine[0] == "Latin America and Caribbean" or currentLine[0] == "Northern America" or currentLine[0] == "Oceania"):
             if (Countries != {}): #Continents holds Regions which holds countries
                 if continent =="":
                     continent = currentLine[0]
                     
                 continentsObj["name"] = continent
                 continentsObj["children"] = Countries
                 Continents.append(continentsObj)

                 
                 continentsObj = {}
                 
            
            
             continent = currentLine[0]
        
        else:
            country["name"] = currentLine[0]
            country["size"] = int(currentLine[1])
            Countries.append(country)

            if currentLine[0] == "Wallis and Futuna Islands":

                continentsObj["name"] = continent
                continentsObj["children"] = Countries
                Continents.append(continentsObj)
            
            country = {}
        
        
    
    
    result["name"] = "flare"
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
    


