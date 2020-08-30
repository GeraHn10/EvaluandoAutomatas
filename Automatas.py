import json
from collections import OrderedDict
class Automatas:

  def definirTipo(self,transiciones):
    return 1

        
  def nfae_dfa(self,alphabet, states, initial_state, accepting_states, transitions):
   
   cerraduraEpsilon=[]

   for est in states:
     newCerr = ''
     for trans in transitions:
       if trans[0]==est and trans[1]=='e':
         newCerr=newCerr+trans[2]
     newCerr=newCerr+est
     cerraduraEpsilon.append((est,newCerr))
    
   
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

   cerraduradeltaEpsilon=[]
   
   for delt in deltaCerraduraEpsilon:
     #print(delt)
     for char in delt[0]:
       #print(char)
       for trand in cerraduraEpsilon:
          if char==




        
      
      

   
   

 

  



