#!/usr/bin/python3

from sim import sim_data

sd = sim_data.SimData(100)
sd.generate(100000)
sd.save()
