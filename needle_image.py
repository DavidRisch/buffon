import simulation
import simulation_graphic


def make_image():
    sim = simulation.Simulation(2, 4, 10, 50)
    result = sim.simulate(1000)
    print("total needle count: ", result.total_needles)
    print("needles on a line count: ", result.needles_on_line)
    print("p: ", result.total_needles / result.needles_on_line)
    simulation_graphic.create_image("output/needels.png", result)


if __name__ == "__main__":
    make_image()
