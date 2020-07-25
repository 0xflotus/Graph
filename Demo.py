

###################################################################################################
#                                                                                                 #    
#     ways of passing arguments                                                                   #    
#     1. by list                                                                                  #        
#        x=[1,2,3,4,5]                                                                            #            
#        y=[1,2,3,3,3]                                                                            #        
#        generate_graph(x,y)                                                                      #    
#                                                                                                 #
#     2. by tuples  [ (x1,y1) , (x2,y2) , (x3,y3) .... , (x10,y10)]                               #
#      data=[(1,1),(2,2),(3,3),(4,3),(5,3)]             this will generate graph as same as above #
#      generate_graph(*data)                                                                      #
#                                                                                                 #
#                                                                                                 #
###################################################################################################

from graph import generate_graph


# FOR FUN  =>> uncomment below and RUN.
#smile=[(1, 4),(1, 6),(2, 4),(2, 6),(3, 4),(3, 6),(1, 5),(3, 5),(6, 4),(6, 6),(7, 4),(7, 6),(8, 4),(8, 6),(6, 5),(8, 5),(2,2),(3,1),(4,1),(5,1),(6,1),(7,2)]
#generate_graph(*smile)

x=[1,2,3,4,5,6,7]    
y=[1,2,3,4,3,2,1]    
generate_graph(x,y)    
