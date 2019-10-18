from operator import itemgetter

def getMaxValue(wt, val, capacity): 
          
        """function to get maximum value """
        iVal = [] 
        for i in range(len(wt)): 
            cost=val[i] // wt[i]
            tmp=wt[i], val[i], i, cost
            iVal.append(tmp) 
  
         
        iVal.sort(key=itemgetter(3),reverse = True) 
        
  
        totalValue = 0
        for i in iVal: 
            curWt = int(i[0]) 
            curVal = int(i[1]) 
            print(curWt)
            print(curVal)
            if capacity - curWt >= 0: 
                capacity -= curWt 
                totalValue += curVal 
            else: 
                fraction = capacity / curWt 
                totalValue += curVal * fraction  
                break
        return totalValue 
  

wt = [10, 40, 20, 30] 
val = [60, 40, 100, 120] 
capacity = 50
  
maxValue = getMaxValue(wt, val, capacity) 
print("Maximum value in Knapsack =", maxValue)
