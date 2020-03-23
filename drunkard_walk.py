from drunk import TraditionalDrunk, UpperDrunk, SidesDrunk
from cartesian_plane import CartesianPlane
from coordinate import Coordinate

from bokeh.plotting import figure, show


def graph(x, y):
    graph = figure(title="Drunkard's walk", x_axis_label="Steps", y_axis_label="Average distance traveled")
    graph.line(x, y, legend='Average distance traveled')
    show(graph)


def hike(plane, drunk, steps):
    x_moves = []
    y_moves = []

    for _ in range(steps):
        plane.move_drunk(drunk)
        x_moves.append(plane.get_coordinate(drunk).x)
        y_moves.append(plane.get_coordinate(drunk).y)

    return x_moves, y_moves


def simulate_hike(drunk_type, steps):
    drunk = drunk_type(name="Santi")
    origin = Coordinate(0, 0)
    plane = CartesianPlane()
    plane.add_drunk(drunk, origin)

    x_moves, y_moves = hike(plane, drunk, steps)
    return x_moves, y_moves


def main(drunk_type, steps):
    x_moves, y_moves = simulate_hike(drunk_type, steps)
    graph(x_moves, y_moves)


if __name__ == "__main__":
    main(TraditionalDrunk, 10000)
