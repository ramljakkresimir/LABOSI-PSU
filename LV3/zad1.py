import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

mtcars = pd.read_csv('mtcars.csv')
print("-----------------------------------------------------------------------------------")
print("\n1. Kojih 5 automobila ima najveću potrošnju? \n",mtcars.sort_values(by=['mpg']).tail(5))
print("-----------------------------------------------------------------------------------")
cyl8=mtcars[mtcars.cyl==8]

print("\n2. Koja tri automobila s 8 cilindara imaju najmanju potrošnju?\n",cyl8.sort_values(by=['mpg']).head(3))
print("-----------------------------------------------------------------------------------")
cyl6=mtcars[mtcars.cyl==6]

print("\n3. Kolika je srednja potrošnja automobila sa 6 cilindara?",cyl6['mpg'].mean())
print("-----------------------------------------------------------------------------------")
cyl4m2000 = mtcars[(mtcars.cyl==4) & (mtcars.wt>=2) & (mtcars.wt<=2.2)]
print("\n4. Kolika je srednja potrošnja automobila s 4 cilindra mase između 2000 i 2200 lbs?",cyl4m2000['mpg'].mean())
print("-----------------------------------------------------------------------------------")
print("5. Koliko je automobila s ručnim, a koliko s automatskim mjenjačem u ovom skupu podataka?")
gearboxType = mtcars.groupby('am').car
print(gearboxType.count())
print("-----------------------------------------------------------------------------------")
am_hp100 = mtcars[(mtcars.am==1) & (mtcars.hp > 100)]
print("\n6. Koliko je automobila s automatskim mjenjačem i snagom preko 100 konjskih snaga?",len(am_hp100))
print("-----------------------------------------------------------------------------------")
masa = round(mtcars.wt*1000/0.45359237,2)
print("\n7. Kolika je masa svakog automobila u kilogramima?")
print(masa)