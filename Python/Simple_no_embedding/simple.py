from dwave.system.samplers import DWaveSampler
#sampler = DWaveSampler(solver={'qpu': True})

solver = DWaveSampler()
print("Connected to sampler", solver.solver.id)

qubits = solver.properties['qubits']
couplers = solver.properties['couplers']

qubit_1 = 0
qubit_2 = 4
coupler = [qubit_1,qubit_2]

if (qubit_1 in qubits) and \
   (qubit_2 in qubits) and \
   (coupler in couplers):
    print('Qubits {} and {} and their coupler {} are available'.format(qubit_1,
                                                                       qubit_2,
                                                                        coupler))
h = {qubit_1:-1,qubit_2:-1}
J = {tuple(coupler):-1}
solution = solver.sample_ising(h,J,num_reads=10)
solution
