# Database
## Consecutive Washes
Priority: Medium
The same wash can be registered in the database twice in a row if the hand sanitizer sends two washes from the same person and same station one after another. 
This can cause abnormal graphs that can confuse the user.
Solutions:
 - Hand Sanitizer Check: The server would need another url to update a wash. The Raspberry Pi can check if the employee ID has been scanned recently. If so, the update script can be called which increases duration without adding another row.
 - Server Check: When adding a new scan to the Database, check the last scan and compare IDs. If the IDs are the same, only update the duration with the new value. 
## Secure Add
Priority: Low
Anyone can send a HTML request to add a wash to the database. 
People could use this to fabricate washing information or even make the system think stations are empty.
Solution:
 - Set up a private key only distributed to the stations and checking the key is valid on the server.
## Backups
Priority: High
All the information in the databases can be wiped or lost if anything were to happen to the server.
Solution:
 - A backup of the database should be uploaded to a secure location periodically so that it can be restored into the live version if necessary.

# Website
## Useless Button
Priority: Very Low
There is a home button on the home page that refreshes the page for no reason.
Solution:
 - Remove the button.
## Mobile
Priority: High
Most people may check their stats on a mobile screen, and while the website runs fine, some graphics are not ideal.
Issues:
 - The bar graph labels become distorted.
 - The no. of Hand Washes, avg. Duration, Employees and Empty Stations labels are massive.
 - Danger
## Website Security
Priority: Low
Website is unencrypted so can be intercepted and seen by a hacker easily.
Solution:
 - Get SSL certificate to be https.
## Duration Units
Priority: Low
Avg. Duration label has no units.
Soltuion:
 - Add mins.
## Wrong URL Page
Priority: Low
GOing to the wrong URL shows a django error page.
Solution:
 - Create a custom error page that shows an errror code that we have documentation for.
## Employee Activity Page
Priority: High
 - Wrong data.

# Hand Sanitizer
Since the actual model has not been built, this is just guessing issues we may have.
## RFID range
When using the hand sanitizer, the wristband can be up to 10cm away from the scanner.
## Wifi Credentials Change
If the WiFi password or username changes, we may want an easier method of changing it without having to open each sanitizer up.