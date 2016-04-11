import networkx as nx
import matplotlib.pyplot as plt
import random as rand



flag=False
def short(node,second_node,flag=flag):     
    if second_node not in node_dict:
        flag=True
    if flag:
        pass
    node_dict.remove(node)
    if len(node_dict)==0:
        pass
    else:
        for i in range(len(graf_dict[node])):
            print(node_result)
            print(node)
            print(graf_dict[node][i]['node'] not in node_result)
            if graf_dict[node][i]['node'] not in node_result or node_result[graf_dict[node][i]['node']][0]>(graf_dict[node][i]['weight']+node_result[node][0]):
                node_result[graf_dict[node][i]['node']]=[graf_dict[node][i]['weight']+node_result[node][0],node_result[node][1]+' '+graf_dict[node][i]['node']]
        min=None
        for i in node_dict:
            if i in node_result and (min==None or node_result[i][0]<min):
                min=node_result[i][0]
                key=i
        short(key,second_node,flag)



data=open('data.txt','r')

g=nx.Graph()
data_vallue=data.readlines()
graf_dict={}
node_dict=set()
node_result={}
node_list=[]
edge_list=[]
label_dict={}
for i in range(len(data_vallue)):
    small_data=data_vallue[i].split()
    g.add_edge(small_data[0],small_data[1],weight=int(small_data[2]))    
    if not(small_data[0] in label_dict):
        label_dict[small_data[0]]=small_data[0]
    if not(small_data[1] in label_dict):
        label_dict[small_data[1]]=small_data[1]
    if small_data[0] not in graf_dict:
        graf_dict[small_data[0]]=[]
    graf_dict[small_data[0]].append({'node':small_data[1],'weight':int(small_data[2])})
    if small_data[1] not in graf_dict:
        graf_dict[small_data[1]]=[]
    graf_dict[small_data[1]].append({'node':small_data[0],'weight':int(small_data[2])})
    if small_data[0] not in node_dict:
        node_dict.add(small_data[0])
    if small_data[1] not in node_dict:
        node_dict.add(small_data[1])
    if small_data[0] not in node_dict:
        node_dict.add(small_data[0])
    if small_data[1] not in node_dict:
        node_dict.add(small_data[1])
    edge_list.append((small_data[0],small_data[1]))

print(node_dict,'\n\n\n',graf_dict)
first_node=input('Please, iunput name of first node\n')
second_node=input('Please, iunput name of second node\n')
node_result[first_node]=[0,first_node]
short(first_node,second_node)
essens=node_result[second_node][1].split()
node_list_way=essens
edge_list_way=[]
for i in range(len(essens)-1):
    edge_list_way.append((essens[i],essens[i+1]))

pos=nx.spring_layout(g,k=0.8)
color=rand.choice(['grey','blue','green','red','orange'])
color1=rand.choice(['grey','blue','green','red','orange'])

nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list,
                       node_color='blue',
                       node_size=500,
                       alpha=0.7)
                   
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list,
                       width=2,edge_color=color,style='solid',
                       alpha=0.7)
                       
nx.draw_networkx_nodes(g,pos,
                       nodelist=node_list_way,
                       node_color=color1,
                       node_size=500,
                       alpha=1)
                       
nx.draw_networkx_edges(g,pos,
                       edgelist=edge_list_way,
                       width=5,edge_color=color1,style='solid',
                       alpha=1)
nx.draw_networkx_labels(g,pos,font_size=10,labels=label_dict,font_color='black')




plt.axis('off')
plt.savefig("g.png")
plt.show() 

    






