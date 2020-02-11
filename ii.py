import numpy as np
import pandas as pd
import tensorly as tl
import os
y =pd.read_csv('C:/Users/admin/Desktop/курсовая 2.0/y.txt', sep= '\t')
y =  y.fillna(0) #заменяю Nan на 0
y = y.replace(',','.', regex=True) #меняю ',' на '.'
y = y.astype(float) #конвертирую из string в float
y=y.assign(Gominy=y[["Pahokee peat","Nordic aquatic","Suwanee river","Elliot soil","Disser"]].sum(1)) #складываю столбцы
pd.set_option('display.float_format', '{:.15f}'.format) #контроль длинны вывода float
print(y)
fds = sorted(os.listdir('C:/Users/admin/Desktop/курсовая 2.0/X — копия/')) #формируем список файлов x для считывания в цикле
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
