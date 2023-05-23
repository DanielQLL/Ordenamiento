
import os
import matplotlib.pyplot as plt


ruta_carpeta = r"C:\Users\ASUS\Desktop\Practica-proyect\tiempos"

def extraer(a,len):
    ruta_completa=os.path.join(ruta_carpeta,f"tiempos_{a}_{len}.txt")
    archivo=open(ruta_completa,'r')
    txt=(archivo.read())
    n_txt=txt.split(',')
    num=[]
    for k in n_txt:
        n=float(k)
        num.append(n)
    archivo.close()
    return(num)

def separar(tip):
    numbers=[]
    datos=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
    bubble,counting,heap,insertion,merge,quick,selection=[],[],[],[],[],[],[]
    for i in datos:
        n_lis=extraer(tip,i)
        bubble.append(n_lis[0])
        counting.append(n_lis[1])
        heap.append(n_lis[2])
        insertion.append(n_lis[3])
        merge.append(n_lis[4])
        quick.append(n_lis[5])
        selection.append(n_lis[6])
    numbers.append(bubble)
    numbers.append(counting)        
    numbers.append(heap)        
    numbers.append(insertion)        
    numbers.append(merge)        
    numbers.append(quick)        
    numbers.append(selection)
    return(numbers)        
        

    
datos=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
algo=["Bubble","Counting","Heap","Insertion","Merge","Quick","Selection"]
data_python=separar("python")
data_cpp=separar("cpp")
for i in range(7):
    fig,ax=plt.subplots(figsize=(8, 6))
    tempos={'C++':data_cpp[i],'Python':data_python[i]}
    ax.plot(range(len(datos)),tempos['Python'],color='tab:purple',label='Python')
    ax.plot(range(len(datos)),tempos['C++'],color='tab:green',label='C++')
    ax.legend(loc = 'upper left')
    ax.set_xticks(range(len(datos)))
    ax.set_xticklabels([str(x) for x in datos])
    ax.tick_params(axis='x',rotation=70)
    ax.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
    ax.set_ylabel("Tiempo (s)")
    ax.set_xlabel("Numero de datos")
    ax.set_title(f'Tiempo de ejecución de {algo[i]}Sort en Python y C++', loc = "center")
    plt.tight_layout()
    plt.show()
    fig.savefig(r"C:\Users\ASUS\Desktop\Practica-proyect\graficas\grafica_"+algo[i]+".pdf", bbox_inches='tight', pad_inches=0.3, dpi=900)


fig,ay=plt.subplots(figsize=(8, 6))
tempos_py={'Bubble':data_python[0],'Counting':data_python[1],'Heap':data_python[2],'Insertion':data_python[3],'Merge':data_python[4],'Quick':data_python[5],'Selection':data_python[6]}
ay.plot(range(len(datos)),tempos_py['Bubble'],color='tab:purple',label='Bubble')
ay.plot(range(len(datos)),tempos_py['Counting'],color='tab:green',label='Counting')
ay.plot(range(len(datos)),tempos_py['Heap'],color='tab:blue',label='Heap')
ay.plot(range(len(datos)),tempos_py['Insertion'],color='tab:orange',label='Insertion')
ay.plot(range(len(datos)),tempos_py['Merge'],color='tab:red',label='Merge')
ay.plot(range(len(datos)),tempos_py['Quick'],color='tab:brown',label='Quick')
ay.plot(range(len(datos)),tempos_py['Selection'],color='tab:pink',label='Selection')
ay.legend(loc = 'upper left')
ay.set_xticks(range(len(datos)))
ay.set_xticklabels([str(x) for x in datos])
ay.tick_params(axis='x',rotation=70)
ay.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
ay.set_ylabel("Tiempo (s)")
ay.set_xlabel("Numero de datos")
ay.set_title('Comparacion de los algoritmos de ordenamiento en Python.', loc = "center")
plt.tight_layout()
plt.show()
fig.savefig(r"C:\Users\ASUS\Desktop\Practica-proyect\graficas\grafico_python.pdf", bbox_inches='tight', pad_inches=0.3, dpi=900)

fig,az=plt.subplots(figsize=(8, 6))
tempos_cpp={'Bubble':data_cpp[0],'Counting':data_cpp[1],'Heap':data_cpp[2],'Insertion':data_cpp[3],'Merge':data_cpp[4],'Quick':data_cpp[5],'Selection':data_cpp[6]}
az.plot(range(len(datos)),tempos_cpp['Bubble'],color='tab:purple',label='Bubble')
az.plot(range(len(datos)),tempos_cpp['Counting'],color='tab:green',label='Counting')
az.plot(range(len(datos)),tempos_cpp['Heap'],color='tab:blue',label='Heap')
az.plot(range(len(datos)),tempos_cpp['Insertion'],color='tab:orange',label='Insertion')
az.plot(range(len(datos)),tempos_cpp['Merge'],color='tab:red',label='Merge')
az.plot(range(len(datos)),tempos_cpp['Quick'],color='tab:brown',label='Quick')
az.plot(range(len(datos)),tempos_cpp['Selection'],color='tab:pink',label='Selection')
az.legend(loc = 'upper left')
az.set_xticks(range(len(datos)))
az.set_xticklabels([str(x) for x in datos])
az.tick_params(axis='x',rotation=70)
az.grid(axis = 'y', color = 'gray', linestyle = 'dashed')
az.set_ylabel("Tiempo (s)")
az.set_xlabel("Numero de Datos")
az.set_title('Comparacion de los algoritmos de ordenamiento en C++.', loc = "center")
plt.tight_layout()
plt.show()
fig.savefig(r"C:\Users\ASUS\Desktop\Practica-proyect\graficas\grafico_C++.pdf", bbox_inches='tight', pad_inches=0.3, dpi=900)