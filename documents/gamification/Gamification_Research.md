# Gamification Research
This document contains research and ideas for the gamification of our product.
A list of sources can be found on the bottom of the document.

## When should you wash/sanitize your hands?

### Key Times to Wash Hands
* Before, during, and after preparing food
* Before and after eating food
* Before and after caring for someone at home who is sick with vomiting or diarrhea
* Before and after treating a cut or wound
* After using the toilet
* After changing diapers or cleaning up a child who has used the toilet
* After blowing your nose, coughing, or sneezing
* After touching an animal, animal feed, or animal waste
* After handling pet food or pet treats
* After touching garbage

### Covid-19 Prevention
* Before and after touching your eyes, nose, or mouth
* Before and after touching your mask
* Entering and leaving a public place
* Touching an item or surface that may be frequently touched by other people, such as door handles, tables, gas pumps, shopping carts, or electronic cashier registers/screens


## How often should you wash/sanitize your hands?
There isn't a set amount of times a person should wash their hands, it only depends on what you've been doing
So someone working in a hospital would need to wash their hands more than an office worker.


## What can/should our product track?
Ideas for what our product could track in various enviroments.

### Hospital/Care Home/Clinic
* Check that you wash/sanitize before and after taking a lunch break
* Check that you wash/sanitize after using the toilet
* Check that you wash/sanitize when coming to and leaving work
* Before and after caring for someone who is sick with vomiting or diarrhea (Use of gloves and other equipment might mean this is unnecessary)
* Before and after treating a cut or wound (Might not be necessary, same reason as above)
* After touching garbage (Possibly)

### Normal Office Space
* Check that you wash/sanitize before and after taking a lunch break
* Check that you wash/sanitize after using the toilet
* Check that you wash/sanitize when coming to and leaving work

### School Enviroment (Teachers)
* Check that you wash/sanitize before and after taking a lunch break
* Check that you wash/sanitize after using the toilet
* Check that you wash/sanitize when coming to and leaving work
* Touching an item or surface that may be frequently touched by other people, such as door handles, tables, gas pumps, shopping carts, or electronic cashier registers/screen (Holding a lecture/class)

### More examples ...

## Gamification Initial Thoughts
The gamification needs to be balanced in a way, that it can't be abused.
Perhaps an upper limit for amount of times washed or a cooldown so you can't wash to often.
The upper limit seems like the best idea, setting a standard for how many times you should wash your hands.
Combining it with the cooldown would mean employees coudln't simply wash 10 times before leaving.

By guessing, I'd say that in a normal office workspace, you should wash/sanitize your hands:
1. When arriving at work
2. Bathroom break before lunch (at any point)
3. Before eating lunch
4. After eating lunch
5. Bathroom break after lunch (at any point)
6. When leaving work
So six times in total. Need to do more research to find out if that is an optimal amount.

The users score and cooldown timer needs to be stored somewhere, most likely in a database.
The database could be a seperate table linking to the employee, and would reset every day.

## Gamification Idea 1
* A system that has an upper limit, based on how often you should wash your hands.
* A cooldown timer for each employee, so they can't abuse the system to get points.
* The upper limit would be set by the administrator, based on their needs.
* The cooldown timer would be based on the amount the administrator chooses. Possibly zero?


## Sources
* [Centers for Disease Control and Prevention](https://www.cdc.gov/handwashing/when-how-handwashing.html)
* [Healthline](https://www.healthline.com/health/how-long-should-you-wash-your-hands#when-to-wash-hands)
* [WebMD](https://www.webmd.com/cold-and-flu/qa/how-often-should-you-wash-your-hands)
* [NHS](https://www.nhs.uk/live-well/healthy-body/best-way-to-wash-your-hands/)
