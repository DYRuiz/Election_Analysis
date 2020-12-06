counties=["Arapahoe","Denver","Jefferson"]

voting_data=[]
voting_data.append({"county":"Arapahoe","regisered_voters":422829})
voting_data.append({"county":"Denver","regisered_voters":463353})
voting_data.append({"county":"Jefferson","registerd_voters":432438})

if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

if "Arapahoe" in counties or "El Paso" in counties:
    print("Arapahoe or El Paso are in the list of counties")
else:
    print("Arapahoe and El Paso are not in the list of counties")

counties_tuple=("Arapahoe","Denver","Jefferson")
counties_dict={}
counties_dict["Arapahoe"]=422829
counties_dict["Denver"]=463353
counties_dict["Jefferson"]=432438

voting_data


