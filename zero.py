# Tiana Laurence
# 11.14.2019
# Description: This is a calculator that estimates the number of trees that an individual
# needs to move from carbon production to carbon sequestration.


"""Some variables that relate to carbon outputs and inputs"""
ton = 20  # The metric tonnage of co2 produced by an average american
pound_c = ton * 2205  # The number of pounds in a metric ton 2205, this is the pounds of carbon per american
tree_in = 13  # The pounds co2 a young tree consumes a year
tree_space = 12 * 12  # The space in feet a single tree needs to grow
feet_space = int (pound_c / tree_in * tree_space)  # the space in feet all the trees need
acre_space = int (feet_space / 43560)  # The square feet in an acre 43560, this is to find space in acres for trees
hectare_space = int (feet_space / 107640)  # 107639.1 square feet in a hector, this is to hid hector space for trees
meter_space = int (feet_space / 11)  # There are 10.76 feet in a meter
trees = int (pound_c / tree_in + 1)
meat_meal = int (7 - 3)  # CO2 in meat 6.61 lbs CO2 and beans to replace the calories at 2.25 lbs CO2

while True:
    meal = input("Did your meal have any meat? Enter yes or no:")
    if meal == "no":
        meal = -4 # the CO2 savings no meat
    else:
        meal = 4 # the CO2 cost meat in one meal
    print(meal)
    break

new_number = int((meal + pound_c)/tree_in)
print("The new number of tees you need", new_number)


print("The pounds of CO2 produced a year:", pound_c)
print("The number of trees:", trees)
print("The number of acres:", acre_space)
print("CO2 output of one meal with meat:", meat_meal)
