from drunk import TraditionalDrunk, UpperDrunk, SidesDrunk
from cartesian_plane import CartesianPlane
from coordinate import Coordinate

from bokeh.plotting import figure, show


def graph(x, y):
    graph = figure(title="Drunkard's walk", x_axis_label="Steps", y_axis_label="Average distance traveled")
    graph.line(x, y, legend='Average distance traveled')
    show(graph)


def hike(plane, drunk, steps):
    start = plane.get_coordinate(drunk)

    for _ in range(steps):
        plane.move_drunk(drunk)

    return start.distance(plane.get_coordinate(drunk))


def simulate_hike(steps, number_of_attempts, drunk_type):
    drunk = drunk_type(name="Santi")
    origin = Coordinate(0, 0)
    distances = []

    for _ in range(number_of_attempts):
        plane = CartesianPlane()
        plane.add_drunk(drunk, origin)
        hike_simulation = hike(plane, drunk, steps)
        distances.append(round(hike_simulation, 1))

    return distances


def main(hike_distances, number_of_attempts, drunk_type):
    average_distance_traveled_in_hikes = []

    for steps in hike_distances:
        distances = simulate_hike(steps, number_of_attempts, drunk_type)
        medium_distance = round(sum(distances) / len(distances), 4)
        average_distance_traveled_in_hikes.append(medium_distance)

    graph(hike_distances, average_distance_traveled_in_hikes)


if __name__ == "__main__":
    hike_distances = range(1, 200)
    number_of_attempts = 100

    main(hike_distances, number_of_attempts, TraditionalDrunk)
