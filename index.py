print("Adad Avale")
sieve = [True] * 11
for i in range(2, 10):
    if sieve[i]:
        print(i)   
        for j in range(i*i, 10, i):          
            sieve[j] = False

print(sieve)