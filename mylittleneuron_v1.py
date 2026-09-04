def step(z):
    return 1 if z >= 0 else 0 

def neuron(x1, x2, w1, w2, bias):
    z = x1 * w1 + x2 * w2 + bias
    return step(z),z

w1, w2, bias = 2,2,-0.5

print("\n ==AND gate== \n")

for x1 in (0,1): 
    for x2 in (0,1):
        out, z = neuron(x1,x2,w1,w2,bias)
        expected = x1 and x2
        ok = "OK" if out == expected else "FAIL"
        print(f"{x1:>3} {x2:>3} {z:>6.1f} {out:>7} {expected:>9} {ok:>10}")


print("\n ==XOR gate== \n")

for x1 in (0,1): 
    for x2 in (0,1):
        out, z = neuron(x1,x2,w1,w2,bias)
        expected = x1 ^ x2
        ok = "OK" if out == expected else "FAIL"
        print(f"{x1:>3} {x2:>3} {z:>6.1f} {out:>7} {expected:>9} {ok:>10}")



