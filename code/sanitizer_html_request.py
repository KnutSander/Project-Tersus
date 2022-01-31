#Example code for sanitizer in python

import requests

#Server Address:
ip = 'localhost:8000' 

#Placeholder Values:
SanID = 8
EmpID = 5
Time = 6
Dur = 7

#Send POST
dat = {'SanitizerID': SanID, 'EmployeeID': EmpID, 'Time': Time, 'Duration': Dur}
x = requests.post('http://' + ip + '/add/', data = dat)

#Verification
if x.text == 'Success':
    print('It worked')
else:
    print("It didn't work. Maybe send try to send another request, or turn the light red or something")
