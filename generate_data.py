#!/usr/bin/python3

from sim import sim_data

sd = sim_data.SimData(1000)
sd.generate(20 * (10 ** 5))
sd.save()
