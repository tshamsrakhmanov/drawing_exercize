from dataclasses import dataclass


@dataclass
class Point:
    """
    Class to determine object-related coordinates
    """
    x: int
    y: int


@dataclass
class RGBColor:
    r: int
    g: int
    b: int