from abc import ABC, abstractmethod
from typing import Tuple


# Strategy Interface
class RouteStrategy(ABC):
    @abstractmethod
    def calculate_route(
            self,
            point_a: Tuple[float, float],
            point_b: Tuple[float, float]
    ):
        pass


# Concrete Strategies
class FastestRoute(RouteStrategy):
    def calculate_route(
            self,
            point_a: Tuple[float, float],
            point_b: Tuple[float, float]
    ):
        print(f"Calculating fastest route from: {point_a} to {point_b}...")


class ShortestRoute(RouteStrategy):
    def calculate_route(
            self,
            point_a: Tuple[float, float],
            point_b: Tuple[float, float]
    ):
        print(f"Calculating shortest route from {point_a} to {point_b}...")


# Context
class NavSystem:
    def __init__(self, route_strategy: RouteStrategy):
        self.route_strategy = route_strategy

    def set_route_strategy(self, route_strategy: RouteStrategy):
        self.route_strategy = route_strategy

    def get_route(
            self,
            point_a: Tuple[float, float],
            point_b: Tuple[float, float]
    ):
        self.route_strategy.calculate_route(point_a=point_a, point_b=point_b)


# Usage
if __name__ == "__main__":
    waze = NavSystem(route_strategy=FastestRoute())
    waze.get_route(point_a=(12.334, 54.998), point_b=(51.928, 97.554))
    waze.set_route_strategy(route_strategy=ShortestRoute())
    waze.get_route(point_a=(12.334, 54.998), point_b=(51.928, 97.554))
