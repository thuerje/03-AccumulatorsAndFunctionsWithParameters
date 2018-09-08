"""
This module lets you practice  ** using objects **, including:
  -- CONSTRUCTING objects,
  -- applying METHODS to them, and
  -- accessing their DATA via INSTANCE VARIABLES

Authors: David Mutchler, Dave Fisher, Vibha Alangar, Mark Hays, Amanda Stouder,
         their colleagues and Jess Thuer.
"""  # DONE PUT YOUR NAME IN THE ABOVE LINE.

import rosegraphics as rg


def main():
    """ Calls the other functions to demonstrate and/or test them. """
    # Test your functions by putting calls to them here:

    two_circles()
    circle_and_rectangle()
    lines()


def two_circles():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws two rg.Circle objects on the window
         such that:
           -- They fit in the window and are easily visible.
           -- They have different radii.
           -- One is filled with some color and one is not filled.
    -- Waits for the user to press the mouse, then closes the window.
    """
    # ------------------------------------------------------------------
    # DONE Implement this function, per its green doc-string above.
    #    -- ANY two rg.Circle objects that meet the criteria are fine.
    #    -- File  COLORS.pdf  lists all legal color-names.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    # ------------------------------------------------------------------

    window = rg.RoseWindow(500,500)

    center_point1 = rg.Point(400,150)
    circle1 = rg.Circle(center_point1,50)
    circle1.fill_color = 'turquoise'
    circle1.attach_to(window)
    center_point2 = rg.Point(150,250)
    circle2 = rg.Circle(center_point2,100)
    circle2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

def circle_and_rectangle():
    """
    -- Constructs an rg.RoseWindow.
    -- Constructs and draws a rg.Circle and rg.Rectangle
       on the window such that:
          -- They fit in the window and are easily visible.
          -- The rg.Circle is filled with 'blue'
    -- Prints (on the console, on SEPARATE lines) the following data
         associated with your rg.Circle:
          -- Its outline thickness.
          -- Its fill color.
          -- Its center.
          -- Its center's x coordinate.
          -- Its center's y coordinate.
    -- Prints (on the console, on SEPARATE lines) the same data
         but for your rg.Rectangle.
    -- Waits for the user to press the mouse, then closes the window.

    Here is an example of the output on the console,
    for one particular circle and rectangle:
           1
           blue
           Point(180.0, 115.0)
           180
           115
           1
           None
           Point(75.0, 150.0)
           75.0
           150.0
    """
    # ------------------------------------------------------------------
    # DONE Implement this function, per its green doc-string above.
    #   -- ANY objects that meet the criteria are fine.
    # Put a statement in   main   to test this function
    #    (by calling this function).
    #
    # IMPORTANT: Use the DOT TRICK to guess the names of the relevant
    #       instance variables for outline thickness, etc.
    # ------------------------------------------------------------------

    print()
    print('--------------------------------------------------')
    print('Circle and Rectangle:')
    print('--------------------------------------------------')

    window = rg.RoseWindow(500,500)

    cc_x = 400
    cc_y = 150
    circle_center_point = rg.Point(cc_x,cc_y)
    circle = rg.Circle(circle_center_point,50)
    circle.fill_color = 'Blue'
    circle.attach_to(window)
    print(circle.outline_thickness)
    print(circle.fill_color)
    print(circle.center)
    print(cc_x)
    print(cc_y)

    rc1 = rg.Point(50,250)
    rc2 = rg.Point(250,400)
    rectangle = rg.Rectangle(rc1,rc2)
    rectangle.attach_to(window)
    center_point = rectangle.get_center()
    print(rectangle.outline_thickness)
    print(rectangle.fill_color)
    print(rectangle.get_center())
    print(center_point.x)
    print(center_point.y)

    window.render()
    window.close_on_mouse_click()


def lines():
    """
    -- Constructs a rg.RoseWindow.
    -- Constructs and draws on the window two rg.Lines such that:
          -- They both fit in the window and are easily visible.
          -- One rg.Line has the default thickness.
          -- The other rg.Line is thicker (i.e., has a bigger width).
    -- Uses a rg.Line method to get the midpoint (center) of the
         thicker rg.Line.
    -- Then prints (on the console, on SEPARATE lines):
         -- the midpoint itself
         -- the x-coordinate of the midpoint
         -- the y-coordinate of the midpoint

       Here is an example of the output on the console, if the two
       endpoints of the thicker line are at (100, 100) and (121, 200):
            Point(110.5, 150.0)
            110.5
            150.0

    -- Waits for the user to press the mouse, then closes the window.
    """
    # DONE Implement and test this function.

    print()
    print('--------------------------------------------------')
    print('Lines:')
    print('--------------------------------------------------')

    window = rg.RoseWindow(500,500)

    L1P1 = rg.Point(100,100)
    L1P2 = rg.Point(300,150)
    line1 = rg.Line(L1P1,L1P2)
    mid_point1 = line1.get_midpoint()
    print(mid_point1)
    print(mid_point1.x)
    print(mid_point1.y)
    line1.attach_to(window)

    L2P1 = rg.Point(200,250)
    L2P2 = rg.Point(100,350)
    line2 = rg.Line(L2P1,L2P2)
    line2.thickness = 3
    mid_point2 = line2.get_midpoint()
    print(mid_point2)
    print(mid_point2.x)
    print(mid_point2.y)
    line2.attach_to(window)

    window.render()
    window.close_on_mouse_click()

# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
