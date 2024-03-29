
import json 

def create_dish(name, veggie = False, vegan = False, fish = False,
                beef = False, pork = False, chicken = False, healthy = False,
            allergenes = [], origin = 'Austrian',
            available_in = {}):
    
    dish = {
        'name': name,
        'veggie': veggie,
        'vegan' : vegan,
        'beef': beef,
        'pork': pork,
        'chicken': chicken, 
        'fish': fish,
        'healthy': healthy,
        'allergens': allergenes,
        'origin': origin,
        'available_in': available_in
        }
    
    #with open('data/dishes.json') as f:
    #dishes = json.load(f)
    
    #dishes['dishes'].append(dish)
    dishes = []
    dishes.append(dish)
    with open('data/dishes.json', 'w') as f:
        json.dump(dishes, f)
    
    return dish


create_dish('Ausgelöste Flußkrebserl mit Dill und Avocados auf Häuptlsalat',
            fish = True,
            healthy = True,
            available_in = {'ChIJ44eRDa2adkcRBpmhhcXRonA': {'price': 30}},
            allergenes = ['B', 'D', 'R']
            )

with open('data/dishes.json') as f:
    dishes = json.load(f)


dish = {
        'name': 'superawesomedish',
        'veggie': False,
        'fish': False,
        'allergens': [],
        'origin': [],
        'available_in': []
        }


allergenes = {
        'A': 'Glutenhaltige Getreide und daraus gewonnene Erzeugnisse',
        'B': 'Krebstiere und daraus gewonnene Erzeugnisse',
        'C': 'Eier von Geflügel und daraus gewonnene Erzeugnisse',
        'D': 'Fisch und daraus gewonnene Erzeugnisse (außer Fischgelatine)',
        'E': 'Erdnüsse und daraus gewonnene Erzeugnisse ',
        'F': 'Sojabohnen und daraus gewonnene Erzeugnisse', 
        'G': 'Milch von Säugetieren und Milcherzeugnisse (inklusive Laktose)',
        'H': 'Schalenfrüchte (Baumnüsse) und daraus gewonnene Erzeugnisse',
        'L': 'Sellerie und daraus gewonnene Erzeugnisse',
        'M': 'Senf und daraus gewonnene Erzeugnisse',
        'N': 'Sesamsamen und daraus gewonnene Erzeugnisse',
        'O': 'Schwefeldioxid und Sulfite',
        'P': 'Lupinen und daraus gewonnene Erzeugnisse',
        'R': 'Weichtiere und daraus gewonnene Erzeugnisse'
        }

