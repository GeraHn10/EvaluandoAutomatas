import json
from collections import OrderedDict
from Evaluadores import *

class Automatas:
        
  def nfae_dfa(self,alphabet, states, initial_state, accepting_states, transitions):
   
   cerraduraEpsilon=[]

   for est in states:
     newCerr = ''
     for trans in transitions:
       if trans[0]==est and trans[1]=='e':
         newCerr=newCerr+trans[2]
     newCerr=newCerr+est
     cerraduraEpsilon.append((est,newCerr))

   
   #print(cerraduraEpsilon)
   #print("---------------Cerradura Epsilon-------------------------") 
   for i in range(len(cerraduraEpsilon)):
      newword = list(OrderedDict.fromkeys(cerraduraEpsilon[i][1]))
      concatword=""
      for c in newword:
          concatword= concatword+c
      cerraduraEpsilon[i]=(cerraduraEpsilon[i][0],concatword)
   deltaCerraduraEpsilon=[]

   for alph in alphabet:
     #print(alph)
     for tuples in cerraduraEpsilon:
       newDeltWord=""
       for char in tuples[1]:
         #print(char)
         for trans in transitions:
           if char==trans[0] and alph==trans[1]:
             #print(trans)
             newDeltWord=newDeltWord+trans[2]
       #print(newDeltWord) 
       #print(trans[1])
       deltaCerraduraEpsilon.append((newDeltWord,alph,tuples[0]))
   #print(deltaCerraduraEpsilon)
   #print("------------Gerardo Gonzales--------------")
   cerraduradeltaEpsilon=[]
   
   for delt in deltaCerraduraEpsilon:
     #print(delt)
     posibleWord=""
     for char in delt[0]:
       #print(char)
       for trand in cerraduraEpsilon:
          #print(trand)
          if char==trand[0]:
            posibleWord=posibleWord+trand[1]
     #print(posibleWord)
     #print(delt[2])        
     cerraduradeltaEpsilon.append((posibleWord,delt[1],delt[2])) 

   #print(cerraduradeltaEpsilon) 

   for i in range(len(cerraduradeltaEpsilon)):
      newword = list(OrderedDict.fromkeys(cerraduradeltaEpsilon[i][0]))
      concatword=""
      #print(newword)
      for c in newword:
          concatword= concatword+c
      cerraduradeltaEpsilon[i]=(concatword,cerraduradeltaEpsilon[i][1],cerraduradeltaEpsilon[i][2]) 
      concatword=""
   
   #print(cerraduradeltaEpsilon)

   

   #NFa simple to dfa
   transhelp=[]
   for start in cerraduradeltaEpsilon:
     if start[2]==initial_state:
        transhelp.append((start[2],start[1],start[0]))

   
   for test in transhelp:
    ing=True
    estado=""
    for aux in transhelp:
      if test[2]==aux[0] or test[2] == '' :
        ing=False
    if ing==True:
     if test[2] not in states:
       states.append(test[2])
     for alp in alphabet: 
       val="" 
       #print(test[2])
       for cahr in test[2]:
         #print(cahr)
         for trans in cerraduradeltaEpsilon:
            #print(trans)
            if trans[2]==cahr and trans[1]==alp:
              val = val + trans[0]
       transhelp.append((test[2],alp,val))  


   #print(transhelp)
   #print("----------Estados------------------")
   #print(states)

   
   #print(states)A
    
   for accepting in accepting_states:
     val=False
     for est in states:
       if accepting in est:
         val=True
         if est != accepting and val==True:
           accepting_states.append(est)   
   #print(accepting_states)
   
   #print(cerraduradeltaEpsilon)
   transicionesfinales=[]
   for t in transhelp:
     if(t[2]!=''):
       transicionesfinales.append((t[0],t[1],t[2]))
   
   #print(transicionesfinales)
   print("Ingrese Cadena a evaluar")
   src=input()
   ev = Evaluadores()
   ev.dfa_evaluate(alphabet,states,initial_state,accepting_states,transicionesfinales,src)
   

  def expresionregular(self,expresion):
   alfabeto = []
   estados = []
   estados_iniciales = []
   estados_aceptados = []
   transiciones = {}
   for evaluando in expresion:
     if evaluando.isalpha() ==True and evaluando not in alfabeto:
       alfabeto.append(evaluando)

   if expresion[1]=="+":
    print(expresion) 
   if expresion[1]=="*":
    print(expresion)


  
        
      
      

   
   

 

  



