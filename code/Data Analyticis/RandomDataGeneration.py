import pandas as pd
import random as rand


time =[]
day = []
month = []
year = []
ID =[]
Quantity = []
Machine_ID = []


#May need to improve this method to provide a normally distributed 
#data, 

#The reason for 3 for loops is for adding in varied data, the range values are different for specific simulated
#'bad handwashers' and 'compliant' hand washers.


for i in range(400):
    time.append(rand.randrange(1,25,1))
    day.append(rand.randrange(1,31,1))
    month.append(rand.randrange(1,13,1))
    year.append(2020)
    ID.append(rand.randrange(1,60,1))
    Quantity.append(rand.randrange(1,4))
    Machine_ID.append(rand.randrange(1,5,1))
    
    

for i in range(400):
    time.append(rand.randrange(1,25,1))
    day.append(rand.randrange(1,31,1))
    month.append(rand.randrange(1,13,1))
    year.append(2020)
    ID.append(rand.randrange(1,20,1))
    Quantity.append(rand.randrange(1,4))
    Machine_ID.append(rand.randrange(1,5,1))
    

for i in range(400):
    time.append(rand.randrange(1,25,1))
    day.append(rand.randrange(1,31,1))
    month.append(rand.randrange(1,2,1))
    year.append(2020)
    ID.append(rand.randrange(1,31,1))
    Quantity.append(rand.randrange(1,4))
    Machine_ID.append(rand.randrange(1,5,1))
    
for i in range(400):
    time.append(rand.randrange(1,25,1))
    day.append(rand.randrange(1,31,1))
    month.append(rand.randrange(1,2,1))
    year.append(2020)
    ID.append(rand.randrange(28,60,1))
    Quantity.append(rand.randrange(1,4))
    Machine_ID.append(rand.randrange(1,5,1))
    
        
    
    


Generated_data = pd.DataFrame(data = {'EmployeeID':ID,
                               'TW':time,
                               'DW':day,
                               'MW':month,
                               'YW':year,
                               'Quantity':Quantity,
                               'MachineID':Machine_ID})

Generated_data.to_csv('GeneratedData.csv',index=False)
