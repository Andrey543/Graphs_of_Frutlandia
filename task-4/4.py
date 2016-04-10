import networkx as nx
import matplotlib.pyplot as plt
import random as rand




    

def BFS(start_node,node_list,edge_list):
    node_dict.discard(start_node)
    node_list.append(start_node)
    if len(nodege_dict[start_node])==0:
        pass
    else:      
        for i in range(len(nodege_dict[start_node])):
            edge_list.append((start_node,nodege_dict[start_node][i]))
            if nodege_dict[start_node][i] in node_dict:                
                BFS(nodege_dict[start_node][i],node_list,edge_list)
            


    
hey=input('Please, input name of data file (data1.txt, data2.txt,data3.txt,data4.txt)\n')   
data=open(hey,'r')

g=nx.Graph()
data_vallue=data.readlines()
node_list=[]
edge_list=[]
node_dict=set()
nodege_dict={}
label_dict={}

for i in range(len(data_vallue)):
    small_data=data_vallue[i].split()
    g.add_edge(small_data[0],small_data[1],weight=int(small_data[2]))    
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
    if small_data[0] not in node_dict:
        node_dict.add(small_data[0])
    if small_data[1] not in node_dict:
        node_dict.add(small_data[1])
    edge_list.append((small_data[0],small_data[1]))
    

pos=nx.spring_layout(g,k=0.8)
k=0
while len(node_dict)>0:

    k+=1
    node_list=[]
    edge_list=[]
    BFS(node_dict.pop(),node_list,edge_list)
    color=rand.choice(['grey','blue','green','red','orange','pink'])
    nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list,
                       node_color=color,
                       node_size=500,
                       alpha=0.7)
                   
    nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,
                       width=2,edge_color=color,style='solid',
                       alpha=0.7)
                       
                       
nx.draw_networkx_labels(g,pos,font_size=10,labels=label_dict,font_color='black')


if k==1:
    print('Граф связен')
else:
    print('Граф не связен')
    
plt.axis('off')
plt.savefig("g.png")
plt.show() 




