#python -u index.py
#TODO Python 

import sys
import math

Number1 = int(sys.argv[1])
Number2 = int(sys.argv[2])
char = 'dasdasdas'

print(len(char))
print(f'{Number1} + {Number2} = {Number1 + Number2}\n')
print(f'{Number1} - {Number2} = {Number1 - Number2}\n')
print(f'{Number1} * {Number2} = {Number1 * Number2}\n')
print(f'{Number1} // {Number2} = {Number1 // Number2}\n')
print(f'{Number1} % {Number2} = {Number1 % Number2}\n')
print(f'{Number1} ** {Number2} = {Number1 ** Number2}\n')

#------ Math 
print(f'{Number1} sqrt = {math.sqrt(Number1)}\n')
print(f'{Number1} sin = {math.sin(Number1)}\n')
print(f'{Number1} cos = {math.cos(Number1)}\n')

bool1 = True
bool2 = False
print(bool1 or bool2)
print(1 == 2)
print(1 >= 2)
print(1 != 2)
print(1 <= 2)
i = 1
while True :
    i += 1
print(i)
















'''
Number = int(input("Pleas Enter The Number : "))

Sum,Avg = 0,None 

while Number > 0 :
    Avg = Number % 10    
    Sum = Sum * 10 + Avg
    Number = int(Number/10)

print(f"You Are Number Is {Sum} .")




int ArrayMe[8] = {11,22,33,12,77,23,32,11};
int boolar;

for(int i = 0; i<8 ; i++){
    for (int j = 0 ; j<8 ; j++){
        if(i!=j && ArrayMe[i]==ArrayMe[j]){boolar = 1;}
    } 
    if(boolar == 1){
        cout<<"This Number: "<<ArrayMe[i]<<endl;
        break;
    }
}



'''