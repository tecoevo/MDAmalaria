import numpy as np
import matplotlib.pyplot as plt
import glob
import pandas as pd
from scipy import stats
import matplotlib.cm as cm

track_all_binary_A = np.zeros((23,4))
track_all_binary_C = np.zeros((23,4))
track_all_binary_AC = np.zeros((23,4))

##### PLOT TYPE (SI) GENOTYPE AT TIME OF INTERRUPTION

##### RANGE 1: 90 to 100 %


num_sim = 100
num_cycles = 15
num_scenarios = 11
num_gen = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim,num_gen))


#### ATOVAQUONE

mode_scenario_A1 = np.zeros((num_scenarios,num_gen))
for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)


    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T
#
    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_A1[m] = stats.mode(track_freq_ext)[0]

print(mode_scenario_A1)
track_all_binary_A[12:23,:] = np.copy(mode_scenario_A1)

###CHLOROQUINE


mode_scenario_C1 = np.zeros((num_scenarios,num_gen))
for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:

                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_C1[m] = stats.mode(track_freq_ext)[0]

print(mode_scenario_C1)
track_all_binary_C[12:23,:] = np.copy(mode_scenario_C1)

#### ATOVAQUONE AND CHLOROQUINE

mode_scenario_AC1 = np.zeros((num_scenarios,num_gen))
for m in range(0,num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)


    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_AC1[m] = stats.mode(track_freq_ext)[0]

print(mode_scenario_AC1)

track_all_binary_AC[12:23,:] = np.copy(mode_scenario_AC1)


##### RANGE 2: 70 to 90 %


num_sim = 100
num_cycles = 15
num_scenarios = 4
num_gen = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim,num_gen))


#### ATOVAQUONE

mode_scenario_A1 = np.zeros((num_scenarios,num_gen))
for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_A1[m-11] = stats.mode(track_freq_ext)[0]

print(mode_scenario_A1)
track_all_binary_A[8:12,:] = np.copy(mode_scenario_A1)

### CHLOROQUINE

mode_scenario_C1 = np.zeros((num_scenarios,num_gen))
for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T


    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_C1[m-11] = stats.mode(track_freq_ext)[0]

print(mode_scenario_C1)
track_all_binary_C[8:12,:] = np.copy(mode_scenario_C1)

#### ATOV and CHLO

mode_scenario_AC1 = np.zeros((num_scenarios,num_gen))
for m in range(11,11+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_AC1[m-11] = stats.mode(track_freq_ext)[0]

print(mode_scenario_AC1)
track_all_binary_AC[8:12,:] = np.copy(mode_scenario_AC1)



##### RANGE 3: 50 to 70 (15-19) %


num_sim = 100
num_cycles = 20
num_scenarios = 4
num_gen = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim,num_gen))


#### ATOVAQUONE

mode_scenario_A1 = np.zeros((num_scenarios,num_gen))
for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_A1[m-15] = stats.mode(track_freq_ext)[0]

print(mode_scenario_A1)
track_all_binary_A[4:8,:] = np.copy(mode_scenario_A1)

### CHLOROQUINE

mode_scenario_C1 = np.zeros((num_scenarios,num_gen))
for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_C1[m-15] = stats.mode(track_freq_ext)[0]

print(mode_scenario_C1)
track_all_binary_C[4:8,:] = np.copy(mode_scenario_C1)

#### ATOV and CHLOROQUINE

mode_scenario_AC1 = np.zeros((num_scenarios,num_gen))
for m in range(15,15+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_AC1[m-15] = stats.mode(track_freq_ext)[0]

print(mode_scenario_AC1)
track_all_binary_AC[4:8,:] = np.copy(mode_scenario_AC1)

#### RANGE 4: 10 to 50 (19-22) %


num_sim = 100
num_cycles = 60
num_scenarios = 4
num_gen = 4
data_all_scenarios = np.zeros((num_scenarios,num_sim,num_gen))


#### ATOVAQUONE

mode_scenario_A1 = np.zeros((num_scenarios,num_gen))
for m in range(19,19+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_A_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_A1[m-19] = stats.mode(track_freq_ext)[0]

print(mode_scenario_A1)
track_all_binary_A[0:4,:] = np.copy(mode_scenario_A1)

### CHLOROQUINE

mode_scenario_C1 = np.zeros((num_scenarios,num_gen))
for m in range(19,19+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_C_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)

    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:

                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break

    mode_scenario_C1[m-19] = stats.mode(track_freq_ext)[0]

print(mode_scenario_C1)
track_all_binary_C[0:4,:] = np.copy(mode_scenario_C1)

#### ATOV and CHLOROQUINE

mode_scenario_AC1 = np.zeros((num_scenarios,num_gen))
for m in range(19,19+num_scenarios):

    track_pool1 = np.zeros((num_sim,num_gen,num_cycles+1))
    all_track_pool1 = glob.glob('Freq_AC_*_{0}.csv'.format(m))

    list_data_NP1 = []
    #
    for filename in all_track_pool1:
         data_NP1 = pd.read_csv(filename,header=None)
         list_data_NP1.append(data_NP1)

    pd.concat(list_data_NP1,ignore_index=True)


    for i in range(0,num_sim):
        track_pool1[[i],:,:] = list_data_NP1[i].iloc[0:num_cycles+1].T

    counter = 0
    cyc_ext = np.zeros(num_sim)
    track_freq_ext = np.zeros((num_sim,num_gen))

    for j in range(0,num_sim):
        for i in range(0,num_cycles):
            if np.sum(track_pool1[j,:,i]) == 0:
                cyc_ext[j] = i
                track_freq_ext[j] = track_pool1[j,:,i-1]
                break
    mode_scenario_AC1[m-19] = stats.mode(track_freq_ext)[0]

print(mode_scenario_AC1)
track_all_binary_AC[0:4,:] = np.copy(mode_scenario_AC1)

print(track_all_binary_A)

fig, ax = plt.subplots()
im = ax.pcolormesh(track_all_binary_A.T, cmap=cm.binary, edgecolors='white', linewidths=1,
                   antialiased=True)
fig.colorbar(im)


plt.show()

fig, ax = plt.subplots()
im = ax.pcolormesh(track_all_binary_C.T, cmap=cm.binary, edgecolors='white', linewidths=1,
                   antialiased=True)
fig.colorbar(im)
plt.show()
fig, ax = plt.subplots()
im = ax.pcolormesh(track_all_binary_AC.T, cmap=cm.binary, edgecolors='white', linewidths=1,
                   antialiased=True)
fig.colorbar(im)
plt.show()
