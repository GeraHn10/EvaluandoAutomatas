from Automatas import Automatas
import networkx as nx
import matplotlib.pyplot as plt


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

   
   def imprimir(self, estados, transiciones):
        que = nx.DiGraph()

        for arre in estados:
            que.add_node(arre)
        for t in transiciones:
            que.add_edge(t[2], t[0])

        #pos = nx.spring_layout(que)
        #plt.figure()
        # nx.draw(que, \
        # node_size=500,node_color='pink',alpha=0.9,\
        # labels={node:node for node in que.nodes()})
        # nx.draw_networkx_labels(que, edges_labels={}, with_labels = True)
        # plt.axis('off')

        nx.draw(que, with_labels = True)
        plt.show()
      