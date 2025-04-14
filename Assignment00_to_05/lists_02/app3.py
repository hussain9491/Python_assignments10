from graphics import Canvas
import time

# Constants for the canvas size and cell size
CANVAS_WIDTH: int = 400
CANVAS_HEIGHT: int = 400
CELL_SIZE: int = 40
ERASER_SIZE: int = 20

def erase_objects(canvas, eraser):
    """Erase objects in contact with the eraser"""
    # Get mouse info to help us know which cells to delete
    mouse_x = canvas.get_mouse_x()
    mouse_y = canvas.get_mouse_y()
    
    # Calculate where our eraser is
    left_x = mouse_x
    top_y = mouse_y
    right_x = left_x + ERASER_SIZE
    bottom_y = top_y + ERASER_SIZE
    
    # Find things that overlap with our eraser
    overlapping_objects = canvas.find_overlapping(left_x, top_y, right_x, bottom_y)
    
    # For everything that overlaps with our eraser (that isn't our eraser), change
    # its color to white
    for overlapping_object in overlapping_objects:
        if overlapping_object != eraser:
            canvas.set_color(overlapping_object, 'white')

def main():
    # Initialize the canvas with the given width and height
    canvas = Canvas(CANVAS_WIDTH, CANVAS_HEIGHT)
    
    # Calculate the number of rows and columns of cells
    num_rows = CANVAS_HEIGHT // CELL_SIZE
    num_cols = CANVAS_WIDTH // CELL_SIZE
    
    # Create a grid of blue cells
    for row in range(num_rows):
        for col in range(num_cols):
            left_x = col * CELL_SIZE
            top_y = row * CELL_SIZE
            right_x = left_x + CELL_SIZE
            bottom_y = top_y + CELL_SIZE
            
            # Create a rectangle (cell) on the canvas
            cell = canvas.create_rectangle(left_x, top_y, right_x, bottom_y, 'blue')
    
    # Wait for the user to click on the canvas to create the eraser
    canvas.wait_for_click()  # Wait for the user to click before creating the eraser
    
    # Get the starting location for the eraser from the user's click
    last_click_x, last_click_y = canvas.get_last_click()
    
    # Create the eraser as a pink rectangle at the clicked position
    eraser = canvas.create_rectangle(
        last_click_x, 
        last_click_y, 
        last_click_x + ERASER_SIZE, 
        last_click_y + ERASER_SIZE, 
        'pink'
    )
    
    # Move the eraser with the mouse and erase objects in its path
    while True:
        # Get the mouse coordinates and move the eraser to those coordinates
        mouse_x = canvas.get_mouse_x()
        mouse_y = canvas.get_mouse_y()
        canvas.moveto(eraser, mouse_x, mouse_y)
        
        # Erase anything touching the eraser
        erase_objects(canvas, eraser) 
        
        # Sleep briefly to make the eraser movement visible and avoid high CPU usage
        time.sleep(0.05)

# Run the program
if __name__ == '__main__':
    main()
