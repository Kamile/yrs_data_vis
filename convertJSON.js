//convert CSV to JSON

function convert(f) {
    
    var lines = f.split("\n");
    
    var result = {};
    
    var Continents = [];
    var Regions = [];
    var Countries = [];
    
    var country = {};
    var regionObj = {};
    var continentsObj ={};
    
    var continent;
    var region;
    
    
    for (var i=1; i<lines.length; i++){
        
        currentLine = lines[i].split(",");
        
        if (currentLine[0] == "Africa" || "Asia" || "Europe" || "Latin America and Caribbean" || "Northern America" || "Oceania") {
             if (Regions != {}) { //Continents holds Regions which holds countries
                
                 continentsObj["name"] = continent;
                 continentsObj["children"] = Regions;
                 Continents.push(continentsObj);
                 
                 continentsObj = {};
                 
            }
            
            continent = currentLine[0];   
        }
            
        else if (currentLine[0] == "Eastern Africa" || "Central Africa" || "Northern Africa" || "Southern Africa" || "Western Africa" || "Eastern Asia" || "South-Central Asia" || "South-Eastern Asia" || "Western Asia" || "Eastern Europe" || "Northern Europe" || "Southern Europe" || "Western Europe" || "Caribbean" || "Central America" || "South America" || "Australia/New Zealand" || "Melanesia" || "Micronesia" || "Polynesia"){
            if (Countries != {}) { //Continents holds Regions which holds countries
                
                 regionObj["name"] = region;
                 regionObj["children"] = Countries;
                 Regions.push(regionObj);
                
                 regionObj = {};
                 
                 
            }
            
            region = currentLine[0];
        }
        else {
            country["name"] = currentLine[0];
            country["size"] = currentLine[1];
            
            Countries.push(country);
            
            country = {};
        
        }
        
    }
    
    result["name"] = "flare";
    result["children"] = Continents;
    
    return JSON.stringify(result);
    
}


