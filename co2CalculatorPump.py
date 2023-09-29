# This calculator is meant for systems that pump air through a capture chamber
# This measures CO2 based on the difference between the CO2 ppm at the inlet and the outlet, so two sensors are needed at both ends
# Note that the code might be wrong so use it at your own risk
# Credits: Charles Nicholson, 2023
# Licensed under an GNU GPL v3 license, basically means you can do whatever you want
# My website so you can learn more about this system and usage of this code snippet: https://bit.ly/44Ig0Lz

# Varaibles you can change based off your scrubber:
inlet = 400 # CO2 ppm at the inlet of your scrubber
outlet = 350 # CO2 ppm at the outlet of your srubber
lpm = 10 # liters per minute of your pump
pumpTime = 1440 # minutes your pump is working throughout day (right now this is configured to run 24 hours, which wouldn't actually work in a real system because of regeneration. That being said, you could hve multiple capturing chambers.)
mpg = 30 # miles per gallon
efficiency = 1 # just in case you want to play around and see what happens when you increase the effciency
carbonFootprint = 16 # average annual metric tons emitted by an American. Find out your own here:
# https://www.nature.org/en-us/get-involved/how-to-help/carbon-footprint-calculator/
cost = 150 # the amount of money it costs to make your system. This will be calculated to show how much money is needed for net zero.
estimatedMassCost = 10 # cost with mass production and cheaper materials of the machine. This will be calculated to show how much money is needed for net zero.
treeCost = 0.5 # the cost of a sapling in US dollars (probably cheaper than 50 cents)

# You probably shouldn't play with this stuff:
molecularWeight = 44.01 # g/mol of CO2
co2PerGallon = 8.887 # kilos of CO2 emitted by burning through a whole gallon of gasoline, not including earlier-on emissions like transportation
treeKilos = 22 # kilos of CO2 an adult tree removes annually https://www.usda.gov/media/blog/2015/03/17/power-one-tree-very-air-we-breathe#:~:text=According%20to%20the%20Arbor%20Day,and%20release%20oxygen%20in%20exchange.

# And now were doing the math:
litersAir = lpm * pumpTime
ppmDifference = inlet - outlet
co2Concentration = ppmDifference / 1000000
co2Grams = co2Concentration * litersAir * molecularWeight
co2Grams = co2Grams * efficiency

co2Kilo = co2Grams / 1000
capturedGallons = co2Grams / co2PerGallon
miles = capturedGallons / mpg
feet = miles * 5280
inches = feet * 12

tonsMetric = co2Grams / 1000000
yourImpact = tonsMetric / carbonFootprint * 100 * 365 # (in percent) how much this contributes to bringing down your annual carbon emmissions
gigatons = tonsMetric / 1000000000 # how many gigatons of CO2 you captured
impact = gigatons / 5 # https://marginalcarbon.substack.com/p/how-much-carbon-will-we-need-to-remove
impactCH4N2O = gigatons / 19.7 # this includes offsets for other GHGs https://marginalcarbon.substack.com/p/how-much-carbon-will-we-need-to-remove
percent24hr = impact * 100
percent24hrCH4N2O = impactCH4N2O * 100
percent365 = percent24hr * 365 # how much it contributes in a year
percent365CH4N2O = percent24hrCH4N2O * 365
hundredMil = percent365 * 100000000
hundredMilCH4N2O = percent365CH4N2O * 100000000

treeDailyGrams = treeKilos * 1000 / 365 # dividing by 1000 to get grams and then dividing by 365 to get daily grams
treeTon = treeDailyGrams / 1000000
treeGiga = treeTon / 1000000000
neededTrees = 5 / treeGiga # finding how many trees we need
totalTreeCost = neededTrees * treeCost
treeEfficiency = treeDailyGrams / co2Grams
machines = 5 / gigatons # we need to remove 5 gigatons a year
scaledCost = machines * cost
scaledMassCost = machines * estimatedMassCost
machines = round(machines)
costEffectivness = scaledMassCost / totalTreeCost # here, we are finding the cost effectivness of you machine compared to adult trees

if costEffectivness >= 1: # here, we are finding whether to print more or less in the output of the calculations
  placeHolderCost = "more"
else:
  placeHolderCost = "less"

if treeEfficiency >= 1: # here, we are finding whether to print more or less in the output of the calculations
  placeHolderEfficiency = "more"
else:
  placeHolderEfficiency = "less"

# Converting into a string and taking away scientific notation so it's easier to read:
yourImpact = f'{yourImpact:.7f}'
tonsMetric = f'{tonsMetric:.30f}'
percent365 = f'{percent365:.30f}'
percent365CH4N2O = f'{percent365CH4N2O:.30f}'
hundredMil = f'{hundredMil:.15f}'
hundredMilCH4N2O = f'{hundredMilCH4N2O:.15f}'
scaledCost = f'{scaledCost:,}'
scaledMassCost = f'{scaledMassCost:,}'
machines = f'{machines:,}'
miles = f'{miles:.9f}'
treeEfficiency = f'{treeEfficiency:.4f}'
costEffectivness = f'{costEffectivness:.4f}'

# Printing our results:
print("Grams of CO2 captured in 24 hours: ") # assuming that the machine is running for 24 hours
print(co2Grams)
print("How many miles of car travel you offsetted (in 24 hrs): ") # assuming 30 MPG car burning gasoline, also assuming that the machine is running for 24 hours
print(miles)
print("How many feet of car travel you offsetted (in 24 hrs): ") # assuming 30 MPG car burning gasoline, also assuming that the machine is running for 24 hours
print(feet)
print("How many inches of car travel you offsetted (in 24 hrs): ") # assuming 30 MPG car burning gasoline, also assuming that the machine is running for 24 hours
print(inches)
print("Metric tons of CO2 captured in 24 hours: ")
print(tonsMetric)
print("Part of the annual 5 gigatons we need to remove by 2050 (impact it has in a year): ")
print(percent365 + "%")
print("And if 100 million people had these: ")
print(hundredMil + "%")
print("Part of the annual 19.7 gigatons we to remove to offset carbon, CH4, and N2O: ")
print(percent365CH4N2O + "%")
print("And if 100 million people had these: ")
print(hundredMilCH4N2O + "%")
print("And all of this offsets your footprint by this much: ") # just carbon, not including methane and N2O
print(yourImpact + "%")
print("Cost of net zero with current system: ") # if you had enough of your machines to do net zero
print("$" + scaledCost)
print("Cost of net zero with mass-produced current system: ") # if you had enough of your machines to do net zero, but the cost is the mass production cost
print("$" + scaledMassCost)
print("Which is equal to " + machines + " machines")
print("------------- Bottom line -------------")
print("A tree can remove " + treeEfficiency + " times " + placeHolderEfficiency  + " than your machine")
print("For carbon neutrality, you would need to spend " + costEffectivness + " times " + placeHolderCost + " money on your machine than using trees")
print("------------- Final word --------------")
if placeHolderCost == "more":
  print("So in all, trees are more cost effective than your machine, but you should keep trying!")
else:
  print("Woohoo! You machine is more cost effective than trees! Now you need to find the carbon footprint of your machine...") # celebration!
