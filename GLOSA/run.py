import random
from BatAlgorithm import *
import pandas as pd
import numpy as np

df=np.random.randint(30,100,(100,3))                 #random number generator
df=pd.DataFrame(df,columns=['NumberOfVehicle','AverageSpeed','DistanceBetweenVehicleAverage']) #giving names to the rows
df.to_csv('data.csv')                          #saving in the file named data.csv
df=df.values
prob_dim=(len(df))
pop_size=10
data_set=[[0 for x in range(prob_dim)] for x in range(pop_size)]

def generate(df):
    no_of_lane=prob_dim
    for i in range(pop_size):
        for j in range(no_of_lane):
            data_set[i][j]=((df[j][0]*df[j][1])//df[j][2])
            # print(data_set[i][j])
    return data_set


data_set=generate(df)
def Fun(D, sol):
    val = 0.0
    for i in range(D):
        val = val + sol[i] * sol[i]
    return val

# For reproducive results
#random.seed(5)
import csv
with open('data.csv', newline='') as csvfile:
 data = csv.reader(csvfile, delimiter=' ', quotechar='|')
 for row in data:
   print(', '.join(row))

for i in range(10):
    Algorithm = BatAlgorithm(10, 40, 1000, 0.5, 0.5, 0.0, 2.0, -10.0, 10.0, Fun)  #10, 40, 1000, 0.5, 0.5, 0.0, 2.0, -10.0, 10.0
    Algorithm.move_bat()
    