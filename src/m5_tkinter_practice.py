"""
This project lets you try out Tkinter/Ttk and practice it!

Authors: David Mutchler, Valerie Galluzzi, Mark Hays, Amanda Stouder,
         their colleagues and Yuanning Zuo.
"""  # Done: 1. PUT YOUR NAME IN THE ABOVE LINE.

import tkinter
from tkinter import ttk


def main():
    """ Constructs a GUI with stuff on it. """
    # ------------------------------------------------------------------
    # Done: 2. After reading and understanding the m1e module,
    #   ** make a window that shows up. **
    # ------------------------------------------------------------------
    window=tkinter.Tk()


    # print("Hello and goodbye!")

    # ------------------------------------------------------------------
    # Done: 3. After reading and understanding the m2e module,
    #   ** put a Frame on the window. **
    # ------------------------------------------------------------------
    frame1=ttk.Frame(window, padding=20,relief='raised')
    frame1.grid()

    thefirstbutton=ttk.Button(frame1,text='Press!')
    thefirstbutton['command']=lambda : print('hello')
    thefirstbutton.grid()




    # ------------------------------------------------------------------
    # Done: 4. After reading and understanding the m2e module,
    #   ** put a Button on the Frame. **
    # ------------------------------------------------------------------

    # ------------------------------------------------------------------
    # Done: 5. After reading and understanding the m3e module,
    #   ** make your Button respond to a button-press **
    #   ** by printing   "Hello"  on the Console.     **
    # ------------------------------------------------------------------
    # print_hello_button=ttk.Button(frame1,text='Print Hello')
    # print_hello_button['command']=lambda : print('hello')

    # ------------------------------------------------------------------
    # Done: 6. After reading and understanding the m4e module,
    #   -- Put an Entry box on the Frame.
    #   -- Put a second Button on the Frame.
    #   -- Make this new Button, when pressed, print "Hello"
    #        on the Console if the current string in the Entry box
    #        is the string 'ok', but print "Goodbye" otherwise.
    # ------------------------------------------------------------------
    entry_box=ttk.Entry(frame1)
    entry_box.grid()

    print_entry=ttk.Button(frame1,text='Print Entry!')
    print_entry['command']=lambda : printcontents(entry_box)
    print_entry.grid()



    # ------------------------------------------------------------------
    # TODO: 7.
    #    -- Put a second Entry on the Frame.
    #    -- Put a third Button on the frame.
    #    -- Make this new Button respond to a button-press as follows:
    #
    #    Pressing this new Button causes the STRING that the user typed
    #    in the FIRST Entry box to be printed N times on the Console,
    #      where N is the INTEGER that the user typed
    #      in the SECOND Entry box.
    #
    #    If the user fails to enter an integer,
    #    that is a "user error" -- do NOT deal with that.
    #
    # ------------------------------------------------------------------
    ####################################################################
    # HINT:
    #   You will need to obtain the INTEGER from the STRING
    #   that the GET method returns.
    #   Use the   int   function to do so, as in this example:
    #      s = entry_box.get()
    #      n = int(s)
    ####################################################################
    another_entry_box=ttk.Entry(frame1)
    another_entry_box.grid()
    print_entry_again=ttk.Button(frame1,text='Printagain!')
    print_entry_again['command']= (lambda:
                                   print_string_multiple_times(entry_box, another_entry_box))
    print_entry_again.grid()

    # ------------------------------------------------------------------
    # TODO: 8. As time permits, do other interesting GUI things!
    # ------------------------------------------------------------------

    window.mainloop()
def printcontents(entry_box):
    print_contents=entry_box.get()
    print(print_contents)


def print_string_multiple_times(string_entry_box, number_entry_box):
    number = int(number_entry_box.get())
    letters = string_entry_box.get()

    for k in range(number):
        print(letters)


# ----------------------------------------------------------------------
# Calls  main  to start the ball rolling.
# ----------------------------------------------------------------------
main()
