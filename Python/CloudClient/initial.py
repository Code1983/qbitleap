#!/usr/bin/python3.5
from dwave.cloud import Client
client = Client.from_config()
solver = client.get_solver()

#This does not provide embeddings of it's own and hence need sto be checked manually
print(solver.check_problem({0: -1, 1: 1},{(0, 1):0.5}))
print(solver.check_problem({0: -1, 4: 1},{(0, 4):0.5}))

#to find appropriate qubits
u, v = next(iter(solver.edges))

#submit the problem to D-wave
computation = solver.sample_ising({u: -1, v: 1},{(u,v): 1}, num_reads=5)

#print the results
print(computation.samples[0][u], computation.samples[0][v])
