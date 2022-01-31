# Neural Network example 
This system uses 4 signals derived from collective data on out system. It utilizes this data to refine a warning system that can tell users the risk from 0 - 10 of the chance that a viral pathogen could be spreading and do significant damage within the workplace to individuals and their productivity.

## Neural Network inputs

Below are the 4 methods of analysis I have thought would have the best inputs for a neural algorithm that could tell users when the collective/company is in danger/ at risk. The information on each signal is shown below and a brief overview on how they work, and what they would input into the neural network.

# 1. **Crossover Signal of MA**

The 90 day moving average and 10 day moving average can help us see the relationship between the macro/micro trends. 
In this example we would want to see when the 10ma passes over the 90ma, this would mean **recent** data is not abiding by 
current trends and a shift is occuring (eother downwards or upwards)

![alt text](https://media.dailyfx.com/illustrations/2012/12/28/Learn_Forex_Trend_Trading_Rules_with_Moving_Average_Crosses_body_Picture_1.png "Logo Title Text 1")

As you can see in the image above, the crossover will signal a trend within the data itself. The lower moving average passing over the higher moving average means that there could be an expected rise in price, (**In our case this would be an increase in the amount of sick employees due to external circumstances**). Alone it is not a worthy indicator to try and predict future figures and past performance will never let us with 100% confidence predict future behaviour.

### The output of this signal would be a 0/1 value for if a crossover occurs indicating an upwards trend in the last week (of working days)


# 2. **Crossover Signal of EMA** (MACD Signalling)

A normal moving average takes into account all the days it encapsulates equally. Everyday in a 90 day Moving average has the same 'weight' in the average equally. An exponential moving average is better in this regard as it will ensure values closer to the current date have more 'weight' within the final average value.

![alt text](https://www.theoptionsguide.com/images/macd-indicator.png "Logo Title Text 1")


As you can see above, we use a "signal line" which is a smoothed value of another specified moving average (in this example it is the 9EMA). This functions similarly to the 1st Specified signal but by using the difference of the two lines y values we can visualize the 'intent' of the trend in the blue histogram shown below the main figure. A bullish signal would mean for us a rise in the number of sick employees. 


# 3. **AutoRegressive Model** of Risk Group Categories

An autoregressive model is a "**time series model** that uses observations from previous time steps as input to a regression equation to predict the value at the next time step". In out example the figure we would plot on the y value is the total number of High Risk Category Employees. This indicator assumes as the number of people not washing their hands in accordance with guidelines, the higher risk we are in as a collective company.

This is useful to help give us a window of what the next values could be represented as. The values given from the prediction on a 7+day buffer time window will provide information on the future trend of the amount of employees within the high sick group category.

![alt text](https://www.researchgate.net/profile/Ales-Prochazka/publication/237396657/figure/fig5/AS:646454993506305@1531138289168/Prediction-results-for-autoregressive-model-short.png "Logo Title Text 1")

This above example shows the accuracy of specific autoregression models. As you can see the model can help predict future values as shown in the image above, the 'testing part' would hold only predictive values.
In our case we would want to calculate the difference in how the predicted amount of high risk individuals increases or the possibility of it increasing to a higher value. This would be done taking into account the value of high risk employees **now** and comparing it to the predicted value 7 days from now. A positive increase would then signal that the chance for damage to be done in the workplace would increase. 

### The output of this signal would be a signal displaying change in value of the number of high risk employees from current date to 7 next days. 

# 4. **Gradient/ Rate of growth of High Risk Group individuals**

We can use the actual gradient of the 'singal line' of the amount of high risk group individuals themselves. The rate of change of people entering the high risk zone could signal company/collective wide insubordination of the washing guidelines which in turn could result in a higher risk of infection/viral spread.

![alt text](https://useruploads.socratic.org/69VemDw4RJWsL6dSmB2S_Tangent.png "Logo Title Text 1")

A less sophisitaced signal by far but not an insignificant piece of information. If we take the gradient of the change in high risk individuals this week and the week prior we can evaluate the amount of individuals taking part in the specified guidelines. 

If the gradient value increases from week 1 to 2 then we can evaluate that there are more individuals not sanitizing their hands correctly as the **rate of change itself** is increasing. We only need a short window on this to evaluate the signal of increased risk 

### The output of this signal would be a signal displaying change in value of the gradient of the amount of people in the high risk category.

## Neural Network Initial construction
![alt text](https://cseegit.essex.ac.uk/2020_ce299/ce299_team05/-/raw/master/documents/images/NeuralNet.png "Logo Title Text 1")

The Neural network will output a ranking or predictive score based on several test data samples that will tell the users the impact and risk of spread within the workplace. This could be valued either on a scale of 0 - 10 or 0 - 100 from the output of **y**

