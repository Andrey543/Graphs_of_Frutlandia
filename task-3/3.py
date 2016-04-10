import networkx as nx
import matplotlib.pyplot as plt
import random as rand



def BFS(start_node,nodege_dict,n=1):
    vizited_nodes.add(start_node)
    pos[start_node]=[rand.randint(0,1000),10000-n*100]
    if len(nodege_dict[start_node])==0:
        pass
    else:
        for i in range(len(nodege_dict[start_node])):
            if nodege_dict[start_node][i]not in vizited_nodes:
                edge_list.append((start_node,nodege_dict[start_node][i]))
                BFS(nodege_dict[start_node][i],nodege_dict,n=n+1)
    pos[start_node]=[rand.randint(0,1000),10000-n*500]          
  
        

data=open('data.txt','r')

g=nx.Graph()
data_vallue=data.readlines()
node_list=[]
edge_list=[]
nodege_dict={}
label_dict={}
pos={}
for i in range(len(data_vallue)):
    small_data=data_vallue[i].split()
    
    if not(small_data[0] in label_dict):
        label_dict[small_data[0]]=small_data[0]
    if not(small_data[1] in label_dict):
        label_dict[small_data[1]]=small_data[1]
    if small_data[0] in nodege_dict:
        nodege_dict[small_data[0]].append(small_data[1])
    else:
        nodege_dict[small_data[0]]=[small_data[1]]
    if small_data[1] in nodege_dict:
        nodege_dict[small_data[1]].append(small_data[0])
    else:
        nodege_dict[small_data[1]]=[small_data[0]]
    if all(node_list[j]!=small_data[0] for j in range(len(node_list))):
        node_list.append(small_data[0])
    if all(node_list[j]!=small_data[1] for j in range(len(node_list))):
        node_list.append(small_data[1])
print(' '.join(node_list))
hey=input('Please, input the first node\n')
vizited_nodes=set()
BFS(hey,nodege_dict)


nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list,
                       node_color='g',
                       node_size=500,
                       alpha=0.7)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,
                       width=2,edge_color='g',style='solid',
                       alpha=0.7)
nx.draw_networkx_labels(g,pos,font_size=10,labels=label_dict,font_color='black')


    
    
plt.axis('off')
plt.savefig("g.png")
plt.show() 
    
