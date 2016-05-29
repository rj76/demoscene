import time

from turtle import *
from cmath import phase

# TODO: use _multiple turtles_ to trace points with different escape times (awesome)
# TODO: optimize sort order to avoid awkward radial lines

def z_n_escape_time(c, n):
    z = 0
    for i in range(n):
        z = z**2 + c
        if abs(z)>2:
            return i
    return False

def mandelbrot_edge(resolution, iterations, edge):
    points=[]
    x_coordinates = [-2+i*(3/resolution) for i in range(int(resolution*1.5))]
    y_coordinates = [1-j*(2/resolution) for j in range(resolution)]
    for x in x_coordinates:
        for y in y_coordinates:
            if z_n_escape_time(complex(x,y),iterations) in edge:
                points.append((x,y))
    points = sorted(points, key=lambda p: phase(complex(p[0],p[1])))
    return points

def draw_boundary(protagonist, boundary_points, speed):
    protagonist.speed(speed)
    protagonist.penup()
    protagonist.setheading(protagonist.towards(boundary_points[0][0],boundary_points[0][1]))
    protagonist.forward(protagonist.distance(boundary_points[0][0],boundary_points[0][1]))
    protagonist.pendown()
    for p in boundary_points[1:]:
        protagonist.setheading(protagonist.towards(p[0],p[1]))
        protagonist.forward(protagonist.distance(p[0],p[1]))

def main():
    setting = Screen()
    setting.title("Mandelbrot fun")
    setting.bgcolor('#FFFFFF')

    protagonist = RawTurtle(setting)
    protagonist.shape("turtle")

    resolution = 300

    iterations = 500

    # increasing edge start / end will make it more dense
    edge_list_start = 10
    edge_list_end = 20

    # “fastest”: 0
    # “fast”: 10
    # “normal”: 6
    # “slow”: 3
    # “slowest”: 1
    speed = 0

    start = time.time()

    points = [(190*p[0],190*p[1]) for p in mandelbrot_edge(resolution, iterations, list(range(edge_list_start, edge_list_end)))]

    print('Time to create %d points: %r' % (len(points), time.time()-start))

    draw_boundary(protagonist, points, speed)
    setting.mainloop()

main()
