"""List of prime numbers generator."""
"""ENTER YOUR SOLUTION HERE!"""

def primes(number_of_primes):
    if number_of_primes <=0:
        raise ValueError(f'{number_of_primes} should should be a positive number')
    else:
        list = []
        incremental = 2
        while len(list) < number_of_primes:
            is_prime = True
            for i in range(2, incremental):
                if incremental%i == 0:
                    is_prime = False
                    break
            if is_prime:
                list.append(incremental)
            incremental += 1    
        
    return list



