import pandas as pd
from matplotlib import pyplot as plt
from matplotlib import style

style.use("ggplot")

#https://www.youtube.com/watch?v=7XhDsbZyYoQ

#https://colab.research.google.com/drive/1f3c9JuQh2Nd1MD-c1GEa9LbNO2ij2VCl#scrollTo=jUhOUShsic_t


sample_data = pd.read_csv("GeneratedData.csv") 
#Reads generated files from csv into dataframe


EmployeeWashCount = sample_data.groupby('EmployeeID').size().reset_index(name='count')




plt.scatter(EmployeeWashCount['EmployeeID'],EmployeeWashCount['count'])
plt.title("Hands Washed Scatter Data for 2020 Feburary")
plt.xlabel("EmployeeIDs")
plt.ylabel("Washing Count")
plt.show()

#Need to count how many times EmployeeID shows up specifically for EmployeeID

plt.bar(EmployeeWashCount['EmployeeID'],EmployeeWashCount['count'])
plt.title("Total Count Hand sanitized")
plt.show()


EmployeeWashCount.to_csv('out.csv',index=False)
    
