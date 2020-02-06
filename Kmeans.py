import random
import matplotlib.pyplot as plt

"""##"""

data=[1,2,3,4,5,11,12,13,14,25]
y=[0,0,0,0,0,0,0,0,0,0]
len(data),len(y)

for ix in range(len(data)):
    plt.scatter(data[ix],y[ix])

def distance(x1,x2):
    return abs(x2-x1)

def mean(l):
    m_list=[]
    for ix in range(len(l)):
        k=l[ix]
        if len(k)==0:
            m_list.append(0)
            continue
        m_list.append(sum(k)/len(k))
    return m_list

for ix in range(len(data)):
    plt.scatter(data[ix],y[ix])

def main_func_gen(data,k):
    k_list=[]
    while(len(k_list)!=k):
        clust=random.randint(0,200)
        if not clust in k_list:
            k_list.append(clust)
    print('Cluster Centers Randomly Initialized at {}'.format(k_list))
    
    

    m_list=[]
    for m in range(len(k_list)):
        m_list.append(-1.1)
    
    cnt=0
    
    while True:
        cnt+=1
        clusters=[]
        for ix in range(len(k_list)):
            clusters.append([])
            
        for x2 in data:
            dist=[]
            for kp in k_list:
                dist.append(distance(kp,x2))
                
            min_arg=get_argmin(dist)
            clusters[min_arg].append(x2)
        
    
        m_list=mean(clusters)    

        
        if k_list==m_list:
            print('Final Centers found at Iter. {}  {}'.format(cnt,k_list)) 
            return k_list,clusters
        
        print('Cluster Centers at Iter. {}  {}'.format(cnt,k_list))   
        k_list=m_list
        
        
    return k_list

def get_argmin(l):
    m=min(l)
    for ix in range(len(l)):
        if l[ix]==m:
            return ix

k_list,clusters=main_func_gen(data,2)

for ix in range(len(data)):
    plt.scatter(data[ix],y[ix])
for ix in range(len(k_list)):
    plt.scatter(k_list[ix],0,marker='*',s=500)

print(clusters)
