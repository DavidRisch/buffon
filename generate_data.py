#!/usr/bin/python3

from sim import sim_data
from definitions import *

sd = sim_data.SimData(100)
sd.generate((10 ** 4))
sd.save(path_saved_sim_data_hist)

sd = sim_data.SimData(1000)
sd.generate(20 * (10 ** 5))
sd.save()
