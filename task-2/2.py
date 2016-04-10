import networkx as nx
import matplotlib.pyplot as plt



def DFS(start_list,number_of_nodes,nodege_dict,vizited_nodes=set(),n=1):
    if len(vizited_nodes)==number_of_nodes or len(start_list)==0:
        pass
    else:
        
        vizited=set()
        new_start_list=[]          
        k=1
        for i in range(len(start_list)):
            for j in range(len(nodege_dict[start_list[i]])):
                if nodege_dict[start_list[i]][j] not in vizited_nodes and nodege_dict[start_list[i]][j] not in vizited and all(nodege_dict[start_list[i]][j]!=start_list[o] for o in range(len(start_list))) and all(nodege_dict[start_list[i]][j]!=new_start_list[o] for o in range(len(new_start_list))):
                    new_start_list.append(nodege_dict[start_list[i]][j])
                    edge_list.append((start_list[i],nodege_dict[start_list[i]][j]))
            pos[start_list[i]]=[k*1000/(len(start_list)+1),10000-n*100]
            vizited.add(start_list[i])
            k+=1
        DFS(new_start_list,number_of_nodes,nodege_dict,vizited_nodes=vizited.union(vizited_nodes),n=n+1)
    
        


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
DFS([hey],len(node_list),nodege_dict)


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
    
    

