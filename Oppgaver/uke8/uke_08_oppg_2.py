"""Implement Pearsons correlation equation by creating the function pearson_corr(x,y)"""
import math

def pearson_corr(x,y:list) -> float:
    """Takes in xs and ys and returns the pearson correlation"""
    xAvg = sum(x)/len(x)
    yAvg = sum(y)/len(y)
    dx = []
    dy = []
    for value in x: dx.append(value-xAvg)
    for value in y: dy.append(value-yAvg)

    sumDxDy = 0
    for xValue, yValue in zip(dx,dy):
        sumDxDy += xValue * yValue

    dx2 = 0
    dy2 = 0
    for value in dx: dx2 += value**2
    for value in dy: dy2 += value**2

    sqr_dx2dy2 = math.sqrt(dx2 * dy2)

    return sumDxDy/sqr_dx2dy2


