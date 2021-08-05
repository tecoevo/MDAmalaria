import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
import statistics as stat
import scipy
from scipy import stats

##### RANGE 1: 90 to 100 %


num_sim = 100
num_cycles = 15
num_scenarios = 11
data_all_scenarios = np.zeros((num_scenarios,num_sim))


#### atov

for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break

    print(cyc_ext)

    data_all_scenarios[m] = np.copy(cyc_ext)

print(data_all_scenarios)
data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_A1 = np.nanmean(data_all_scenarios,axis = 1)
std_data_A1 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_A1)

mode_data_A1 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_A1 = scipy.stats.tvar(data_all_scenarios,axis = 1)


###CHLO

for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m] = np.copy(cyc_ext)

print(data_all_scenarios)
data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_C1 = np.nanmean(data_all_scenarios,axis = 1)
std_data_C1 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_C1)


mode_data_C1 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_C1 = scipy.stats.tvar(data_all_scenarios,axis = 1)

#### ATOVCCHLO


for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m] = np.copy(cyc_ext)

print(data_all_scenarios)
data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_AC1 = np.nanmean(data_all_scenarios,axis = 1)
std_data_AC1 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_AC1)

mode_data_AC1 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_AC1 = scipy.stats.tvar(data_all_scenarios,axis = 1)



##### RANGE 2: 70 to 90 %


num_sim = 100
num_cycles = 15
num_scenarios = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim))


#### atov

for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m-11] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_A2 = np.nanmean(data_all_scenarios,axis = 1)
std_data_A2 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_A2)

mode_data_A2 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_A2 = scipy.stats.tvar(data_all_scenarios,axis = 1)

###CHLO

for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
                #cyc_ext[j] == np.copy(i)
    print(cyc_ext)

    data_all_scenarios[m-11] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_C2 = np.nanmean(data_all_scenarios,axis = 1)
std_data_C2 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_C2)
mode_data_C2 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_C2 = scipy.stats.tvar(data_all_scenarios,axis = 1)

#### ATOVCCHLO


for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m-11] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_AC2 = np.nanmean(data_all_scenarios,axis = 1)
std_data_AC2 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_AC2)
mode_data_AC2 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_AC2 = scipy.stats.tvar(data_all_scenarios,axis = 1)



##### RANGE 3: 50 to 70 (15-19) %


num_sim = 100
num_cycles = 30
num_scenarios = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim))


#### atov

for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m-15] = np.copy(cyc_ext)

print(data_all_scenarios)
data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_A3 = np.nanmean(data_all_scenarios,axis = 1)
std_data_A3 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_A3)
mode_data_A3 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_A3 = scipy.stats.tvar(data_all_scenarios,axis = 1)
###CHLO
num_cycles = 20
for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m-15] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_C3 = np.nanmean(data_all_scenarios,axis = 1)
std_data_C3 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_C3)
mode_data_C3 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_C3 = scipy.stats.tvar(data_all_scenarios,axis = 1)

#### ATOVCCHLO

num_cycles = 30
for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('Poolsize_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break
    print(cyc_ext)

    data_all_scenarios[m-15] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_AC3 = np.nanmean(data_all_scenarios,axis = 1)
std_data_AC3 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_AC3)
mode_data_AC3 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_AC3 = scipy.stats.tvar(data_all_scenarios,axis = 1)

#### RANGE 4: 10 to 50 (19-22) %


num_sim = 100
num_cycles = 100
num_scenarios = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim))


#### atov

for m in range(20,20+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('14OCT_A/Poolsize_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break

    print(cyc_ext)

    data_all_scenarios[m-20] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_A4 = np.nanmean(data_all_scenarios,axis = 1)
std_data_A4 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_A4)
mode_data_A4 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_A4 = scipy.stats.tvar(data_all_scenarios,axis = 1)
###CHLO
num_cycles = 100
for m in range(20,20+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('14OCT_C/Poolsize_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break

    print(cyc_ext)

    data_all_scenarios[m-20] = np.copy(cyc_ext)

print(data_all_scenarios)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_C4 = np.nanmean(data_all_scenarios,axis = 1)
std_data_C4 = np.nanstd(data_all_scenarios,axis = 1)
print(mean_data_C4)
mode_data_C4 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_C4 = scipy.stats.tvar(data_all_scenarios,axis = 1)

#### ATOVCCHLO

num_cycles = 100
for m in range(20,20+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_cycles+1))
    all_track_pool1 = glob.glob('14OCT_AC/Poolsize_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    mean_track_pool1 = np.nanmean(track_pool1, axis = 0)
    std_track_pool1 = np.nanstd(track_pool1, axis = 0)

    counter = 0
    cyc_ext = np.zeros(num_sim)

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if track_pool1[j,i] == 0:
                print('hey')
                print(i)
                cyc_ext[j] = i
                break

    print(cyc_ext)

    data_all_scenarios[m-20] = np.copy(cyc_ext)

data_all_scenarios[data_all_scenarios == 0] = np.nan
mean_data_AC4 = np.nanmean(data_all_scenarios,axis = 1)
std_data_AC4 = np.nanstd(data_all_scenarios,axis = 1)
mode_data_AC4 = scipy.stats.mode(data_all_scenarios,axis = 1)
var_data_AC4 = scipy.stats.tvar(data_all_scenarios,axis = 1)

m_values1 = np.linspace(90,100,11)
m_values2 = np.linspace(70,85,4)
m_values3 = np.linspace(50,65,4)
m_values4 = np.linspace(10,40,4)

fig,ax = plt.subplots()

plt.errorbar(m_values1,mean_data_A1, std_data_A1 , linestyle='None', linewidth=1,capsize=2, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(m_values1,mean_data_C1, std_data_C1 , linestyle='None', linewidth=1,capsize=2,marker='v', markersize=10,color = 'xkcd:bluish')
plt.errorbar(m_values1,mean_data_AC1, std_data_AC1 , linestyle='None', linewidth=1,capsize=2,marker='d', color = 'xkcd:maize')
plt.errorbar(m_values2,mean_data_A2, std_data_A2 , linestyle='None', linewidth=1,capsize=2,marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(m_values2,mean_data_C2, std_data_C2 , linestyle='None', linewidth=1,capsize=2,marker='v', markersize=10,color = 'xkcd:bluish')
plt.errorbar(m_values2,mean_data_AC2, std_data_AC2 , linestyle='None', linewidth=1,capsize=2,marker='d', color = 'xkcd:maize')
plt.errorbar(m_values3,mean_data_A3, std_data_A3 , linestyle='None', linewidth=1,capsize=2,marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(m_values3,mean_data_C3, std_data_C3 , linestyle='None', linewidth=1,capsize=2,marker='v',markersize=10, color = 'xkcd:bluish')
plt.errorbar(m_values3,mean_data_AC3, std_data_AC3 , linestyle='None',linewidth=1,capsize=2, marker='d', color = 'xkcd:maize')
plt.errorbar(m_values4,mean_data_A4, std_data_A4 , linestyle='None',linewidth=1,capsize=2, marker='o',markersize=12, color = 'xkcd:crimson')
plt.errorbar(m_values4,mean_data_C4, std_data_C4 , linestyle='None',linewidth=1,capsize=2, marker='v',markersize=10, color = 'xkcd:bluish')
plt.errorbar(m_values4,mean_data_AC4, std_data_AC4 , linestyle='None',linewidth=1,capsize=2, marker='d', color = 'xkcd:maize')

plt.show()
