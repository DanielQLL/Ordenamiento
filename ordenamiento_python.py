import os
import sys
import time
ruta_carpeta = r"C:\Users\ASUS\Desktop\Practica-proyect\Listas"
ruta_carpeta_tiempos=r"C:\Users\ASUS\Desktop\Practica-proyect\tiempos"

def extraer(len):
    ruta_completa=os.path.join(ruta_carpeta,f"lista_de_{len}.txt")
    archivo=open(ruta_completa,'r')
    txt=(archivo.read())
    n_txt=txt.split(',')
    num=[]
    for k in n_txt:
        n=int(k)
        num.append(n)
    archivo.close()
    return(num)
    
def bubbleSort(array):
    arra = array.copy()
    for i in range(len(arra) - 1):
        for j in range(len(arra) - i - 1):
            if arra[j] > arra[j+1]:
                arra[j], arra[j+1] = arra[j+1], arra[j]
    return arra

def counting_sort(array):
    max_val = max(array)
    count = [0] * (max_val + 1)
    for val in array:
        count[val] += 1
    for i in range(1, max_val + 1):
        count[i] += count[i - 1]
    output = [0] * len(array)
    for val in array:
        output[count[val] - 1] = val
        count[val] -= 1
    return output

def heapify(arra, n, i):
    largest = i
    l = 2 * i + 1
    r = 2 * i + 2
    if l < n and arra[i] < arra[l]:
        largest = l  
    if r < n and arra[largest] < arra[r]:
        largest = r  
    if largest != i:
        arra[i],arra[largest] = arra[largest],arra[i]
        heapify(arra, n, largest)
  
def heap_sort(array):
    arra = array.copy()
    n = len(arra)  
    for i in range(n // 2 - 1, -1, -1):
        heapify(arra, n, i)  
    for i in range(n-1, 0, -1):
        arra[i], arra[0] = arra[0], arra[i]   
        heapify(arra, i, 0)       
    return arra

def insertion_sort(array):
    arra = array.copy()
    for i in range(1, len(arra)):
        key = arra[i]
        j = i - 1
        while j >= 0 and key < arra[j]:
            arra[j + 1] = arra[j]
            j -= 1
        arra[j + 1] = key
    return(arra)

def merge_sort(array):
    if len(array) > 1:
        mid = len(array) // 2
        left_half = array[:mid]
        right_half = array[mid:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = j = k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] < right_half[j]:
                array[k] = left_half[i]
                i += 1
            else:
                array[k] = right_half[j]
                j += 1
            k += 1
        while i < len(left_half):
            array[k] = left_half[i]
            i += 1
            k += 1
        while j < len(right_half):
            array[k] = right_half[j]
            j += 1
            k += 1
    return(array)

def partition(array, low, high):
  pivot = array[high]
  i = low - 1
  for j in range(low, high):
    if array[j] <= pivot:
      i = i + 1
      (array[i], array[j]) = (array[j], array[i]) 
  (array[i + 1], array[high]) = (array[high], array[i + 1]) 
  return i + 1
 
def quick_sort(array, low, high):
  if low < high:
    pi = partition(array, low, high)
    quick_sort(array, low, pi - 1)
    quick_sort(array, pi + 1, high)
  return array

def selection_sort(array):
    arra=array.copy()
    for i in range(len(arra)):
        min_idx = i
        for j in range(i+1, len(arra)):
            if arra[j] < arra[min_idx]:
                min_idx = j
        arra[i], arra[min_idx] = arra[min_idx], arra[i]
    return(arra)
    
num_datos=[100,500,1000,2000,3000,4000,5000,6000,7000,8000,9000,10000,20000,30000,40000,50000,60000,70000,80000,90000,100000]
sys.setrecursionlimit(2000)
for i in num_datos:
    time_dat=[]
    #Utilizamos esta funcion para extraer los archivos txt y con vertirlos en listas de numeros enteros
    lista=extraer(i)


    a1=time.time()
    bubble=bubbleSort(lista)
    b1=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_buble_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{bubble}")
    file.close()


    a2=time.time()
    counting=counting_sort(lista)
    b2=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_couting_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{counting}")
    file.close()
    

    a3=time.time()
    heap=heap_sort(lista)
    b3=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_heap_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{heap}")
    file.close()


    a4=time.time()
    insertion=insertion_sort(lista)
    b4=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_insertion_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{insertion}")
    file.close()


    array=lista.copy()
    a5=time.time()
    marge=merge_sort(array)
    b5=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_marge_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{marge}")
    file.close()

    lis_nw=lista.copy()
    a6=time.time()
    quick=quick_sort(lis_nw,0,len(lis_nw)-1)
    b6=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_quick_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{quick}")
    file.close()

    a7=time.time()
    selection=selection_sort(lista)
    b7=time.time()
    ruta_completa=os.path.join(ruta_carpeta, f"lista_selection_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{selection}")
    file.close()


    time_dat.append(b1-a1)
    time_dat.append(b2-a2)
    time_dat.append(b3-a3)
    time_dat.append(b4-a4)
    time_dat.append(b5-a5)
    time_dat.append(b6-a6)
    time_dat.append(b7-a7)
    time_datos=str(time_dat)[1:-1]
    ruta_completa=os.path.join(ruta_carpeta_tiempos, f"tiempos_python_{i}.txt")
    file=open(ruta_completa,"x")
    file.write(f"{time_datos}")
    file.close()



