#include <iostream>
#include <fstream>
#include <sstream>
#include <ctime>
#include <algorithm>
#include <iomanip>
#include <chrono>




using namespace std;
using namespace std::chrono;


void imprimir(int array[],int size){
	for (int k = 0; k < size; k++) {
    	cout << array[k] << " ";
    }
	
}
	
int* extraer(int len) {
	string nombre_archivo= "C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_de_" +to_string(len)+ ".txt";
    ifstream archivo(nombre_archivo);
    string txt, line;
    while (getline(archivo, line)) {
        txt += line;
    }
    archivo.close();
    stringstream ss(txt);
    string num_str;
    int* num = new int[len];
    int i = 0;
    while (getline(ss, num_str, ',')) {
        int n = stoi(num_str);
        num[i++] = n;
    }
    return num;
}

void bubbleSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        for (int j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                swap(arr[j], arr[j + 1]);
            }
        }
    }
}

int* countingSort(int array[], int size) {
    int max_val = *max_element(array, array + size);
    int* count = new int[max_val + 1]{0};
    for (int i = 0; i < size; i++) {
        count[array[i]]++;
    }
    for (int i = 1; i <= max_val; i++) {
        count[i] += count[i - 1];
    }
    int* output = new int[size];
    for (int i = size - 1; i >= 0; i--) {
        output[count[array[i]] - 1] = array[i];
        count[array[i]]--;
    }
    delete[] count;
    return output;
}


void swap(int& a, int& b) {
    int temp = a;
    a = b;
    b = temp;
}

void heapify(int array[], int n, int i) {
    int largest = i; 
    int left = 2 * i + 1;
    int right = 2 * i + 2;

    if (left < n && array[left] > array[largest])
        largest = left;

    if (right < n && array[right] > array[largest])
        largest = right;

    if (largest != i) {
        swap(array[i], array[largest]);

        heapify(array, n, largest);
    }
}

void heapSort(int array[], int n) {
    for (int i = n / 2 - 1; i >= 0; i--)
        heapify(array, n, i);

    for (int i = n - 1; i >= 0; i--) {
        // Mover la raíz actual al final
        swap(array[0], array[i]);

        heapify(array, i, 0);
    }
}


void insertionSort(int array[], int n) {
    for (int i = 1; i < n; ++i) {
        int key = array[i];
        int j = i - 1;

        while (j >= 0 && array[j] > key) {
            array[j + 1] = array[j];
            j = j - 1;
        }
        array[j + 1] = key;
    }
}


void merge(int arr[], int left[], int leftSize, int right[], int rightSize) {
    int i = 0, j = 0, k = 0;

    while (i < leftSize && j < rightSize) {
        if (left[i] <= right[j]) {
            arr[k] = left[i];
            i++;
        } else {
            arr[k] = right[j];
            j++;
        }
        k++;
    }

    while (i < leftSize) {
        arr[k] = left[i];
        i++;
        k++;
    }

    while (j < rightSize) {
        arr[k] = right[j];
        j++;
        k++;
    }
}

void mergeSort(int arr[], int size) {
    if (size < 2) {
        return;
    }

    int mid = size / 2;
    int left[mid];
    int right[size - mid];

    for (int i = 0; i < mid; i++) {
        left[i] = arr[i];
    }

    for (int i = mid; i < size; i++) {
        right[i - mid] = arr[i];
    }

    mergeSort(left, mid);
    mergeSort(right, size - mid);
    merge(arr, left, mid, right, size - mid);
}


int partition(int arr[], int low, int high) {
    int pivot = arr[high];
    int i = low - 1;

    for (int j = low; j <= high - 1; j++) {
        if (arr[j] < pivot) {
            i++;
            std::swap(arr[i], arr[j]);
        }
    }

    std::swap(arr[i + 1], arr[high]);
    return (i + 1);
}

void quickSort(int arr[], int low, int high) {
    if (low < high) {
        int pi = partition(arr, low, high);

        quickSort(arr, low, pi - 1);
        quickSort(arr, pi + 1, high);
    }
}

void selectionSort(int arr[], int size) {
    for (int i = 0; i < size - 1; i++) {
        int minIndex = i;

        for (int j = i + 1; j < size; j++) {
            if (arr[j] < arr[minIndex]) {
                minIndex = j;
            }
        }

        swap(arr[i], arr[minIndex]);
    }
}



int main(){

    int num_datos[] = {100, 500, 1000, 2000, 3000, 4000, 5000, 6000, 7000, 8000, 9000, 10000, 20000, 30000, 40000, 50000, 60000, 70000, 80000, 90000, 100000};
	int size_datos= sizeof(num_datos) / sizeof(num_datos[0]);
	
    for (int i = 0; i < size_datos; i++) {
		int len = num_datos[i];
		int copia[len];
        double time_dat[7] = {0.0};
        int* arr = extraer(len);
        
        
    	copy(arr, arr + len, copia);
        auto inicio1 = high_resolution_clock::now();
        bubbleSort(copia, len);
        auto fin1 = high_resolution_clock::now();
        ofstream file1("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_bubble_cpp_" + to_string(len) + ".txt");
        for (int j = 0; j < len; j++) {
            file1 << copia[j] << ",";
        }
        file1.close();
       	auto r1= duration_cast<microseconds>(fin1 - inicio1).count()/1000000.0;

    	
    	
    	copy(arr, arr + len, copia);
        auto inicio2 = high_resolution_clock::now();
    	int* counting = countingSort(copia, len); 
        auto fin2 = high_resolution_clock::now();
        ofstream file2("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_counting_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file2 << counting[j] << ",";
        }
        file2.close();
       	auto r2= duration_cast<nanoseconds>(fin2 - inicio2).count()/1e9;


	    copy(arr, arr + len, copia);
        auto inicio3 = high_resolution_clock::now();	    
    	heapSort(copia,len);
        auto fin3 = high_resolution_clock::now();
   		ofstream file3("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_heap_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file3 << copia[j] << ",";
        }
        file3.close();
       	auto r3= duration_cast<microseconds>(fin3 - inicio3).count()/1000000.0;
    	
    	
    	copy(arr, arr + len, copia); 
        auto inicio4 = high_resolution_clock::now();	    
    	insertionSort(copia,len);
        auto fin4 = high_resolution_clock::now();
        ofstream file4("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_insertion_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file4 << copia[j] << ",";
        }
        file4.close();
       	auto r4= duration_cast<microseconds>(fin4 - inicio4).count()/1000000.0;
       	
       	
    	copy(arr, arr + len, copia);  
        auto inicio5 = high_resolution_clock::now();	    
		mergeSort(copia,len);
        auto fin5 = high_resolution_clock::now();
		ofstream file5("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_merge_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file5 << copia[j] << ",";
        }
        file5.close();
       	auto r5= duration_cast<microseconds>(fin5 - inicio5).count()/1000000.0;


    	copy(arr, arr + len, copia);
        auto inicio6 = high_resolution_clock::now();	     
		quickSort(copia,0,len-1);
        auto fin6 = high_resolution_clock::now();
		ofstream file6("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_quick_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file6 << copia[j] << ",";
        }
        file6.close();
       	auto r6= duration_cast<microseconds>(fin6 - inicio6).count()/1000000.0;
		
		  
		copy(arr, arr + len, copia);
        auto inicio7 = high_resolution_clock::now();	     
		selectionSort(copia,len);
        auto fin7 = high_resolution_clock::now();
		ofstream file7("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\Listas\\lista_selection_cpp_" + to_string(len) + ".txt");
		for (int j = 0; j < len; j++) {
            file7 << copia[j] << ",";
        }
        file7.close();
       	auto r7= duration_cast<microseconds>(fin7 - inicio7).count()/1000000.0;
        
        
        time_dat[0] = double(r1) ;
        time_dat[1] = double(r2);
        time_dat[2] = double(r3);
        time_dat[3] = double(r4);
        time_dat[4] = double(r5);
        time_dat[5] = double(r6);
        time_dat[6] = double(r7);

        ofstream file8("C:\\Users\\ASUS\\Desktop\\Practica-proyect\\tiempos\\tiempos_cpp_" + to_string(len) + ".txt");
        for (int j = 0; j < 7; j++) {
        	if (j<6){
            	file8<< setprecision(15)<<time_dat[j] << ",";
			}
			else{
				file8<< setprecision(15)<<time_dat[j];
			}
			
        }
        file8.close();
        delete[] arr;
	}
	

	return 0;
}
