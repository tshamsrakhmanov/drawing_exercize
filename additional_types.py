from dataclasses import dataclass


@dataclass
class Point:
    x: int
    y: int


@dataclass
class RGBColor:
    r: int
    g: int
    b: int


@dataclass
class DrawablePixel:
    x: int
    y: int
    color: RGBColor
