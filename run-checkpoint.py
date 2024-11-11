import json

sample_data = json.load(open('joueurs.json', 'r'))
names = []
for obj in sample_data:
    for j in range(0, int(obj["occurrence"])):
        names.append(obj["name"])
        
with open("liste_noms.txt", 'w') as file:
    file.write("\n".join(names))
    

