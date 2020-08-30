from Automatas import Automatas



class Evaluadores():
   
   def dfa_evaluate(self,alphabet, states, initial_state, accepting_states, transitions, str_test):
       current_state = initial_state
       valid=True
       for char_index in range(len(str_test)):

        
         current_char = str_test[char_index]
         next_state = self.returnNextState(transitions,current_state,current_char)
         print (current_state, current_char, next_state)
         current_state = next_state

         if(current_state==-1):
            valid=False
            break
         
         
       if valid==True:   
         if current_state in accepting_states:
           print ("Pertenece a L(M)")
         else: 
            print ("No pertenece a L(M)")
       else:
               print ("No pertenece a L(M)")


   def returnNextState(self,transitions,initial_state,source): 
    for trans in transitions:
       if(trans[0]==initial_state and trans[1]==source):
          return trans[2]
       
    return -1 

   

      