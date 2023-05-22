from logic.point.point import Point


class GridMap:
    def __init__(self, width, height, obstacle_list, pixel_size=10):
        self.adjacency_list = {}

        for i in range(0, width, pixel_size):
            for j in range(0, height, pixel_size):
                grid_tile = Point(i, j)
                neighbors = []

                # Add Left, Right, Up, Down Neighbors
                adjacent = [grid_tile + Point(-pixel_size, 0),
                            grid_tile + Point(pixel_size, 0),
                            grid_tile + Point(0, -pixel_size),
                            grid_tile + Point(0, pixel_size)]

                # Borders
                top_left = Point(0, 0)
                bottom_right = Point(width, height)

                for points in adjacent:
                    if top_left <= points < bottom_right and points not in obstacle_list:
                        neighbors.append(points)

                self.adjacency_list[grid_tile] = neighbors

    def get_neighbors(self, point):
        if point in self.adjacency_list:
            return self.adjacency_list[point]
        else:
            return []
