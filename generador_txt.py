import os
from random import randint
num_datos=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]

ruta_carpeta=r"C:\Users\ASUS\Desktop\Practica-proyect\Listas"

if not os.path.exists(ruta_carpeta):
    os.makedirs(ruta_carpeta)

for i in num_datos:
    num=[]
    for j in range (i):
        n=randint(0,99)
        num.append(n)
    nw_str=str(num)[1:-1]
    ruta_completa=os.path.join(ruta_carpeta, f"lista_de_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{nw_str}")
    file.close()