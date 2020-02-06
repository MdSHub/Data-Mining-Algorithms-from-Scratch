n = {0:[(8,5),(7,3)], 
              1:[(3,7)],
              2:[(3,6)]
             } 
  
    # testing point p(x,y)
p = (3,4) 
  
    # Number of neighbours  
k = 3
  


def KNNClassifier(n,p,k=3): 
    
    ApartDistance=[] 
    for label in n: 
        for clas in n[label]: 
  
             
            Neighbour_distance = ((clas[0]-p[0])**2 +(clas[1]-p[1]))**0.5       #sqrtApply
  
             
            ApartDistance.append((Neighbour_distance,label)) 
  
    print(ApartDistance)
    distance = sorted(ApartDistance)[:k]   #sortApply
    print(distance)
  
    freq1 = 0  
    freq2 = 0  
    freq3 = 0 
  
    for d in distance: 
        if d[1] == 0: 
            freq1 += 1
        elif d[1] == 1: 
            freq2 += 1
        elif d[1] == 2:
            freq3 += 1
  
    
    if(freq1>freq2 and freq1>freq3):
      return 0
    elif(freq2>freq1 and freq2>freq3):
      return 1
    elif(freq3>freq1 and freq3>freq2):
      return 2




a=KNNClassifier(n,p,k)

