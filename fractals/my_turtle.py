"""
there is a more complicated but more capable way where you subclass the turtle to keep track of its bounding box 
(the furthest points travelled to in each axis)  and then update the screensize based on that.
"""

class MyTurtle(turtle.RawTurtle): # here we subclass the turtle to allow us to call statusbar updates after each movement
    def __init__(self, canvas):
        turtle.RawTurtle.__init__(self, canvas)
        self.bbox = [0,0,0,0]

    def _update_bbox(self): # keep a record of the furthers points visited
        pos = self.position()
        if pos[0] < self.bbox[0]:
            self.bbox[0] = pos[0]
        elif pos[0] > self.bbox[2]:
            self.bbox[2] = pos[0]
        if pos[1] < self.bbox[1]:
            self.bbox[1] = pos[1]
        elif pos[1] > self.bbox[3]:
            self.bbox[3] = pos[1]

    def forward(self, *args):
        turtle.RawTurtle.forward(self, *args)
        self._update_bbox()

    def backward(self, *args):
        turtle.RawTurtle.backward(self, *args)
        self._update_bbox()

    def right(self, *args):
        turtle.RawTurtle.right(self, *args)
        self._update_bbox()

    def left(self, *args):
        turtle.RawTurtle.left(self, *args)
        self._update_bbox()

    def goto(self, *args):
        turtle.RawTurtle.goto(self, *args)
        self._update_bbox()

    def setx(self, *args):
        turtle.RawTurtle.setx(self, *args)
        self._update_bbox()

    def sety(self, *args):
        turtle.RawTurtle.sety(self, *args)
        self._update_bbox()

    def setheading(self, *args):
        turtle.RawTurtle.setheading(self, *args)
        self._update_bbox()

    def home(self, *args):
        turtle.RawTurtle.home(self, *args)
        self._update_bbox()


# then we create a canvas for the turtle to work on:
cv = turtle.ScrolledCanvas(root)

# and then we turn that canvas into a turtlescreen:
screen = turtle.TurtleScreen(cv)

# we create a turtle on the screen:
turt = MyTurtle(screen)

# now the turtle can be used as a normal turtle (move, colour, shape, speed etc) and if the turtle goes beyond the bounds of the screen you can call:
min_x, min_y, max_x, max_y = turt.bbox # get the furthest points the turtle has been
width = max((0-min_x),(max_x)) * 2 + 100 # work out what the maximum distance from 0,0 is for each axis
height = max((0-min_y),(max_y)) * 2 + 100 # the 100 here gives us some padding between the edge and whats drawn
screen.screensize(width, height)

# note that the above code re sizes equally about the origin as thats what the screen method allows for, however if you delved deeper and applied the 
# bbox to the canvas itself you could make it re size only around the items on the canvas.
