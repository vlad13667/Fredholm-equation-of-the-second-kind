import numpy
import math
n=10
copyb=numpy.zeros(n)
copya=numpy.zeros((n,n))
B=numpy.zeros(n)
y = numpy.zeros((n,n))
a=0
b=math.pi/2
l=1
h=(b-a)/10
x=numpy.zeros((n))
def k(x,s):
    return(math.sin(x)*math.cos(s))

def f(x):
    return(1)
input_massiv_a = numpy.zeros((n,n)) #матрица коэфицентов
input_massiv_b = numpy.zeros((n)) #массив свободных членов
input_massiv_x = numpy.zeros((n)) #массив иксов
input_massiv_v = numpy.zeros((n)) # массив ответов
input_massiv_c = numpy.zeros((n,n)) #матрица коэфицентов копия
input_massiv_z = numpy.zeros([n]) #массив свободных членов копия

split = []
columcell = -1
rewcell = -1
gog = 0
value = 0 




def SearchMax(input_massiv_a): #поиск индекса максимального элимента
    global index
    cell = 0
    for i in range(value, n):
        for j in range(value, n):
          if (abs(input_massiv_a[i,j]) > cell):
                cell = abs(input_massiv_a[i,j])
                rewcell = i
                columcell = j
    index = numpy.array([rewcell,columcell])
    

def columc(input_massiv_a):#меняем местами столбцы
    input_massiv_a[:,[index[1],gog]] = input_massiv_a[:,[gog,index[1]]]
    r = input_massiv_x[gog]
    input_massiv_x[gog] = input_massiv_x[index[1]]
    input_massiv_x[index[1]] = r
    

    
    
    
def Row(input_massiv_a): #меняем местами строки
    input_massiv_a[[index[0],gog]] = input_massiv_a[[gog,index[0]]]
    input_massiv_b[[index[0],gog]] = input_massiv_b[[gog,index[0]]]
    
    
    
def One(input_massiv_a,input_massiv_b):#грубо говоря первый элемент становиться единицей
    num = input_massiv_a[gog,gog]
    for i in range(n):
        input_massiv_a[gog,i]= input_massiv_a[gog,i] / num 
    input_massiv_b[gog] = input_massiv_b[gog] / num
        

def zero(input_massiv_a,input_massiv_b):#грубо говоря делает 0 под еденицей
    for i in range(gog + 1,n):
        num = input_massiv_a[i,gog]
        for j in range(n):
            input_massiv_a[i,j]= input_massiv_a[i,j] / num - input_massiv_a[gog,j]
        input_massiv_b[i] = input_massiv_b[i] / num - input_massiv_b[gog]
    

def revers(input_massiv_a):# обратный ход для вычисления x
    for i in range (n-1,-1,-1):
        sum = input_massiv_b[i]
        for j in range(i+1,n):
            sum = sum - input_massiv_a[i,j] * input_massiv_v[j]
        input_massiv_v[i] = sum/input_massiv_a[i,i]

def CheckAnsver(input_massiv_a): # бональная проверка
            for i in range(n):
                sum = 0
                for j in range(n):
                    sum = sum + input_massiv_c[i,j] * input_massiv_v[j]
                sum = round(sum,2)
                    
                f.write( str(sum)+ '='+ str(input_massiv_z[i])+'\n')
           
def matrix(input_massiv_a,input_massiv_b):
    for i in range(value, n):
        for j in range(value, n):
            z = str(input_massiv_a[i,j])
            f.write(z+' ')  
        r = str(input_massiv_b[i])
        f.write('|'+ r +'\n')  


if __name__ == "__main__": 
    X=numpy.zeros((n))
    X[0]=a+h
    copyb[0]=B[0]=f(X[0])
    for i in range(1,n):
        X[i]=X[i-1]+h
        copyb[i] = B[i] = f(X[i])
                
    for i in range(n):
        for j in range(n):
            if (j > 0 and j < 9):
                copya[i, j] = y[i, j] = -l * h * k(X[i], X[j])
            else:
                copya[i, j] = y[i, j] = -0.5 * l * h * k(X[i], X[j])
            if (i == j):
                copya[i, j] = y[i, j] +1

    print(copya)
    for i in range(n):
        for  j in range (n):
            input_massiv_a [i,j] = copya[i,j]
            input_massiv_c [i,j] = copya[i,j]
            
        input_massiv_b[i] = copyb[i]
        input_massiv_z[i] = copyb[i]

    f = open('xyz.txt','a')  # открытие в режиме записи
    print('Исходная матрица')
    print(input_massiv_a)
    
    print('массив свободных членов')
    print(input_massiv_b)
    matrix(input_massiv_a,input_massiv_b)
    for i in range(n):
        input_massiv_x[i] =i+1
    for gog in range (n):
        SearchMax(input_massiv_a)
        Row(input_massiv_a)
        columc(input_massiv_a)
        One(input_massiv_a,input_massiv_b)
        zero(input_massiv_a,input_massiv_b)
        revers(input_massiv_a)
        
       
    
    for i in range(n):
        j = i
        while ((j<n-1) and (input_massiv_x[j]!= i+1)):
            j=j+1
        if (j != i):
            tem = input_massiv_x[i]
            temp = input_massiv_v[i]
            input_massiv_x[i] = input_massiv_x[j]
            input_massiv_v[i] = input_massiv_v[j]
            input_massiv_x[j] = tem
            input_massiv_v[j] = temp
        print("y" , input_massiv_x[i],  "=", input_massiv_v[i],)
        
        z = "y" + str(input_massiv_x[i])+  "="+ str(input_massiv_v[i])
        f.write(z +'\n')  
    CheckAnsver(input_massiv_a)









       



                
            




