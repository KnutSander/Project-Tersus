# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 14:49:26 2020

@author: ArifM
"""
##This code doesnt work as it has to be implemented into the CLustered method
print(centroids)
print(labels)


colours = ["g.","r.","y."]

for i in range(len(X)):
    print("Coordinate :" ,X[i], " Label: ", labels[i])
    plt.plot(X[i][0], X[i][1], colours[labels[i]], markersize = 10)
    
PieValue = [0,0,0]
PieLabel = ["High","Medium","Low"]
#Information For Danger Donut metric
    
for i in range(len(labels)):
    if(labels[i] == 0):
        PieValue[0]+=1
    elif(labels[i] == 1):
        PieValue[1]+=1
    elif(labels[i] == 2):
        PieValue[2]+=1
        
        
plt.scatter(centroids[:,0],centroids[:,1], marker = "X", s=150,linewidths = 5,zorder = 10)
plt.show()


PieColors = ['r','g','y']




fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(aspect="equal"))
wedges, texts = ax.pie(PieValue, wedgeprops=dict(width=0.3), startangle=-40,colors=PieColors )
ax.legend(["High","Low","Medium"])
ax.set_title("Danger Donut, Sanitizing compliance")

plt.show()



department = []
for i in range(len(InputData)):
    department.append(random.randint(1,3))
    
InputData['Cluster'] = labels

InputData['Department'] = department

DepartmentData = InputData[['Department','Cluster']]

d1 = DepartmentData[DepartmentData['Department'] == 1]
d2 = DepartmentData[DepartmentData['Department'] == 2]
d3 = DepartmentData[DepartmentData['Department'] == 3]

Low = [d1[d1['Cluster'] == 1]['Cluster'].count(),d2[d2['Cluster'] == 1]['Cluster'].count(),d3[d3['Cluster'] == 1]['Cluster'].count()]
Medium = [d1[d1['Cluster'] == 2]['Cluster'].count(),d2[d2['Cluster'] == 2]['Cluster'].count(),d3[d3['Cluster'] == 2]['Cluster'].count()]
High = [d1[d1['Cluster'] == 0]['Cluster'].count(),d2[d2['Cluster'] == 0]['Cluster'].count(),d3[d3['Cluster'] == 0]['Cluster'].count()]

N = 3
ind = np.arange(N)
container1 = plt.bar(ind,Low,0.3)
container2 = plt.bar(ind,Medium,0.3,bottom=Low)
container3 = plt.bar(ind,High,0.3,bottom=Medium)

plt.style.use('ggplot')
plt.ylabel("Number of Employees")
plt.xticks(ind,("Sales","HR","Tech"))
plt.yticks(np.arange(0,20))
plt.legend((container1[0],container2[1],container3[2]),("Low","Medium","High"))


#container2 = plt.bar()

plt.show()
