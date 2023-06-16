# Simple Snake game. Speed raises every 5 points.


from tkinter import *
from random import randrange

points = 0
points_to_raise = 5

snake_speed = 400

snake_segment_size = 10

snake_body_size = 1

snake_expected_size = 3


canvas_width = 400

canvas_height = 350


snake_segments = []

food_object = []


food_eaten = False
food_size = 10


head_pos_x = 190

head_pos_y = 170


expected_vector = ""

game_over_bool = False


root = Tk()

root.geometry("600x350")

c = Canvas(root, width=canvas_width, height=canvas_height, background="black")

main_menu = Tk()

main_menu.geometry("300x300")


class Segment():

    def __init__(self, x, y, vector, c):
        self.x = x
        self.y = y
        self.vector = vector

        self.segment = c.create_rectangle(self.x, self.y, self.x + snake_segment_size, self.y + snake_segment_size, fill="green")

class Food():

    def __init__(self, x, y):
        self.x = x
        self.y = y

        self.food = c.create_rectangle(self.x, self.y, self.x + food_size, self.y + food_size, fill="red")


snake_segments.append(Segment(head_pos_x, head_pos_y, "up", c))

def add_segment():
    global snake_segments
    global snake_expected_size
    global snake_body_size
    global snake_segment_size

    while snake_body_size < snake_expected_size:
        if snake_segments[-1].vector == "up":
            snake_segments.append(Segment(snake_segments[-1].x, snake_segments[-1].y + snake_segment_size, snake_segments[-1].vector, c))

        elif snake_segments[-1].vector == "down":
            snake_segments.append(Segment(snake_segments[-1].x, snake_segments[-1].y - snake_segment_size, snake_segments[-1].vector, c))

        elif snake_segments[-1].vector == "right":
            snake_segments.append(Segment(snake_segments[-1].x - snake_segment_size, snake_segments[-1].y, snake_segments[-1].vector, c))

        elif snake_segments[-1].vector == "left":
            snake_segments.append(Segment(snake_segments[-1].x + snake_segment_size, snake_segments[-1].y, snake_segments[-1].vector, c))

        snake_body_size += 1

add_segment()


def spawn_food():
    global food_object

    food_pos_x = randrange(10, canvas_width - 10, 10)
    food_pos_y = randrange(10, canvas_height - 10, 10)

    food_object.append(Food(food_pos_x, food_pos_y))

spawn_food()

def collision_check():
    global snake_segments
    global food_object
    global food_eaten
    global snake_expected_size
    global points
    global c
    global game_over_bool

    if snake_segments[0].x == food_object[0].x and snake_segments[0].y == food_object[0].y:
        c.delete(food_object[0].food)
        food_object.pop(0)

        snake_expected_size += 1
        points += 1

        add_segment()
        spawn_food()

    for i in range(1, len(snake_segments)):
        if snake_segments[0].x == snake_segments[i].x and snake_segments[0].y == snake_segments[i].y:
            game_over_bool = True
            open_gameover_window()


def open_gameover_window():
    game_over = Toplevel(root)

    game_over.geometry("300x300")

    game_over.attributes("-topmost", True)

    game_over_label = Label(game_over, text="Game Over!", fg="red", height=3, width=15, font=30).pack(expand=True)
    try_again_button = Button(game_over, text="Try again!", height=3, width=15, font=30, command=lambda :[restart(), game_over.destroy()]).pack(expand=True)
    game_over_exit_button = Button(game_over, text="Exit!", height=3, width=15, font=30, command=lambda :[game_over.destroy(), root.destroy()]).pack(expand=True)

def move():
    global snake_segments
    global snake_speed
    global expected_vector
    global points_to_raise
    global game_over_bool

    points_label.config(text=f"Points: {points}")

    #-----------------------------------------------------------------------

    if expected_vector == "up" and snake_segments[0].vector != "down":
        snake_segments[0].vector = "up"

    elif expected_vector == "down" and snake_segments[0].vector != "up":
        snake_segments[0].vector = "down"

    elif expected_vector == "right" and snake_segments[0].vector != "left":
        snake_segments[0].vector = "right"

    elif expected_vector == "left" and snake_segments[0].vector != "right":
        snake_segments[0].vector = "left"

    # -----------------------------------------------------------------------
    # -----------------------------------------------------------------------

    for seg in snake_segments:
        if seg.vector == "up":
            c.move(seg.segment, 0, -10)
            seg.y -= 10

        elif seg.vector == "down":
            c.move(seg.segment, 0, 10)
            seg.y += 10

        elif seg.vector == "right":
            c.move(seg.segment, 10, 0)
            seg.x += 10

        elif seg.vector == "left":
            c.move(seg.segment, -10, 0)
            seg.x -= 10

    # -----------------------------------------------------------------------
    # -----------------------------------------------------------------------

    for i in range(len(snake_segments)-1, 0, -1):
        snake_segments[i].vector = snake_segments[i-1].vector

    # -----------------------------------------------------------------------

    for seg in snake_segments:
        if seg.y == 0:
            c.moveto(seg.segment, seg.x - 1, 350 - 1)
            seg.y = 350

        elif seg.y == 350:
            c.moveto(seg.segment, seg.x - 1, 0 - 1)
            seg.y = 0

        elif seg.x == 0:
            c.moveto(seg.segment, 400 - 1, seg.y - 1)
            seg.x = 400

        elif seg.x == 400:
            c.moveto(seg.segment, 0 - 1, seg.y - 1)
            seg.x = 0

        print(f"{snake_segments.index(seg)}; X: {seg.x}, Y: {seg.y}")
    #print(snake_segments[0].x, snake_segments[0].y)


    if snake_speed >= 50 and points == points_to_raise:
        snake_speed -= 90
        points_to_raise += 5

    collision_check()

    if game_over_bool == True:
        return

    c.after(snake_speed, move)

def start():
    root.attributes("-topmost", True)

    try:
        main_menu.destroy()
    except:
        pass

    move()

def restart():
    global game_over_bool
    global snake_segments
    global snake_body_size
    global snake_expected_size
    global game_over_bool
    global points
    global points_to_raise
    global snake_speed

    for seg in snake_segments:
        c.delete(seg.segment)

    snake_segments.clear()

    snake_segments.append(Segment(head_pos_x, head_pos_y, "up", c))

    points = 0

    points_to_raise = 5

    snake_body_size = 1

    snake_expected_size = 3

    snake_speed = 400

    game_over_bool = False

    root.attributes("-topmost", True)

    add_segment()
    move()

def go_up(e):
    global expected_vector

    expected_vector = "up"

def go_down(e):
    global expected_vector

    expected_vector = "down"

def go_right(e):
    global expected_vector

    expected_vector = "right"

def go_left(e):
    global expected_vector

    expected_vector = "left"

root.bind("<Up>", go_up)
root.bind("<Down>", go_down)
root.bind("<Right>", go_right)
root.bind("<Left>", go_left)

points_label = Label(root, text="Points: 0")
points_label.place(x=20, y=20)


start_button = Button(main_menu, text="Start", height=3, width=15, font=30, command=start).pack(expand=True)

exit_button = Button(main_menu, text="Exit", height=3, width=15, font=30, command=lambda :[main_menu.destroy(), root.destroy()]).pack(expand=True)


c.pack(expand=True)

main_menu.attributes("-topmost", True)

main_menu.mainloop()

root.mainloop()
