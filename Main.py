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

 with open('evaluandodfa.json') as contenido:
  Automaton = json.load(contenido)
  for automatonValues in Automaton['Automata']:
        alphabet = automatonValues['alphabet']
        states = automatonValues['states']
        initial_states = automatonValues['initial_state']
        accepting_states = automatonValues['accepting_states']
        transitions = automatonValues['transitions']

                
 print("Ingrese cadena a evaluar:")
 src=input()

 con.dfa_evaluate(alphabet, states, initial_states, accepting_states, transitions,src)

if op=="2":
 
 with open('evaluando.json') as contenido:
  Automaton= json.load(contenido)
  for automatonValues in Automaton['Automata']:
        alphabet = automatonValues['alphabet']
        states = automatonValues['states']
        initial_states = automatonValues['initial_state']
        accepting_states = automatonValues['accepting_states']
        transitions = automatonValues['transitions']

 #print(alphabet)                  
  
 ev.nfae_dfa(alphabet, states, initial_states, accepting_states, transitions)

if op =="3":
      print("Ingrese su Expresion Regular:")
      expresion = input()
      ev.expresionregular(expresion)

#ev.nfatodfa(alfabeto,estados,estados_iniciales,estados_aceptados,transiciones)
#nfa_transition_dict[(starting_state, transition_symbol)] = [ending_state]


