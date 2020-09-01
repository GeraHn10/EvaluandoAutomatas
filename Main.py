import json
#from Evaluadores import *
from Automatas import *
from Evaluadores import *
print("Main Menu")
print("1.Evaluar Dfa")
print("2.Evaluar Nfa-epsilon")
print("3.Evaluar Expresion Regular")
print("Ingrese un comando:")
op=input()
ev=Automatas()
con=Evaluadores()
if op=="1":
 alfabeto = []
 estados = []
 estados_iniciales = []
 estados_aceptados = []
 transiciones = {}
 with open('evaluandodfa.json') as contenido:
  defincionAutomata = json.load(contenido)
  for automataValores in defincionAutomata['Automata']:
        alfabeto = automataValores['alphabet']
        estados = automataValores['states']
        estados_iniciales = automataValores['initial_state']
        estados_aceptados = automataValores['accepting_states']
        transiciones = automataValores['transitions']

                
 print("Ingrese cadena a evaluar:")
 src=input()

 con.dfa_evaluate(alfabeto,estados,estados_iniciales,estados_aceptados,transiciones,src)

if op=="2":
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

 print(alfabeto)                  
  
 ev.nfae_dfa(alfabeto,estados,estados_iniciales,estados_aceptados,transiciones)

if op =="3":
      print("Ingrese su Expresion Regular:")
      expresion = input()
      ev.expresionregular(expresion)

#ev.nfatodfa(alfabeto,estados,estados_iniciales,estados_aceptados,transiciones)
#nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]


