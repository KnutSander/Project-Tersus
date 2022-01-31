# Test report  

## Initial Ideas
Throughout the development of *Project Tersus*, programs were tested locally on personal computers before being uploaded to the webserver.  
In instances where the code didn't work on the webserver, these issues were solved in a timely fashion.  
However, as testing is never fully completed, this report documents further efforts made in testing.

As manual testing has been performed throughout the development process, the main focus of this report will be automatic testing and can be found in the relevant section below. 
Python and Django present many options and methods for automatic testing, a list of those which were used can be found in the automatic testing section.

## Testing performed

## Manual Testing
#### Test 1: Trying to Access Administration without Authorization to do so.
- Test Details
	- Attempt to log in to the Administration  with an incorrect login. ie. User doesn't exist or is not an administrative account.
	- Pass: If an unauthorized user is unable to gain access.
	- Fail: If an unauthorized user is able to gain access.
	- Parameters Tested: 
		- User exists but is not an admin. 
			- [PASS](testImg/test1a.png)
			- User is prompted to login with correct authority
		- User does not exist. 
			- [PASS](testImg/test1b.png)
			- User is prompted to login with correct authority
			- Note: No Logout exists on this page, and performing this and following tests immediately after the last one shows previously logged in user instead.
		- User is an admin, but doesn't use the correct password. 
			- [PASS](testImg/test1c.png)
			- User is prompted to login with correct authority
		- Random Input. 
			- [PASS](testImg/test1d.png)
			- User is prompted to login with correct authority
		- Accessing the correct version of the Dashboard. 
			- [FAIL](testImg/test1e.png)
			- User can access view of the Dashboard only intended for admins.
			- Note: Logging in as an end user but have access to the admin view of the dashboard upon loading the website. Cannot access or alter the database, but access to cleaning statistics of other individuals.
			Clicking on Analytics takes her to the page end users are supposed to be in. 
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-243)
			- STATUS: Fixed as of 03/03/2021.

#### Test 2: Testing URLS
- Test Details
	- Attempt to access the website without logins, just with knowledge of the URLs.
	- Pass: If forced to Login, and unable to gain access.
	- Fail: If user can gain any kind of access.
	- Parameters Tested:
		- Accessing the statistics dashboard without logging in, just typing the URL (165.232.106.34:8000/admin/home)
			- FAIL
			- As in the last test of Test 1.
			- Note: User can access analytics and potentially senstive information of employees. Cannot access database.
			Clicking on Analytics page finally throws up a login prompt. Seems related to the last parameter tested in Test 1.
			Worth noting that this is the current default page on entering the URL 165.232.106.34:8000 - Definitely needs to be changed to the login
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-244)
			- STATUS: Fixed as of 04/03/2021.
		- Accessing the database management with just the URL (http://165.232.106.34:8000/admin/auth/user/) 
			- [PASS](testImg/test2a.png)
			- User is prompted to login.
		- Accessing random URL from within Database Management (ie http://165.232.106.34:8000/admin/CC/achievement/164/change/) 
			- PASS
			- User is prompted to login.
		- Entering the base URL (165.232.106.34)
			- FAIL (testImg/test2b.png)
			- Leads to an ubuntu default page, this really should be changed to the login page, and this should be accessed in a test page or something.
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-247)
			- STATUS: Fixed as of 04/03/2021.

#### Test 3: Illogical details in the database
- Test Details
	- Test what happens if there is erroneous data in the database, or being sent to it.
	- Pass: The Website & Database handles information correctly, issuing user-readable errors if needed.
	- Fail: Information causes the website/database to break.
	- Parameters Tested:
		- User with a name not in the database. (ie BBoss has no name in the database)
			- [FAIL](testImg/test3a.png)
			- User is presented with an error page that is not user-friendly.
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-245)
			- STATUS: Fixed as of 04/03/2021.
		- RFID connection with a User ID that doesn't exist. (ie. Modified Simulation to scan RFID num '88888888888888888888888888888')
			- PASS(?)
			- The code does not show an error but the database does not log the incorrect RFID tag or affect the website.
		- RFID connection with a Sanitizer ID that doesn't exist. (ie. Modified Simulation to say that the Scanner ID is '88888888888888888888888888888')
			- PASS
			- Code shows an error and informs that the sanitizer doesn't exist.
		- Date Logged For Usage is in the Future (ie RFID connection object 2969 changed to 1st Mar 2021, on 25th Feb 2021)
			- [FAIL](testImg/test3b.png)
			- Database management allows change, and is shown on the website.
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-246)
			- STATUS: Unchanged, deemed not a real issue.
 
 #### Test 4: Different Devices & Browsers
 - Test Details
	- Test what happens when using the website with different set-ups
	- Pass: The website functions and looks as intended.
	- Parameters Tested:
		- Google Chrome, Windows 10 & Mac
			- PASS
			- Website works as intended, correctly adapts to resolution changes.
		- Mozilla Firefox, Windows 10
			- PASS
			- Website works as intended, correctly adapts to resolution changes.
		- Microsoft Edge, Windows 10
			- PASS
			- Website works as intended, correctly adapts to resolution changes.
		- Apple Safari, Mac
			- PASS
			- Website works as intended, correctly adapts to resolution changes.
		- Mozilla Firefox, Android
			- [FAIL](testImg/test4a.png) (minor - aesthetic only)
			- Website works as intended, however logo is cut off in vertical mode on login screen.
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-248)
			-STATUS: Unchanged.
		- Google Chrome, Android
			- [FAIL](testImg/test4b.png) (minor - aesthetic only)
			- Website works as intended, however logo is cut off in vertical mode on login screen.
			- [Jira Bug](https://cseejira.essex.ac.uk/browse/A299109-248)
			-STATUS: Unchanged.

#### Test 5: Misc
- Test Details
	- Running the simulation.
	- Pass: Everything seems to work as intended
	- Fail: Something doesn't work.
		- FAIL
		- Refilling Sanitizers function doesn't seem to work. Code output reports that it's ok, but database doesn't update. Thus caught in endless loop where every sanitizer is constantly reporting that its refilling.
		

## Automatic Testing:
Django's own test package is used to automatically test the code; to visualize these results in a clear and pleasing way. the Python package Coverage was utilised.  
The goal with the automatic tests is to get at least 85% coverage on all files, and at least 90% coverage overall.

### Django Testing Tools
Django provides its own testing package, made specifically for automatic testing. By creating TestCase classes, the test knows what code to run when the 'test' command is given.  
The testing creates a copy of the Django project's database, but doesn't copy over any of the data, to give the tester the option of testing with custom data.  
To load data into the database, "fixtures" are used, which are files that store data from a database in text form.  
The data in the current database can be extracted to a fixture by using the command "*manage.py dumpdata". This can the be loaded into the test database by including it at the start of the code in the test files.  
[Django Testing Tools](https://docs.djangoproject.com/en/3.1/topics/testing/tools/#django.test.TestCase)

### Coverage
Coverage is a tool for measuring code coverage of any Python program.  
It provides an overview of how much of the code in a .py file is executed and can even give an in-depth look at which lines run and which lines don't.  
Using it together with Django's own testing package gives an overview of what lines are covered by the testing and gives insight as to what lines aren't tested and need tests written for them.  
[Coverage Webpage](https://coverage.readthedocs.io/en/latest/)

### Testing
#### Initial Report
To test the code the following command is used: "*coverage run --omit='venv\' manage.py test CC -v 2*".  
- "*coverage run*" is used to make Coverage to gather data from the test.  
- "*--omit='venv\'*" is used to exclude the 'venv\*' folder from the testing and the coverage report.  
- "*manage.py test*" is used to run the Django tests.  
- "*CC*" is used to include all files and folder in the testing. 
- "*-v 2*" is used to increase the verbosity, to include more detail in the report.  

After running the initial command, a report can be shown by running "*coverage report*", which gives the following information:  
![Coverage Report](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_report.PNG "Coverage Report")  
*Figure 1: Coverage Report.*  

The report gives an overview of the amount of statements in each file: the amount of lines that weren't run, and the percentage of code that was covered by running the test.  
An even more in-depth report, which can be view in any web browser, can be created by running the command "*coverage html*" an interactive html version of the report is created, as well as html pages for every .py file. In the newly created "htmlcov/" folder you can access the report by opening the "index.html" file.  
![Coverage HTML Report](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_html_report.png "Coverage HTML")  
*Figure 2: Coverage Report for the project in HTML form.*  

This report is almost the exact same as the normal report, but the interactive aspect is what makes the html report so useful. Clicking any of the filenames leads to an html page with detailed information as to what lines in each file were executed and not, giving insight as to what lines require further testing and what lines tests are being skipped. Below are two examples of this, from models.py and from addConnection.py:  
![models.py](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_models.png "Coverage models.py")  
*Figure 3: Showing the results of a test, models.py.*  

Above is a fragment of the report for models,py, but it can be seen that the file had all its statements tested without the need for writing a test_*.py file.

![addConnection](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_addConnection.png "Coverage addConnection.py")  
*Figure 4: Showing the results of a test, addConnection.py.*  

Above is part of the report for addConnection.py, but here it is clearly shown that there is an excessive amount of lines that are not covered by the base "*test*" command. Examining the entire file, it is evident that the "*addRFIDConnection*" method is what needs to be tested.
This file, as well as any other file with lines that aren't covered, require specialized tests to cover their methods.

#### Writing Tests
Here is an example test file, written specifically for testing addConnection,py, asserting that it returns the correct values when given different requests. Some static methods were omitted from the picture below. They return different HTTPRequest objects with a "method" field and a field containing values that simulate an employee using a sanitizer station. The two fields vary to capture all the error checking in addConnection.py.  
![test_addConnection](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/test_addConnection.PNG "test_addConnection")  
*Figure 5: Code created specifically to test addConnection.py and the lines missed in the previous test.*

After running the full "*test*" command, and "*coverage html*" the new in "index.html" file looks like this.  
![Coverage HTML Report](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_html_report2.png "New Coverage HTML")  
*Figure 6: The results of the new test.*  

And looking at the addConnection.py report, it now shows that all lines have been tested.  
![New addConnection](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_addConnection2.png "New Coverage addConnection.py")  
*Figure 7: The results of the new test, specifically addConnection.py.*  

Here is another example of a test file, this one is made to test getSimulationData.py.  
![test_getSimulationData](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/test_getSimulationData.PNG "test_getSimulationData.py")  
*Figure 8: Code created specifically to test getSimulationData.py.*  

Not all files need to be tested as much as addConnection and getSimulationData. Here is the test file for table.py.  
![test_table](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/test_table.PNG "test_table.py")  
*Figure 9: Code created specifically to test table.py.*  

#### Final Report
After writing tests for all views, the final coverage report looks like this.  
![Final Coverage Report](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/coverage_final_report.png "Final Coverage Report")  
*Figure 10: Final Test Report.*  

All test files can be found at [this link](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/tree/master/Django-webapp/CE299/CC/testing/views)
