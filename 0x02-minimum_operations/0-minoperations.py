#usr/bin/python3
def minOperations(n): 
    if n == 0: 
        return 0 
    elif n == 1: 
        return 1 
    else: 
        # find the largest power of 2 that is less than or equal to n 
        p = 2  
        while p <= n:  
            p *= 2  

        # subtract the largest power of 2 from n and recur for the remaining number  
        return 1 + minOperations(n - (p//2))  

     # Driver code  
n = 10     # Number of H's required in the file  
print(minOperations(n))
