"""
Provide a program to calculate the time and distance based on
below problem.
• We have a 100-meter rod.
• At both ends, 1-1 cockroach is place.
• The left cockroach moves at 1 meter per second forward, and every 10 seconds moves 2
meters backward.
• The right cockroach moves at 2 meters per second forward, and every 5 seconds moves 1
meter backward.
• When both cockroaches meet, we have to calculate the time and distance. Calculate the total
time to complete the 100 meter rod
"""


import pandas as pd

time1 = 0 # time for cockroach 1 set to 0
dist1 = 0 # cockroach 1 starts from distance = 0 m
list1 = [] # passing empty list to store time for cockroach 1
listd1 = [] # passing empty list to store distance for cockroach 1

while time1<150:
  time1 = time1+1
  list1.append(time1)
  if time1%10 == 0:
    dist1 = dist1-1
  else:
    dist1 = dist1+1
  listd1.append(dist1)

time2 = 0 # time for cockroach 2 set to 0
dist2 = 100 # cockroach 2 starts from distance = 100 m
list2 = [] # passing empty list to store time for cockroach 2
listd2 = [] # passing empty list to store distance for cockroach 2
while time2<150:

  time2 = time2+1
  list2.append(time2)
  if time2%5 == 0:
    dist2 = dist2-1
  else:
    dist2 = dist2-2
  listd2.append(dist2)

dict = {'time': list1, 'distofcockroach1': listd1, 'distofcockroach2':listd2} # storing values in dict
data = pd.DataFrame(data=dict) # creating a pandas dataframe
print(data)
# data.to_excel("Final_Data.xlsx") # exporting the file with title - Final_Data.xlsx
print("Distance covered by cockroach 1")
print(data[data.distofcockroach1==100]) #cockroach 1 completes 100m rod in 124 seconds

print("Distance covered by cockroach 2")
print(data[data.distofcockroach2==1]) # cockroach 2 completes 100m rod in 56 seconds

print("Calculate distance where both cockroaches meet with each other")
print(data.head(40))
"""as per data we can see that both cockroaches meet at the distance 31m on the left side of the rod at time 38 sec """