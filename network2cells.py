import numpy as np

X = np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1],
])

Y = np.array([
    [0],
    [1],
    [1],
    [0],

])

def sigmoid(x):
    return x * (1 - x)

#Everything in the network comes from the seed
np.random.seed(43)

n_inputs = 2
n_hidden = 2
n_outputs = 1

weights_1 = np.random.uniform(-1,1,(n_inputs,n_hidden))
bias_1 = np.zeros(1,n_hidden)

weights_2 = np.random.uniform(-1,1,(n_inputs,n_hidden))
bias_2 = np.zeros(1,n_outputs)

learning_rate = 0.5
epoch = 10000

for epoch in range(epochs):
    hidden_input = np.dot(X,weights_1) + bias_1
    hidden_output = sigmoid(hidden_input)

    final_input = np.dot(hidden_output, weights_2) + bias_2
    final_output = sigmoid(final_input)
