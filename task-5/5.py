import networkx as nx
import matplotlib.pyplot as plt




    

def Dek(node):
    node_dict.remove(node)
    if len(node_dict)==0:
        pass
    else:
        for i in range(len(graf_dict[node])):
            if graf_dict[node][i]['node'] not in node_result or node_result[graf_dict[node][i]['node']]>(graf_dict[node][i]['weight']+node_result[node]):
                node_result[graf_dict[node][i]['node']]=graf_dict[node][i]['weight']+node_result[node]
        min=None
        for i in node_dict:
            if i in node_result and (min==None or node_result[i]<min):
                min=node_result[i]
                key=i
        Dek(key)
            
                
            
            
    
    
  
data=open('data.txt','r')


data_vallue=data.readlines()
graf_dict={}
node_dict=set()
node_result={}
for i in range(len(data_vallue)):
    data_small=data_vallue[i].split()
    if data_small[0] not in graf_dict:
        graf_dict[data_small[0]]=[]
    graf_dict[data_small[0]].append({'node':data_small[1],'weight':int(data_small[2])})
    if data_small[1] not in graf_dict:
        graf_dict[data_small[1]]=[]
    graf_dict[data_small[1]].append({'node':data_small[0],'weight':int(data_small[2])})
    if data_small[0] not in node_dict:
        node_dict.add(data_small[0])
    if data_small[1] not in node_dict:
        node_dict.add(data_small[1])

print(node_dict)
first_node=input('Please, iunput name of node\n')
node_result[first_node]=0
Dek(first_node)

for i in node_result:
    print('Shortest way from node "',first_node,'" to node "',i,'": ',node_result[i],sep='')

            
    
    
