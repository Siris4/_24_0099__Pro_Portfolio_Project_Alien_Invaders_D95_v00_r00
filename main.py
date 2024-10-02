import tkinter as tk

# Set up the main window
root = tk.Tk()
root.title("Space Invaders")
root.resizable(False, False)
root.geometry("600x400")

# Create the canvas for the game
canvas = tk.Canvas(root, width=600, height=400, bg="black")
canvas.pack()

# Spaceship properties
spaceship_width = 40
spaceship_height = 20
spaceship_x = 280  # starting x position of the spaceship
spaceship_y = 350  # fixed y position
spaceship_speed = 20

# Create the spaceship
spaceship = canvas.create_rectangle(spaceship_x, spaceship_y, spaceship_x + spaceship_width, spaceship_y + spaceship_height, fill="green")

# List to keep track of bullets
bullets = []

# Function to move the spaceship left
def move_left(event):
    x1, y1, x2, y2 = canvas.coords(spaceship)
    if x1 > 0:
        canvas.move(spaceship, -spaceship_speed, 0)

# Function to move the spaceship right
def move_right(event):
    x1, y1, x2, y2 = canvas.coords(spaceship)
    if x2 < 600:
        canvas.move(spaceship, spaceship_speed, 0)

# Function to fire a bullet
def fire_bullet(event):
    x1, y1, x2, y2 = canvas.coords(spaceship)
    bullet = canvas.create_rectangle((x1 + x2) / 2 - 2, y1 - 10, (x1 + x2) / 2 + 2, y1, fill="red")
    bullets.append(bullet)
    move_bullet()

# Function to move the bullets
def move_bullet():
    for bullet in bullets:
        canvas.move(bullet, 0, -10)
        # Remove bullet if it moves off-screen
        if canvas.coords(bullet)[1] < 0:
            canvas.delete(bullet)
            bullets.remove(bullet)
    root.after(50, move_bullet)  # Continuously move bullets

# Bind key events to spaceship movement and firing
root.bind("<Left>", move_left)
root.bind("<Right>", move_right)
root.bind("<space>", fire_bullet)

# Start the game loop
root.mainloop()
