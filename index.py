#python -u index.py
#TODO Python 

print ("Pleas Enter The Number : ")
Number = int(input())

if 0<=Number<=10:
    print(f"Number ({Number}) Tinner of 10")
elif Number>10:
    print(f"Number ({Number}) Bigger of 10")
else:
    print(f"Number ({Number}) NONE")
