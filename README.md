# Carbon Capture Calculator
This is Python code to calculate the amount of CO2 captured from a DAC (Direct Air Capture) machine, specifically a moisture swing system. This code plays nicely with some other code I wrote: https://github.com/charlienicholson3/SCD30-Code/tree/main. To learn more about how to make your own DAC machine, visit my website: https://nicholsonlabs.gitbook.io/labs/carbon-capture.

There are two different files for the carbon capture calculator. The ```co2CalculatorPump.py``` file calculates CO2 captured from the air going through the capture membrane, measures the CO2 difference between the inlet and outlet, and then does some math to find the CO2 captured. On the other hand, ```co2CalculatorBox.py``` calculates captured CO2 from either the increase or decrease of CO2 in a closed environment, like a box. Both of these can be configured to measure the regeneration of the sorbent and the capture of CO2. However, ```co2CalculatorBox.py``` is already configured to work in a regeneration style, and ```co2CalculatorPump.py``` is configured to work in a capture style. 

# Steps to use this code:
1. Open up a Google Colab or your preferred editor
2. Fill out the variables at the top of the file
3. Press run, and look at the output in the terminal
4. Look at my code to see if I did anything wrong or if any improvements can be made!

# co2CalculatorPump:
To configure this snippet to work in a system releasing captured CO2, find this line: ```ppmDifference = inlet - outlet``` and replace it with ```ppmDifference = outlet - inlet```. Then, change the inlet and the outlet variables accordingly.

# co2CalculatorBox:
To configure this snippet to work in a system measuring a decrease in CO2, find this line: ```ppmRise = ppmEnd - ppmStart``` and replace it with ```ppmRise = ppmStart - ppmEnd```. Then, change the ppmEnd and the ppmStart variables accordingly.

One last note. I tend to get excited and skip over words when I write code or when I write in general, so I'm sorry for any grammatical mistakes.
