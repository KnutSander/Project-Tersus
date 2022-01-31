# Product Context

## Legal

### GDPR
The product's key features rely on the collection and use of personally identifiable information (PII) which means it has to comply with GDPR. PII is processed by Django and stored in a dedicated production database.

- In terms of data storage, the product integrates with each company's current infrastructure for storing PII. In fact, some PII such as the record of employees is taken directly from the company's current database. It is every company's responsibility to protect the production database in a GDPR secure way as they do with their other databases containing PII.

- In terms of data processing, the Django web application is stored on a secure server. All traffic on the final product is SSL encrypted. The dashboard of the website shows anonymized data which is not considered PII. Any PII is password protected and only accessible by logging in. Only employees of a company have access to an account for our product. Regular users only have access to their own PII whereas admin users have access to a more detailed set of information. 


The hand sanitizer stations themselves don't store any PII however they do process some PII. Every employee's RFID card contains a unique ID which is read by the Raspberry pi in the hand sanitizer. This unique ID is what allows Django to associate instances of hand sanitizing with individual employees. The information is securely transmitted over a local network. The sanitizing stations are intended to be placed inside of the company building in order to minimize outside physical access.

### Django licensing
Django is a free and open source project. It is licensed under a standard 3-clause BSD license which allows "Redistribution and use in source and binary forms, with or without modification".[^1] This license is very permissive and gives us the freedom to redistribute the source code with very few requirements.

### Our license
The product would be released under a modified version of the GNU general public licence. This license would encourage the use of the product while maintaining the intellectual property of our machine learning algorithms. 

## Ethical

- Individuals could be punished based on the hand sanitization metrics. The product gives employers several new metrics which they can use minimize infection spread. However, this information could be misused to target individuals who might not meet the expected targets.

- Improper use of the hand sanitizer by an employee could be exploited to artificially increase the individual metrics. There are several features in the code of the hand sanitizer software to protect the integrity of the data collected. One such feature is a limit on the number of times one employee can use the hand sanitizer in short succession. However, the possibility of hand sanitizations being faked exists, especially if there is a reward associated with high individual metrics.


- Downtime in an individual hand sanitizer could negatively impact the overall metrics of certain employees. The hand sanitizing stations don't store any data for GDPR reasons. A network outage or an issue with a sanitizing station could make it seem as though the employees using it haven't sanitized their hands. Small deviations would not significantly impact the long-term metrics but short-term metrics could be skewed as a result.

- Given enough sanitizing stations, the employer could potentially track the movement of an employee based on the hand sanitization data. This wouldn't be an issue for an organization with a couple of sanitizing stations but an employer in a bigger organization could misuse the collected data to target individual employees. For example, lunch break duration could be deduced by comparing the times between hand sanitizations. One when entering a lunch area and the second when exiting it. 


## Health and Safety

- Error in the classification machine learning algorithm could put employees in the wrong risk group. Depending on how the employer uses the classification data, an error could put individuals at risk by giving them a false sense of security. As a result of being in the wrong category, employees could potentially take health and safety risk they might avoid if they were in the right risk group.

- Employees could be prevented from sanitizing their hands if there was an issue with the sanitizing station. The time it would take to repair the sanitizing station could negatively impact the infection prevention controls of the company. The lack of hand sanitizations at a certain area could increase the transmission of infectious viruses and therefore put people at risk.

[^1]: https://opensource.org/licenses/BSD-3-Clause
