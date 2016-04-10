import networkx as nx
import matplotlib.pyplot as plt



data=open('data.txt','r')

g=nx.Graph()
data_vallue=data.readlines()
node_list=[]
node_list_orange=[]
edge_list=[]
edge_list_orange=[]
label_list={}
for i in range(len(data_vallue)):
    data_small=data_vallue[i].split()
    g.add_edge(data_small[0],data_small[1],weight=int(data_small[2]))
    if all(node_list[i]!=data_small[0] for i in range(len(node_list))):
        if data_small[0]=='Mandarin' or data_small[1]=='Mandarin':
            node_list_orange.append(data_small[0])
        else:
            node_list.append(data_small[0])
        label_list[data_small[0]]=data_small[0]
    if all(node_list[i]!=data_small[1] for i in range(len(node_list))):
        if data_small[0]=='Mandarin' or data_small[1]=='Mandarin':
            node_list_orange.append(data_small[1])
        else:
            node_list.append(data_small[1])
        label_list[data_small[1]]=data_small[1]
    if data_small[0]=='Mandarin' or data_small[1]=='Mandarin':
        edge_list_orange.append((data_small[0],data_small[1]))
    else:
        edge_list.append((data_small[0],data_small[1]))


print(node_list)

    
    
    
pos=nx.spring_layout(g,k=0.8)




nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list,
                       node_color='b',
                       node_size=500,alpha=0.5)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,alpha=0.2,
                       width=2,edge_color='b',style='solid')
                       
                       
nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list_orange,
                       node_color='g',
                       node_size=500)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list_orange,
                       width=2,edge_color='g',style='solid')
                       
nx.draw_networkx_nodes(g,pos,
                       nodelist=['Orange'],
                       node_color='black',
                       node_size=500)



nx.draw_networkx_labels(g,pos=pos,font_size=10,labels=label_list,font_color='white')


plt.axis('off')
plt.savefig("g.png")
plt.show() 

