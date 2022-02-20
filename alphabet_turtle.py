"""Functions in Python for the Website."""

from turtle import Turtle, colormode, done, tracer, update
import random
from random import randint
colormode(255)

# get an input from the user
# user_word: str = input("Choose a word to generate an image!: ")


def main() -> None:
    """The entrypoint of the program."""
    user_input: str = input("Enter a word for a randomly generated piece of art!: ")
    user_input = user_input.lower()
    tracer(0, 0)
    leo: Turtle = Turtle()
    for i in user_input:
        if i == "a":
            a(leo)
        elif i == "b":
            letter_b(leo)
        elif i == "c":
            c(leo)
        elif i == "d":
            d(leo)
        elif i == "e":
            e(leo)
        elif i == "f":
            f(leo)
        elif i == "g":
            letter_g(leo)
        elif i == "h":
            h(leo)
        elif i == "i":
            i(leo)
        elif i == "j":
            j(leo)
        elif i == "k":
            k(leo)
        elif i == "l":
            letter_l(leo)
        elif i == "m":
            m(leo)
        elif i == "n":
            n(leo)
        elif i == "o":
            o(leo)
        elif i == "p":
            p(leo)
        elif i == "q":
            q(leo)
        elif i == "r":
            letter_r(leo)
        elif i == "s":
            s(leo)
        elif i == "t":
            t(leo)
        elif i == "u":
            u(leo)
        elif i == "v":
            v(leo)
        elif i == "w":
            w(leo)
        elif i == "x":
            x(leo)
        elif i == "y":
            y(leo)
        elif i == "z":
            z(leo)
        else:
            user_input = input("Invalid Characters. Try Again: ")
    leo.speed(0)
    update()
    done()


# generate random image based on letters of the input
def a(draw_a: Turtle) -> None:
    """Draws a square."""
    draw_a.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    side_length: int = randint(45, 250)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_a.fillcolor(r, g, b)
    draw_a.goto(x, y)
    draw_a.pendown()
    draw_a.begin_fill()
    for i in range(4):
        draw_a.forward(side_length)
        draw_a.left(90)
    draw_a.end_fill()


def letter_b(draw_b: Turtle) -> None:
    """Draws a pentagon."""
    draw_b.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    side_length: int = randint(45, 250)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_b.fillcolor(r, g, b)
    draw_b.goto(x, y)
    draw_b.pendown()
    draw_b.begin_fill()
    for i in range(5):
        draw_b.forward(side_length)
        draw_b.left(72)
    draw_b.end_fill()


def c(draw_c: Turtle) -> None:
    """Draws a super-star."""
    draw_c.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_c.fillcolor(r, g, b)
    draw_c.begin_fill()
    draw_c.goto(x, y)
    draw_c.pendown()
    for i in range(36):
        draw_c.forward(200)
        draw_c.left(170)
    draw_c.end_fill()


def d(draw_d: Turtle) -> None:
    """Draws a cloud."""
    draw_d.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_d.goto(x, y)
    draw_d.fillcolor(r, g, b)
    draw_d.pendown()  # begins drawing
    draw_d.begin_fill()
    draw_d.circle(25, 180)
    draw_d.right(90)
    draw_d.circle(25, 180)
    draw_d.right(180)
    draw_d.circle(25, 180)
    draw_d.right(90)
    draw_d.circle(25, 180)
    draw_d.right(90)
    draw_d.circle(25, 180)
    draw_d.right(180)
    draw_d.circle(25, 180)
    draw_d.end_fill()
    draw_d.setheading(0)


def e(draw_e: Turtle) -> None:
    """Draws an ordinary star."""
    draw_e.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_e.fillcolor(r, g, b)
    draw_e.goto(x, y)
    draw_e.right(75)
    draw_e.forward(100)
    draw_e.pendown()
    draw_e.begin_fill()
    for i in range(4):
        draw_e.right(144)
        draw_e.forward(100)
    draw_e.end_fill()


def f(draw_f: Turtle) -> None:
    """Draws a hexagon."""
    draw_f.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_f.fillcolor(r, g, b)
    draw_f.goto(x, y)
    draw_f.pendown()
    draw_f.begin_fill()
    for i in range(6):
        draw_f.right(60)
        draw_f.forward(100)
    draw_f.end_fill()


def letter_g(draw_g: Turtle) -> None:
    """Draws a septagon."""
    draw_g.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_g.fillcolor(r, g, b)
    draw_g.goto(x, y)
    draw_g.pendown()
    draw_g.begin_fill()
    for i in range(7):
        draw_g.right(360/7)
        draw_g.forward(100)
    draw_g.end_fill()


def h(draw_h: Turtle) -> None:
    """Draws an octagon."""
    draw_h.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_h.fillcolor(r, g, b)
    draw_h.goto(x, y)
    draw_h.pendown()
    draw_h.begin_fill()
    for i in range(8):
        draw_h.right(360/8)
        draw_h.forward(100)
    draw_h.end_fill()


def letter_i(draw_i: Turtle) -> None:
    """Draws a nonagon."""
    draw_i.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_i.fillcolor(r, g, b)
    draw_i.goto(x, y)
    draw_i.pendown()
    draw_i.begin_fill()
    for counter in range(9):
        draw_i.right(360/9)
        draw_i.forward(100)
    draw_i.end_fill()


def j(draw_j: Turtle) -> None:
    """Draws a decagon."""
    draw_j.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_j.fillcolor(r, g, b)
    draw_j.goto(x, y)
    draw_j.pendown()
    draw_j.begin_fill()
    for i in range(10):
        draw_j.right(360/10)
        draw_j.forward(100)
    draw_j.end_fill()


def k(draw_k: Turtle) -> None:
    """Draws an inverse pentagon."""
    draw_k.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_k.fillcolor(r, g, b)
    draw_k.goto(x, y)
    draw_k.pendown()
    draw_k.begin_fill()
    for i in range(5):
        draw_k.right(108)
        draw_k.forward(100)
    draw_k.end_fill()


def letter_l(draw_l: Turtle) -> None:
    """Draws an inverse octagon."""
    draw_l.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_l.fillcolor(r, g, b)
    draw_l.goto(x, y)
    draw_l.pendown()
    draw_l.begin_fill()
    for i in range(8):
        draw_l.right(135)
        draw_l.forward(100)
    draw_l.end_fill()


def m(draw_m: Turtle) -> None:
    """Draws an inverse octagon."""
    draw_m.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_m.fillcolor(r, g, b)
    draw_m.goto(x, y)
    draw_m.pendown()
    draw_m.begin_fill()
    for i in range(9):
        draw_m.right(140)
        draw_m.forward(100)
    draw_m.end_fill()


def n(draw_n: Turtle) -> None:
    """Draws a petal."""
    draw_n.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_n.penup()
    draw_n.goto(x, y)
    draw_n.pendown()  # begins drawing
    draw_n.fillcolor(r, g, b)
    draw_n.begin_fill()
    count: int = 0
    # draws one half of a petal
    while count < 50:
        draw_n.right(2)
        draw_n.forward(1)
        count += 1
    count = 0
    draw_n.left(99)
    # draws the other half
    while count < 50:
        draw_n.right(2)
        draw_n.backward(1)
        count += 1
    draw_n.end_fill()
    draw_n.penup()
    draw_n.goto(x, y)
    draw_n.right(99)
    draw_n.left(45)


def o(draw_o: Turtle) -> None:
    """Draws a circle."""
    draw_o.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_o.fillcolor(r, g, b)
    draw_o.goto(x, y)
    draw_o.pendown()
    draw_o.begin_fill()
    draw_o.circle(randint(30, 80))
    draw_o.end_fill()


def p(draw_p: Turtle) -> None:
    """Draws a flower."""
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_p.penup()
    draw_p.goto(x, y)
    draw_p.pendown()  # begins drawing
    i: int = 0
    # creates seven petals
    while i < 7:
        draw_p.penup()
        draw_p.goto(x, y)
        draw_p.pendown()  # begins drawing
        draw_p.fillcolor(r, g, b)
        draw_p.begin_fill()
        count: int = 0
        # draws one half of a petal
        while count < 50:
            draw_p.right(2)
            draw_p.forward(1)
            count += 1
        count = 0
        draw_p.left(99)
        # draws the other half
        while count < 50:
            draw_p.right(2)
            draw_p.backward(1)
            count += 1
        draw_p.end_fill()
        draw_p.penup()
        draw_p.goto(x, y)
        draw_p.right(99)
        draw_p.left(45)
        i += 1


def q(draw_q: Turtle) -> None:
    """Draws a cube."""
    draw_q.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    draw_q.fillcolor(r, g, b)
    draw_q.goto(0, 0)
    draw_q.pendown()
    draw_q.begin_fill()
    for i in range(4):
        draw_q.forward(100)
        draw_q.left(90)
    draw_q.goto(50, 50)
    for i in range(4):
        draw_q.forward(100)
        draw_q.left(90)
    draw_q.goto(150, 50)
    draw_q.goto(100, 0)
    draw_q.goto(100, 100)
    draw_q.goto(150, 150)
    draw_q.goto(50, 150)
    draw_q.goto(0, 100)
    draw_q.end_fill()


def letter_r(draw_r: Turtle) -> None:
    """Draws a parallelogram."""
    draw_r.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_r.fillcolor(r, g, b)
    draw_r.goto(x, y)
    draw_r.pendown()
    draw_r.begin_fill()
    for i in range(2):
        draw_r.forward(100)
        draw_r.right(60)
        draw_r.forward(100)
        draw_r.right(120)
    draw_r.end_fill()


def s(draw_s: Turtle) -> None:
    """Draws a semi-circle."""
    draw_s.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_s.fillcolor(r, g, b)
    draw_s.goto(x, y)
    draw_s.pendown()
    draw_s.begin_fill()
    draw_s.circle(randint(30, 80), 180)
    draw_s.end_fill()


def t(draw_t: Turtle) -> None:
    """Draws a flower made of diamonds."""
    draw_t.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_t.fillcolor(r, g, b)
    draw_t.goto(x, y)
    draw_t.pendown()
    draw_t.begin_fill()
    for i in range(10):
        for i in range(2):
            draw_t.forward(100)
            draw_t.right(60)
            draw_t.forward(100)
            draw_t.right(120)
        draw_t.right(36)
    draw_t.end_fill()


def u(draw_u: Turtle) -> None:
    """Draws a snowflake."""
    draw_u.penup()
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_u.goto(x, y)
    draw_u.forward(90)
    draw_u.left(45)
    draw_u.pendown()
    for i in range(8):
        for i in range(3):
            for i in range(3):
                draw_u.forward(30)
                draw_u.backward(30)
                draw_u.right(45)
            draw_u.left(90)
            draw_u.backward(30)
            draw_u.left(45)
        draw_u.right(90)
        draw_u.forward(90)
        draw_u.left(45)


def v(draw_v: Turtle) -> None:
    """Draws a heart."""
    draw_v.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_v.fillcolor(r, g, b)
    draw_v.goto(x, y)
    draw_v.pendown()
    draw_v.begin_fill()
    draw_v.left(140)
    draw_v.forward(113)
    for i in range(200):
        draw_v.right(1)
        draw_v.forward(1)
    draw_v.left(120)
    for i in range(200):
        draw_v.right(1)
        draw_v.forward(1)
    draw_v.forward(112)
    draw_v.end_fill()


def w(draw_w: Turtle) -> None:
    """Draws a circle spirograph."""
    draw_w.penup()
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_w.goto(x, y)
    draw_w.pendown()
    for i in range(10):
        for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
            draw_w.color(color)
            draw_w.circle(50)
            draw_w.left(5)
        

def x(draw_x: Turtle) -> None:
    """Draws a rectangular prism."""
    draw_x.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    draw_x.fillcolor(r, g, b)
    draw_x.goto(0, 0)
    draw_x.pendown()
    draw_x.begin_fill()
    for i in range(2):
        draw_x.forward(100)
        draw_x.left(90)
        draw_x.forward(150)
        draw_x.left(90)
    draw_x.goto(50, 50)
    for i in range(2):
        draw_x.forward(100)
        draw_x.left(90)
        draw_x.forward(150)
        draw_x.left(90)
    draw_x.goto(150, 50)
    draw_x.goto(100, 0)
    draw_x.goto(100, 150)
    draw_x.goto(150, 200)
    draw_x.goto(50, 200)
    draw_x.goto(0, 150)
    draw_x.end_fill()


def y(draw_y: Turtle) -> None:
    """Draws a square spirograph."""
    draw_y.penup()
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_y.goto(x, y)
    draw_y.pendown()
    for i in range(10):
        for color in ("red", "magenta", "blue", "cyan", "green", "white", "yellow"):
            draw_y.color(color)
            for i in range(4):
                draw_y.forward(50)
                draw_y.right(90)
            draw_y.left(5)
    draw_y.pencolor("black")


def z(draw_z: Turtle) -> None:
    """Draws a spiraling background."""
    draw_z.penup()
    r: int = randint(0, 256)
    g: int = randint(0, 256)
    b: int = randint(0, 256)
    x: float = random.uniform(-250, 250)
    y: float = random.uniform(-250, 250)
    draw_z.fillcolor(r, g, b)
    draw_z.goto(x, y)
    draw_z.pendown()
    draw_z.begin_fill()
    for i in range(100):
        draw_z.circle(5*i)
        draw_z.circle(-5*i)
        draw_z.left(i)
    draw_z.end_fill()


if __name__ == "__main__":
    main()
