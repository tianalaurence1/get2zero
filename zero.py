# Tiana Laurence
# 11.14.2019
# Description: This is a calculator that estimates the number of trees that an individual
# needs to move from carbon production to carbon sequestration.



'''Some variables that relate to carbon outputs and inputs'''
carbon_out = 65000  # The number of pounds of CO2 an average human produces a year.
tree_in = 13  # The number of pounds a young tree consumes a year
tree_space = 20 * 20  # The space in feet a single tree needs to grow
human_space = carbon_out/tree_in * tree_space  # the space a human needs to have sufficient trees to get to zero
print(human_space)







