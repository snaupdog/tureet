import tkinter as tk
import math
import serial # For communication with the servo controller

# Function to map values from one range to another
def map_value(value, in_min, in_max, out_min, out_max):
    return (value - in_min) * (out_max - out_min) / (in_max - in_min) + out_min

# Function to handle mouse motion
def motion(event):
    global last_x, last_y
    global servo_x_angle, servo_y_angle

    # Calculate the change in mouse position
    dx = event.x - last_x
    dy = event.y - last_y

    # Update last position
    last_x = event.x
    last_y = event.y

    # Update servo angles based on mouse movement
    servo_x_angle = map_value(event.x, 0, root.winfo_width(), 0, 180)
    servo_y_angle = map_value(event.y, 0, root.winfo_height(), 0, 180)

    # Update servo positions
    update_servos()

# Function to update servos
def update_servos():
    print(type(servo_x_angle))
    ser.write(f"X{180 - int(servo_x_angle)}Y{int(servo_y_angle)}\n".encode())
    pass

def on_key_press(event):
        if event.keysym == "q":
            root.destroy()
# Create a Tkinter window
root = tk.Tk()
root.title("Mouse Control")

root.geometry("600x600")
# Bind mouse motion event to the motion function
root.bind('<Motion>', motion)
root.bind("<KeyPress>", on_key_press)
# Initialize variables
last_x = 0
last_y = 0
servo_x_angle = 90  # Initial angle for servo X
servo_y_angle = 90  # Initial angle for servo Y
ser = serial.Serial("/dev/cu.usbserial-1420", 9600, timeout=0.5)
# Main loop
root.mainloop()
