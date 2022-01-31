# On system setup  
Would be set by the system administrator whenever the system is initialised
```python
maximumPointsPerDay = givenvalue  
cooldownTimerLength = givenLength  
```
# On user interaction  
Sanitizing station sends information to webserver.  
Webserver saves information like normal.  
```python
if(employee.cooldownTimer >= time.Now AND employee.pointsToday < maximumPointsPerDay)  
    employee.pointsToday++  
    employee.cooldownTimer = time.Now + cooldownTimerLength  
```
The timer needs to be saved in the database, together with the points.  
Should make a seperate table that is linked to the user with the timer and points.  

# Reset code  
Likely runs at midnight.  
```python
for(Employee e : employees)  
    employee.pointsToday = 0  
    employee.cooldownTimer = time.Now  
```
# Saving scores for longer periods  
The scores need to be saved for longer periods than a day.  
Depending on how long the company wants it to be saved.  
A weekly score that resets at midnight every Sunday.  
A montly score that resets at midnight the last day of the month.  
Saved in either the employee table, or in a seprate table.  
The achivements table in the newest database design is a good option.  