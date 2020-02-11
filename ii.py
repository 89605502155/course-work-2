import numpy as np
import pandas as pd
import tensorly as tl
import os
y =pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/y.txt', sep= '\t')
y =  y.fillna(0)
y = y.replace(',','.', regex=True)
cols = ["Pahokee peat","Nordic aquatic","Suwanee river","Elliot soil","Disser"]
y = y.eval('Gominy=Pahokee peat+Nordic aquatic', inplace=True)
print(y)
fds = sorted(os.listdir('C:/Users/admin/Desktop/курсовая 2.0/X — копия/')) #формируем список файлов для считывания в цикле
print(fds)
k = 0

while k < 35:
    dataset = pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/X — копия/'+fds[k],sep='\t')
    dataset = dataset.fillna(0)
    k = k + 1
    print()
    print()
    print(k)
    print()
