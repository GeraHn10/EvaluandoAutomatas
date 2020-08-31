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
   
   print(cerraduradeltaEpsilon)

   

   #NFa simple to dfa
   transhelp=[]
   for start in cerraduradeltaEpsilon:
     if start[2]==initial_state:
        transhelp.append((start[2],start[1],start[0]))

   
   for test in transhelp:
    ing=True
    estado=""
    for aux in transhelp:
      if test[2]==aux[2]:
        ing=False
    if ing==True:
      for trans in cerraduradeltaEpsilon:
        



   

   
   #print(states)
    
   for accepting in accepting_states:
     val=False
     for est in states:
       if accepting in est:
         val=True
         if est != accepting and val==True:
           accepting_states.append(est)   
   #print(accepting_states)

   #print(cerraduradeltaEpsilon)

  def expresionregular(self,expresion):
    val=True


        
      
      

   
   

 

  



