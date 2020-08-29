import json

with open('evaluando.json') as contenido:
 defincionAutomata = json.load(contenido)
 for automataValores in defincionAutomata['Automata']:
        alfabeto = automataValores['alphabet']
        estados = automataValores['states']
        estados_iniciales = automataValores['initial_state']
        estados_aceptados = automataValores['accepting_states']
        transiciones = automataValores['transitions']

print(transiciones)