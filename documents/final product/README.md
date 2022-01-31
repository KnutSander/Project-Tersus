# CE299 - Team 5 - Smart Hand Sanitisation Solution
![logo](/documents/images/branding/png/logo.png)

## How to Run
These are instructions to view the website on our own server.  
Visit the URL: http://165.232.106.34/user/login.   
Use the credentials below to view the website as an admin or normal user.  

|              |  Normal User |Admin|
|--------------|--------------|-|
| **Username** |  RThon | dev |
| **Password** |mynameisrachel|  team5!webserver1  |  

As an admin, you are given two main pages to visit, the User Management system and the Statistics Dashboard.  
Normal users are taken their statistics page where they can view their hand wash information. 

## How to Compile
### Compiling to http://165.232.106.34/
1. SSH into the server using the dev user with password team5!webserver1.
> ssh dev@165.232.106.34
> team5!webserver1
2. Navigate to the project directory.
> cd ce299_team05
3. Execute a git pull.
> git pull

### Compiling to Custom/Local Server
All commands should be run on the server hosting the website. Remember to navigate to the directory containing the files mentioned in each step.
1.	Install pip and create a virtual environment for the code to run in an isolated environment.
2.	Obtain the source code with git pull, clone or fork depending on whether you would like to make local changes or keep it updated. 
3.	Once you have the files on the server, install the libraries for use in  Django-webapp/CE299/requirements.txt.
> pip install -r requirements.txt
4.	Create an SQL database and cutomise the settings in Django-webapp/CE299/CE299/settings.py. Database settings begin line 88.
5.	Then, run migrations to create the tables in the SQL database defined in step 4. 
> python manage.py migrate 
6.  Now run the server.
> python manage.py runserver  
7.  Create an admin account. The command line will prompt you for a username and password. Keep note of what you enter.
> python manage.py createsuperuser
8.	The website should be running on the server, log in with the admin account you created by visiting the URL and start adding users.
9.	Everything should be fully operational at this point, so you can run the hardware simulation to give the website data to display.

## How to Test
Link testing documents.

## Known Issues
Without being able to meet on campus and use University resources, we weren't able to develop a substantial hardware component in the project as we had expected. To circumvent this, we developed a hardware simulation that can be ran on any computer and we also planned the design and specifications of the hardware as though we were actually building it.
