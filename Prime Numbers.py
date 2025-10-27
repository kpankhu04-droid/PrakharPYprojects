prime = [1]

for i in range(2,10000):
    count = 0
    for num in range(0,len(prime)):
        if i % prime[num] == 0:
            count += 1
    if count == 1 :
        prime.append(i)

print(prime)
