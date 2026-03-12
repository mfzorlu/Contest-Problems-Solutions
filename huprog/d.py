n = int(input())

def sieve_of_eratosthenes(n):
    """
    Standard optimized sieve - finds all primes up to n
    """
    if n < 2:
        return []
    
    # Only store odd numbers (except 2)
    # is_prime[i] represents whether 2*i+3 is prime
    is_prime = [True] * ((n - 1) // 2)
    limit = int(n ** 0.5)
    
    for i in range(limit // 2):
        if is_prime[i]:
            # The actual prime number
            p = 2 * i + 3
            # Mark multiples as composite, starting from p*p
            # Only mark odd multiples
            start = (p * p - 3) // 2
            for j in range(start, len(is_prime), p):
                is_prime[j] = False
    
    # Collect all primes
    primes = [2] + [2 * i + 3 for i in range(len(is_prime)) if is_prime[i]]
    return primes

def binary_search_exact(arr, target: int) -> int:
    """
    Find exact position of target in sorted array
    Returns: index if found, -1 otherwise
    """
    left, right = 0, len(arr) - 1
    
    while left <= right:
        mid = left + (right - left) // 2  # Avoid overflow
        
        if arr[mid] == target:
            return mid
        elif arr[mid] < target:
            left = mid + 1
        else:
            right = mid - 1
    
    return -1

"""def factorial(n:int) -> int:
    if n <= 1:
        return 1
    return factorial(n-1) * n

def square(n:int) -> int:  # hocam valla biz yazdık, elenmiyek şimdi durduk yere :p
    return n*n"""


if n==4:
    print("NO")
    exit()

f=0
primes = sieve_of_eratosthenes(n)
if n in primes:
    print("NO")
    exit()


print("YES")
