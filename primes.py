import pickle, math
import time, statistics

with open('primes.pkl','rb') as f:
    primes = pickle.load(f)
try:
    interval = []
    t = time.time()
    current = primes[-1] + 1
    while True:
        prime = True
        sqrt = math.sqrt(current)
        for i in primes:
            if current % i == 0:
                prime = False
            if i > sqrt:
                break
        if prime:
            primes.append(current)
            print(current)
            i = time.time()-t
            interval.append(i)
            # print(f'{i:4f}')
            t = time.time()
        current += 1
except KeyboardInterrupt:
    with open('primes.pkl','wb') as f:
        pickle.dump(primes,f)
    with open('primes.txt', 'w') as f:
        for p in primes:
            f.write(f'{str(p)}\n')
    import numpy
    primes = numpy.array(primes)
    primes = {'primes':primes}
    from safetensors.numpy import save_file
    save_file(primes,'primes.safetensors')
    print(f'\nMean time between primes: {statistics.mean(interval):4f}')
    print(f'Found {len(interval)} primes')