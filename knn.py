def KNNClassifier(n,p,k=3): 
    
    ApartDistance=[] 
    for label in n: 
        for clas in n[label]: 
  
             
            Neighbour_distance = ((clas[0]-p[0])**2 +(clas[1]-p[1])**2+(clas[2]-p[2])**2)**0.5       #sqrtApply
  
             
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
  
    #return 0 if freq1>freq2 else 1
    if(freq1>freq2 and freq1>freq3):
      return 0
    elif(freq2>freq1 and freq2>freq3):
      return 1
    elif(freq3>freq1 and freq3>freq2):
      return 2

n = {0:[(1.70,65,20),(1.73,74,24),(1.75,69,25)], 
              1:[(1.90,85,33),(1.78,76,31),(1.81,75,35)],
              2:[(1.73,70,75),(1.80,71,63)]
             } 
  
    # testing point p(x,y) 
    p = (1.90,85,33) 
  
    # Number of neighbours  
    k = 3
  
    print("The value classified to unknown point is: {}",KNNClassifier(n,p,k))
    
 
