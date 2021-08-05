import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import statistics as stat
#track_freq = np.zeros((100,num_cycles + 1,4))

#### Atov
num_sim = 100

num_cycles = 30

freq_01 = glob.glob('Poolsize_A_*_3.csv')
freq_015 = glob.glob('Poolsize_A_*_75_015.csv')
freq_02 = glob.glob('Poolsize_A_*_75_02.csv')
freq_025 = glob.glob('Poolsize_A_*_75_025.csv')

list_data_NP_01 = []
list_data_NP_015 = []
list_data_NP_02 = []
list_data_NP_025 = []
#
for filename in freq_01:
     data_NP_01 = pd.read_csv(filename,header=None)
     list_data_NP_01.append(data_NP_01)
pd.concat(list_data_NP_01,ignore_index=True)

for filename in freq_015:
     data_NP_015 = pd.read_csv(filename,header=None)
     list_data_NP_015.append(data_NP_015)
pd.concat(list_data_NP_015,ignore_index=True)

for filename in freq_02:
     data_NP_02 = pd.read_csv(filename,header=None)
     list_data_NP_02.append(data_NP_02)
pd.concat(list_data_NP_02,ignore_index=True)

for filename in freq_025:
     data_NP_025 = pd.read_csv(filename,header=None)
     list_data_NP_025.append(data_NP_025)
pd.concat(list_data_NP_025,ignore_index=True)


print(np.shape(list_data_NP_01[0]))
#print(np.shape(list_data_NP_01[99]))

track_freq_01 = np.zeros((num_sim,num_cycles + 1))
track_freq_015 = np.zeros((num_sim,num_cycles + 1))
track_freq_02 = np.zeros((num_sim,num_cycles + 1))
track_freq_025 = np.zeros((num_sim,num_cycles + 1))

for i in range(0,num_sim):
         track_freq_01[i,:] = list_data_NP_01[i].iloc[0:num_cycles + 1].T
         track_freq_015[i,:] = list_data_NP_015[i].iloc[0:num_cycles + 1].T
         track_freq_02[i,:] = list_data_NP_02[i].iloc[0:num_cycles + 1].T
         track_freq_025[i,:] = list_data_NP_025[i].iloc[0:num_cycles + 1].T
print(np.shape(track_freq_01))



mean_track_pool_01 = np.nanmean(track_freq_01) #, axis = 0)
std_track_pool_01 = np.nanstd(track_freq_01) #, axis = 0)

mean_track_pool_015 = np.nanmean(track_freq_015) #, axis = 0)
std_track_pool_015 = np.nanstd(track_freq_015) #, axis = 0)

mean_track_pool_02 = np.nanmean(track_freq_02) #, axis = 0)
std_track_pool_02 = np.nanstd(track_freq_02) #, axis = 0)

mean_track_pool_025 = np.nanmean(track_freq_025) #, axis = 0)
std_track_pool_025 = np.nanstd(track_freq_025) #, axis = 0)


counter = 0
cyc_ext_A_01 = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_01[j,i] == 0:
            cyc_ext_A_01[j] = i
            break

print(cyc_ext_A_01)

cyc_ext_A_01[cyc_ext_A_01 == 0] = np.nan
mean_data_A1 = np.nanmean(cyc_ext_A_01,axis = 0)
std_data_A1 = np.nanstd(cyc_ext_A_01,axis = 0)
print(mean_data_A1)
print(std_data_A1)

mode_data_A1 = stat.mode(cyc_ext_A_01)
var_data_A1 = stat.variance(cyc_ext_A_01)


counter = 0
cyc_ext_A_015 = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_015[j,i] == 0:
            cyc_ext_A_015[j] = i
            break

print(cyc_ext_A_015)

cyc_ext_A_015[cyc_ext_A_015 == 0] = np.nan
mean_data_A15 = np.nanmean(cyc_ext_A_015,axis = 0)
std_data_A15 = np.nanstd(cyc_ext_A_015,axis = 0)
mode_data_A15 = stat.mode(cyc_ext_A_015)
var_data_A15 = stat.variance(cyc_ext_A_015)


counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_02[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_A2 = np.nanmean(cyc_ext,axis = 0)
std_data_A2 = np.nanstd(cyc_ext,axis = 0)

mode_data_A2 = stat.mode(cyc_ext)
var_data_A2 = stat.variance(cyc_ext)


counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_025[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_A25 = np.nanmean(cyc_ext,axis = 0)
std_data_A25 = np.nanstd(cyc_ext,axis = 0)
mode_data_A25 = stat.mode(cyc_ext)
var_data_A25 = stat.variance(cyc_ext)





#### CHLOROQUINE
num_sim = 100

num_cycles = 30

freq_01 = glob.glob('Poolsize_C_*_75_01.csv')
freq_015 = glob.glob('Poolsize_C_*_75_015.csv')
freq_02 = glob.glob('Poolsize_C_*_75_02.csv')
freq_025 = glob.glob('Poolsize_C_*_75_025.csv')

list_data_NP_01 = []
list_data_NP_015 = []
list_data_NP_02 = []
list_data_NP_025 = []
#
for filename in freq_01:
     data_NP_01 = pd.read_csv(filename,header=None)
     list_data_NP_01.append(data_NP_01)
pd.concat(list_data_NP_01,ignore_index=True)

for filename in freq_015:
     data_NP_015 = pd.read_csv(filename,header=None)
     list_data_NP_015.append(data_NP_015)
pd.concat(list_data_NP_015,ignore_index=True)

for filename in freq_02:
     data_NP_02 = pd.read_csv(filename,header=None)
     list_data_NP_02.append(data_NP_02)
pd.concat(list_data_NP_02,ignore_index=True)

for filename in freq_025:
     data_NP_025 = pd.read_csv(filename,header=None)
     list_data_NP_025.append(data_NP_025)
pd.concat(list_data_NP_025,ignore_index=True)


print(np.shape(list_data_NP_01[0]))


track_freq_01 = np.zeros((num_sim,num_cycles + 1))
track_freq_015 = np.zeros((num_sim,num_cycles + 1))
track_freq_02 = np.zeros((num_sim,num_cycles + 1))
track_freq_025 = np.zeros((num_sim,num_cycles + 1))

for i in range(0,num_sim):
         track_freq_01[i,:] = list_data_NP_01[i].iloc[0:num_cycles + 1].T
         track_freq_015[i,:] = list_data_NP_015[i].iloc[0:num_cycles + 1].T
         track_freq_02[i,:] = list_data_NP_02[i].iloc[0:num_cycles + 1].T
         track_freq_025[i,:] = list_data_NP_025[i].iloc[0:num_cycles + 1].T
print(np.shape(track_freq_01))

counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_01[j,i] == 0:
            cyc_ext[j] = i
            break

print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_C1 = np.nanmean(cyc_ext,axis = 0)
std_data_C1 = np.nanstd(cyc_ext,axis = 0)
print(mean_data_C1)
print(std_data_C1)
mode_data_C1 = stat.mode(cyc_ext)
var_data_C1 = stat.variance(cyc_ext)



counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_015[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_C15 = np.nanmean(cyc_ext,axis = 0)
std_data_C15 = np.nanstd(cyc_ext,axis = 0)

mode_data_C15 = stat.mode(cyc_ext)
var_data_C15 = stat.variance(cyc_ext)

counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_02[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_C2 = np.nanmean(cyc_ext,axis = 0)
std_data_C2 = np.nanstd(cyc_ext,axis = 0)
mode_data_C2 = stat.mode(cyc_ext)
var_data_C2 = stat.variance(cyc_ext)

counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_025[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_C25 = np.nanmean(cyc_ext,axis = 0)
std_data_C25 = np.nanstd(cyc_ext,axis = 0)

mode_data_C25 = stat.mode(cyc_ext)
var_data_C25 = stat.variance(cyc_ext)

#### ATOV CHLOROQUINE
num_sim = 93

num_cycles = 30

freq_01 = glob.glob('Poolsize_AC_*_75_01.csv')
freq_015 = glob.glob('Poolsize_AC_*_75_015.csv')
freq_02 = glob.glob('Poolsize_A_*_75_01.csv')
freq_025 = glob.glob('Poolsize_AC_*_75_025.csv')

list_data_NP_01 = []
list_data_NP_015 = []
list_data_NP_02 = []
list_data_NP_025 = []
#
for filename in freq_01:
     data_NP_01 = pd.read_csv(filename,header=None)
     list_data_NP_01.append(data_NP_01)
pd.concat(list_data_NP_01,ignore_index=True)

for filename in freq_015:
     data_NP_015 = pd.read_csv(filename,header=None)
     list_data_NP_015.append(data_NP_015)
pd.concat(list_data_NP_015,ignore_index=True)

for filename in freq_02:
     data_NP_02 = pd.read_csv(filename,header=None)
     list_data_NP_02.append(data_NP_02)
pd.concat(list_data_NP_02,ignore_index=True)

for filename in freq_025:
     data_NP_025 = pd.read_csv(filename,header=None)
     list_data_NP_025.append(data_NP_025)
pd.concat(list_data_NP_025,ignore_index=True)


print(np.shape(list_data_NP_01[0]))

track_freq_01 = np.zeros((num_sim,num_cycles + 1))
track_freq_015 = np.zeros((num_sim,num_cycles + 1))
track_freq_02 = np.zeros((num_sim,num_cycles + 1))
track_freq_025 = np.zeros((num_sim,num_cycles + 1))

for i in range(0,num_sim):
         track_freq_01[i,:] = list_data_NP_01[i].iloc[0:num_cycles + 1].T
         track_freq_015[i,:] = list_data_NP_015[i].iloc[0:num_cycles + 1].T
         track_freq_02[i,:] = list_data_NP_02[i].iloc[0:num_cycles + 1].T
         track_freq_025[i,:] = list_data_NP_025[i].iloc[0:num_cycles + 1].T
print(np.shape(track_freq_01))


counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_01[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_AC1 = np.nanmean(cyc_ext,axis = 0)
std_data_AC1 = np.nanstd(cyc_ext,axis = 0)

mode_data_AC1 = stat.mode(cyc_ext)
var_data_AC1 = stat.variance(cyc_ext)

counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_015[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_AC15 = np.nanmean(cyc_ext,axis = 0)
std_data_AC15 = np.nanstd(cyc_ext,axis = 0)
mode_data_AC15 = stat.mode(cyc_ext)
var_data_AC15 = stat.variance(cyc_ext)
counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_02[j,i] == 0:
            cyc_ext[j] = i
            break
print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_AC2 = np.nanmean(cyc_ext,axis = 0)
std_data_AC2 = np.nanstd(cyc_ext,axis = 0)

mode_data_AC2 = stat.mode(cyc_ext)
var_data_AC2 = stat.variance(cyc_ext)

counter = 0
cyc_ext = np.zeros(num_sim)

for j in range(0,num_sim):
    for i in range(0,num_cycles):
        if track_freq_025[j,i] == 0:
            cyc_ext[j] = i
            break

print(cyc_ext)

cyc_ext[cyc_ext == 0] = np.nan
mean_data_AC25 = np.nanmean(cyc_ext,axis = 0)
std_data_AC25 = np.nanstd(cyc_ext,axis = 0)
mode_data_AC25 = stat.mode(cyc_ext)
var_data_AC25 = stat.variance(cyc_ext)

x_values = [0.1,0.15,0.2,0.25]


fig,ax = plt.subplots()



plt.errorbar(x_values[0],mode_data_A1, var_data_A1 , linestyle='None', linewidth=2,capsize=4, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(x_values[0],mode_data_C1, var_data_C1 , linestyle='None', linewidth=2,capsize=4,marker='v', markersize=12,color = 'xkcd:bluish')
plt.errorbar(x_values[0],mode_data_AC1, var_data_AC1 , linestyle='None', linewidth=2,capsize=4,marker='d',markersize=8, color = 'xkcd:maize')
plt.errorbar(x_values[1],mode_data_A15, var_data_A15 , linestyle='None', linewidth=2,capsize=4, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(x_values[1],mode_data_C15, var_data_C15 , linestyle='None', linewidth=2,capsize=4,marker='v', markersize=12,color = 'xkcd:bluish')
plt.errorbar(x_values[1],mode_data_AC15, var_data_AC15 , linestyle='None', linewidth=2,capsize=4,marker='d',markersize=8, color = 'xkcd:maize')
plt.errorbar(x_values[2],mode_data_A2, var_data_A2 , linestyle='None', linewidth=2,capsize=4, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(x_values[2],mode_data_C2, var_data_C2 , linestyle='None', linewidth=2,capsize=4,marker='v', markersize=12,color = 'xkcd:bluish')
plt.errorbar(x_values[2],mode_data_AC2, var_data_AC2 , linestyle='None', linewidth=2,capsize=4,marker='d',markersize=8, color = 'xkcd:maize')
plt.errorbar(x_values[3],mode_data_A25, var_data_A25 , linestyle='None', linewidth=2,capsize=4, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(x_values[3],mode_data_C25, var_data_C25 , linestyle='None', linewidth=2,capsize=4,marker='v', markersize=12,color = 'xkcd:bluish')
plt.errorbar(x_values[3],mode_data_AC25, var_data_AC25 , linestyle='None', linewidth=2,capsize=4,marker='d',markersize=8, color = 'xkcd:maize')

plt.ylim(0,15)
plt.show()
