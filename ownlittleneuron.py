def step(z):
    return 1 if z >= 0 else 0

def neuron(x1,x2,w1,w2,bias):
    z = x1 * w1 + x2 * w2 + bias
    return step(z),z


w1, w2, bias = 0,0,1 

