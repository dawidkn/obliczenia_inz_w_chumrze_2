import time

def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def find_primes(limit=30):
    primes = []
    start_time = time.time()
    num = 2
    while time.time() - start_time < limit:
        if is_prime(num):
            primes.append(num)
        num += 1
    return primes

if __name__ == "__main__":
    limit = 30  # Czas w sekundach
    primes = find_primes(limit)
    with open("python_output.txt", "w") as f:
        f.write(f"Found {len(primes)} primes in {limit} seconds.\n")
