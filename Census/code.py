# --------------
# Importing header files
import numpy as np

# Path of the file has been stored in variable called 'path'

#New record
new_record=np.array([[50,  9,  4,  1,  0,  0, 40,  0]])

#Code starts here
data_file= path
data=np.genfromtxt(data_file, delimiter= ",", skip_header=1)
print('\ndata: \n', data)
print("\nType of Data: \n\n", type(data))
census=np.concatenate((data, new_record), axis=0)
print('\ndata: \n', census)


# --------------
#Code starts here
age= census[:,0]
max_age=np.max(age)
print("\nMaximum Age: ", max_age)
min_age=np.min(age)
print("\nMinimum Age: ",min_age)
age_mean=np.mean(age)
print("\nAverage Age: ",age_mean)
age_std=np.std(age)
print("\nStandard Deviation of Age: ",age_std)


# --------------
#Code starts here
race_0= census[census[:,2]==0]
race_1=census[census[:,2]==1]
race_2=census[census[:,2]==2]
race_3= census[census[:,2]==3]
race_4=census[census[:,2]==4]
len_0= len(race_0)
len_1=len(race_1)
len_2=len(race_2)
len_3=len(race_3)
len_4=len(race_4)
if min(len_0, len_1, len_2, len_3, len_4)==len_0:
    minority_race=0
elif min(len_0, len_1, len_2, len_3, len_4)==len_1:
    minority_race=1
elif min(len_0, len_1, len_2, len_3, len_4)==len_2:
    minority_race=2
elif min(len_0, len_1, len_2, len_3, len_4)==len_3:
    minority_race=3
else:
    minority_race=4
print(minority_race)


# --------------
#Code starts here
senior_citizens= census[census[:,0]>60]
working_hours_sum=sum(senior_citizens[:,6])
senior_citizens_len=len(senior_citizens)
avg_working_hours=working_hours_sum/senior_citizens_len
print(avg_working_hours)


# --------------
#Code starts here
high=census[census[:,1]>10]
low=census[census[:,1]<=10]
avg_pay_high= high[:,7].mean()
avg_pay_low= low[:,7].mean()
print(avg_pay_high, avg_pay_low, avg_pay_high>avg_pay_low)


