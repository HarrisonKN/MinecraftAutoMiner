import tkinter as gui
import threading
import time
from movements import *
from mining import *

stopRunning = False

x_MinSize = 500
y_MinSize = 300

mainWindow = gui.Tk() #Creates the GUI Window
mainWindow.title("Python GUI Test") #Gives it a title
mainWindow.minsize(x_MinSize,y_MinSize) #Sets its size to predefined values
mainWindow.resizable(width=True, height=True) #can adjust it with mouse

testEvent = threading.Event()

outputLabel = gui.Label(mainWindow, text="")
outputLabel.grid(row=5,column=0,padx=5,pady=5)

def print_x_output(event=None): #Prints X_Axis input from user
    output_value = x_AxisInput.get()
    x_AxisLabel.config(text=f"X: {output_value}")

def print_y_output(event=None): #Prints Y_Axis input from user
    output_value = y_AxisInput.get()
    y_AxisLabel.config(text=f"Y: {output_value}")

def print_depth_output(event=None): #Prints depth input from user
    output_value = depthInput.get()
    depthLabel.config(text=f"Z: {output_value}")

def print_outputs():
    print_x_output()
    print_y_output()
    print_depth_output()

def update_mouse_position():
    x, y = mouse.get_position()
    mousePositionLabel.config(text=f"Mouse Position: X={x}, Y={y}")
    mainWindow.after(10, update_mouse_position)

def on_run_button_click():
    global testEvent
    global stopRunning
    stopRunning = False
    testEvent.clear()
    threading.Thread(target=run_testing_movements, daemon=True).start()
    

def on_stop_button_click():     
    global stopRunning
    stopRunning = True
    output_label("STOP PRESSED")

def remove_label():
    outputLabel.grid_remove()   

def output_label(message):
    outputLabel.config(text=message)
    mainWindow.after(2000, remove_label)



greeting = gui.Label(mainWindow, text="Welcome to Minecraft Python GUI")
greeting.grid(row=0,column=0,padx=5,pady=5)


x_AxisLabel = gui.Label(mainWindow, text="Enter X Axis = ")
x_AxisLabel.grid(row=1,column=0,padx=5,pady=5)
x_AxisInput = gui.Entry(mainWindow,text="Insert X Axis",width=25)
x_AxisInput.grid(row=1,column=1,padx=5,pady=5)
x_AxisInput.bind("<Return>", print_x_output)
x_AxisLabel = gui.Label(mainWindow,text="X:", width=10)
x_AxisLabel.grid(row=3,column=3,padx=5,pady=5)

y_AxisLabel = gui.Label(mainWindow, text="Enter Y Axis = ")
y_AxisLabel.grid(row=2,column=0,padx=5,pady=5)
y_AxisInput = gui.Entry(mainWindow, width=25)
y_AxisInput.grid(row=2,column=1,padx=5,pady=5)
y_AxisInput.bind("<Return>", print_y_output)
y_AxisLabel = gui.Label(mainWindow, text="Y:")
y_AxisLabel.grid(row=1,column=2,padx=5,pady=5)

depthLabel = gui.Label(mainWindow, text="Enter Depth = ")
depthLabel.grid(row=3,column=0,padx=5,pady=5)
depthInput = gui.Entry(mainWindow, width=25)
depthInput.grid(row=3,column=1,padx=5,pady=5)
depthInput.bind("<Return>", print_depth_output)
depthLabel = gui.Label(mainWindow, text="Z:")
depthLabel.grid(row=1,column=3,padx=5,pady=5)

zeroLabel = gui.Label(mainWindow,text="0",width=10)
zeroLabel.grid(row=3,column=2,padx=5,pady=5)


run_button = gui.Button(
    mainWindow,
    text = "RUN",
    command=lambda:[on_run_button_click(),print_outputs()],
    width=10,
    height=2,
    bg="blue",
    fg="white"
)
run_button.grid(row=4,column=0,padx=5,pady=5)

stop_button = gui.Button(
    mainWindow,
    text = "STOP",
    command=on_stop_button_click,
    width=10,
    height=2,
    bg="blue",
    fg="white"
)
stop_button.grid(row=4,column=1,padx=5,pady=5)


mousePositionLabel = gui.Label(mainWindow, text="Mouse Position: X=0, Y=0")
mousePositionLabel.grid(row=6,column=0,padx=5,pady=5)
update_mouse_position()


def run_testing_movements():
    output_label("Testing Movement Starting")
    time.sleep(5)

    while not stopRunning:
        output_label("BEGIN")
        testMineChunk(int(x_AxisInput.get()), int(y_AxisInput.get()), stopRunning)



mainWindow.mainloop()