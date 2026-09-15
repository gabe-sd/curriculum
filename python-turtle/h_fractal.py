import turtle as t

def drawline(pos1, pos2):
    # tracing the algorithm.
    t.penup()
    t.goto(pos1[0], pos1[1])
    t.pendown()
    t.goto(pos2[0], pos2[1])


def recursivedraw(x, y, width, height, count):
    drawline(
        [x + width * 0.25, height // 2 + y],
        [x + width * 0.75, height // 2 + y],
    )
    drawline(
        [x + width * 0.25, (height * 0.5) // 2 + y],
        [x + width * 0.25, (height * 1.5) // 2 + y],
    )
    drawline(
        [x + width * 0.75, (height * 0.5) // 2 + y],
        [x + width * 0.75, (height * 1.5) // 2 + y],
    )

    if count <= 0:  # The base case
        return
    else:  # The recursive step
        count -= 1
        
        recursivedraw(x, y, width // 2, height // 2, count)
     
        recursivedraw(x + width // 2, y, width // 2, height // 2, count)
       
        recursivedraw(x, y + width // 2, width // 2, height // 2, count)
        
        recursivedraw(x + width // 2, y + width // 2, width // 2, height // 2, count)

t.Screen().bgcolor("black")
t.color("red")
t.speed(0)
fractal_depth = 5
drawing_width = 400
drawing_height = 400
recursivedraw(- drawing_width / 2, - drawing_height / 2, drawing_width, drawing_height, fractal_depth)