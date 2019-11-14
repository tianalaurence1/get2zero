# Tiana Laurence
# 11.14.2019
# Description: This is a calculator that estimates the number of trees that an individual
# needs to move from carbon production to carbon sequestration.


'''Some variables that relate to carbon outputs and inputs'''
carbon_out = 65000  # The number of pounds of CO2 an average human produces a year.
tree_in = 13  # The number of pounds a young tree consumes a year
tree_space = 20 * 20  # The space in feet a single tree needs to grow
feet_space = carbon_out / tree_in * tree_space  # the space in feet all the trees need
acre_space = feet_space / 43560  # The square feet in an acre 43560, this is to find space in acres for trees
hectare_space = feet_space / 107640 # There are 107639.1 square feet in a hector, this is to hid hector space for trees
meter_space = feet_space / 11 # There are 10.76 feet in a meter

