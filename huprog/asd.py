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

primes = sieve_of_eratosthenes(10**7)

print(len(primes))