import json
from Evaluadores import *
from Automatas import *

alfabeto = []
estados = []
estados_iniciales = []
estados_aceptados = []
transiciones = {}
with open('evaluando.json') as contenido:
 defincionAutomata = json.load(contenido)
 for automataValores in defincionAutomata['Automata']:
        alfabeto = automataValores['alphabet']
        estados = automataValores['states']
        estados_iniciales = automataValores['initial_state']
        estados_aceptados = automataValores['accepting_states']
        transiciones = automataValores['transitions']
                  
ev=Automatas()
ev.nfae_dfa(alfabeto,estados,estados_iniciales,estados_aceptados,transiciones)
#nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]


