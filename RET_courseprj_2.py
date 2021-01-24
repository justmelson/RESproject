# -*- coding: utf-8 -*-
"""
Created on Mon Nov 23 15:50:38 2020

@author: justm
"""
import matplotlib.pyplot as plt
import numpy as np

co2_limit = [250, 500, 1000, 2000, 4000, 6000, 'no limit'] #tonCO2

co2={}

co2[0]=[15000,
        4804,
        7439,
        11480,
        5240,
        9631]

# 500000 ton
co2[1]=[15000,
        2475,
        7439,
        7081,
        6861,
        8238]

# 1000000 ton
co2[2]=[15000,
        2194,
        7439,
        6298,
        8949,
        6198]

# 2000000 ton
co2[3]=[15000,
        2233,
        7439,
        7592,
        11176,
        3964]

# 4000000 ton
co2[4]=[15000,
        3191,
        7439,
        10843,
        13927,
        1049]

# 6000000 ton
co2[5]=[15000,
        1187,
        7439,
        11641,
        15320,
        0]


# no constraint
co2[6]=[15000,
        0,
        7439,
        6288,
        15531,
        0]

onshore={}
offshorewind={}
hydro={}
solar={}
OCGT={}
NUCL={}


for i in range(7):
    onshore[i]=co2[i][0]
    offshorewind[i]=co2[i][1]
    hydro[i]=co2[i][2]
    solar[i]=co2[i][3]
    OCGT[i]=co2[i][4]
    NUCL[i]=co2[i][5]

onshore=list(onshore.values())
offshorewind=list(offshorewind.values())
hydro=list(hydro.values())
solar=list(solar.values())
OCGT=list(OCGT.values())
NUCL=list(NUCL.values())

#labels = ['onshore wind','offshore wind','solar', 'gas (OCGT)', 'nuclear (NUCL)','hydro' ]



# Heights of bars1 + bars2
bars1 = np.add(onshore, offshorewind).tolist()
bars2 = np.add(bars1, hydro).tolist()
bars3 = np.add(bars2, solar).tolist()
bars4 = np.add(bars3, OCGT).tolist()

# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6]
 
# Names of group and bar width
names = ['a','B','C','2','3','4','5']

barWidth = 0.5
plt.figure(1)
plt.figure(dpi=1200)
# onshore
plt.bar(r, onshore, color='blue', width=barWidth, label = 'Onshore')
# offshore
plt.bar(r, offshorewind, bottom=onshore, color='red', width=barWidth, label = 'Offshore')
# hydro
plt.bar(r, hydro, bottom=bars1, color='cyan', width=barWidth, label ='Hydro')
# solar
plt.bar(r, solar, bottom=bars2, color='orange', width=barWidth, label='Solar')
# OCGT
plt.bar(r, OCGT, bottom=bars3, color='brown', width=barWidth, label='OCGT')
# NUCL
plt.bar(r, NUCL, bottom=bars4, color='green', width=barWidth, label='NUCL')



# Custom X axis
plt.xticks(r, co2_limit)
plt.xlabel("CO2 limit in ton (1000s)")
plt.ylabel('Optimal capacities [MWh]')
plt.legend(loc='best')


"""
Interannual variability
"""


year={}



# 2002
year[0]=[15000,
        0,
        7439,
        9087,
        11401,
        3722]

# 2005
year[1]=[15000,
        0,
        7439,
        10485,
        11422,
        3587]


# 2007
year[2]=[15000,
        0,
        7439,
        9902,
        11703,
        3648]


# 2010
year[3]=[15000,
        0,
        7439,
        10031,
        10748,
        4071]


# 2013
year[4]=[15000,
        0,
        7439,
        10198,
        11236,
        3893]


# 2015
year[5]=[15000,
        2483,
        7439,
        9276,
        12552,
        2546]

# 2017
year[6]=[15000,
        2256,
        7439,
        9556,
        11112,
        3011]


onshore={}
offshorewind={}
hydro={}
solar={}
OCGT={}
NUCL={}


for i in range(7):
    onshore[i]=year[i][0]
    offshorewind[i]=year[i][1]
    hydro[i]=year[i][2]
    solar[i]=year[i][3]
    OCGT[i]=year[i][4]
    NUCL[i]=year[i][5]

onshore=list(onshore.values())
offshorewind=list(offshorewind.values())
hydro=list(hydro.values())
solar=list(solar.values())
OCGT=list(OCGT.values())
NUCL=list(NUCL.values())


# Heights of bars1 + bars2
bars1 = np.add(onshore, offshorewind).tolist()
bars2 = np.add(bars1, hydro).tolist()
bars3 = np.add(bars2, solar).tolist()
bars4 = np.add(bars3, OCGT).tolist()

# The position of the bars on the x-axis
r = [0,1,2,3,4,5,6]
 
# Names of group and bar width
names = ['a','B','C','2','3','4','5']

barWidth = 0.5
plt.figure(1)
plt.figure(dpi=1200)
# onshore
plt.bar(r, onshore, color='blue', width=barWidth, label = 'Onshore')
# offshore
plt.bar(r, offshorewind, bottom=onshore, color='red', width=barWidth, label = 'Offshore')
# hydro
plt.bar(r, hydro, bottom=bars1, color='cyan', width=barWidth, label ='Hydro')
# solar
plt.bar(r, solar, bottom=bars2, color='orange', width=barWidth, label='Solar')
# OCGT
plt.bar(r, OCGT, bottom=bars3, color='brown', width=barWidth, label='OCGT')
# NUCL
plt.bar(r, NUCL, bottom=bars4, color='green', width=barWidth, label='NUCL')

Weather_year = [2002, 2005, 2007, 2010, 2013, 2015, 2017]

# Custom X axis
plt.xticks(r, Weather_year)
plt.xlabel("Year of recorded weather data")
plt.ylabel('Optimal capacities [MWh]')
plt.legend(loc='lower left')
