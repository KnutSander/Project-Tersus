# Further Gamification
The current implimentation of the gamification is lacking any purpose.  
What currently happens is:
* When an employee washes their hands
    * If it's been x amount of time since they last washed their hands
    * And they have a score of y or less
    * They gain a point.

This is rather a simple system, and currently the points aren't used for anything.

## Gamification Idea 1.1
In the database design, there is a table called goal. This is linked with the department table, which in turn is linked with the achievement and employee tables. The goal table is currently unused.  
The idea is to have the individual departments set a goal, as in an average amount of hand washes/points.  
Needs to be an average, because the different departments will have a difference in employees.  
Display the individual users points together with the users stats on the planed user page.  

### Future ideas
Possibly implement a company wide goal as well?  
Still need somethinge more to use the points on, as it now basically represents number of hand washes, just with a cool down.  
The points could be a long term way of storing washes. So the RFIDConnection table would be reset every day, because it would quickly be filled with a lot of data, especially for bigger companies. 
Another idea for further development is to have more than just a number as the goal, specifying also the duration.
