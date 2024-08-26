import numpy as np

A = np.loadtxt("linear-system_a.txt",dtype='f', delimiter=' ')
b = np.array([0,0,0,0,0,0,0,0,0,0,1])
x = np.linalg.solve(A,b)

print("Probabilidades item A via Markov:")

for i, p in enumerate(x):
  print(f"P{i} = {p:.4f}")
