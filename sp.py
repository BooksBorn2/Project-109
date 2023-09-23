import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics 
import random #Creating a list of sum of 2 dice, rolled 1000 times 
dice_result = [] 
for i in range(0, 1000): 
    dice1 = random.randint(1, 6)
    dice2 = random.randint(1, 6) 
    dice_result.append(dice1 + dice2) 
median = statistics.median(dice_result)
#Calculating the mean and the standard deviation 
mean = sum(dice_result) / len(dice_result) 
std_deviation = statistics.stdev(dice_result) 
mode = statistics.mode(dice_result)
first_std_deviation_start, first_std_deviation_end = mean - std_deviation, mean + std_deviation
second_std_deviation_start, second_std_deviation_end = mean - (2*std_deviation), mean +(2*std_deviation)
third_std_deviation_start, third_std_deviation_end = mean - (3*std_deviation), mean +(3*std_deviation)
d1 = [result for result in dice_result if result > first_std_deviation_start and result < first_std_deviation_end]
d2 = [result for result in dice_result if result > second_std_deviation_start and result < second_std_deviation_end]
d3 = [result for result in dice_result if result > third_std_deviation_start and result < third_std_deviation_end]
print("Mean of this data is {}".format(mean))
print("Median of this data is {}".format(median))
print("Mode of this data is {}".format(mode))
print("")
print("Standard deviation of this data is {}".format(std_deviation))
print("First standard deviation of this data is {}".format(len(d1)*100.0/len(dice_result)))
print("Second standard deviation of this data is {}".format(len(d2)*100.0/len(dice_result)))
print("Third standard deviation of this data is {}".format(len(d3)*100.0/len(dice_result)))