#!/usr/bin/python3.5
import dimod
from dwave.system.samplers import DWaveSampler
from dwave.system.composites import EmbeddingComposite

sampler = EmbeddingComposite(DWaveSampler())

csp = dwavebinarycsp.factories.random_2in4sat(10, 7)
bqm = dwavebinarycsp.stitch(csp)

bqm = dimod.BinaryQuadraticModel({0: 0, 1: 0},{(0, 1):-1},0,dimod.SPIN)

solution = sampler.sample(bqm, num_reads=1000)
