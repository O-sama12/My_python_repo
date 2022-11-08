
# Creating a clock using Tkinter

A brief description of Creating a clock using Tkinter. 

Hi all, My name is Osama Abdul Qader. In this python file you'll get 
thecode of "How we can create a clock using Tkinter?".


Using Tkinter we can build a desktop application of any OS (short for Operating System) it may be Linux, Mac, Solaris or Windows etc. 

Now we can't install Tkinter (using pip command) because Tkinter is a built in library that comes with the installation of python in the machine.

 
## Brief explanation of the code

The first line of code creates a new instance of Tkinter object called root which represents the entire application window.
 
 Next, title("Clock") sets what text appears at top center of screen as well as changing its background color from white to black (the default).

 Then pack(anchor="center") places all widgets inside this container into their respective positions relative to each other using anchor values like "top", "left", etc., so they are centered horizontally within their parent widget or container.

 Next comes def time(), where string = strftime('%H:%M:%S %p') converts seconds into hours, minutes and seconds using strftime().

 This allows us to create labels that show different times depending on how long we want them displayed for without having to constantly change

 The code will create a label with the text "Clock" and a red background.

 The label will be placed in the center of the screen and after 1000 milliseconds, it will change to say "Time".

 The mainloop() function is what keeps everything running.
 
 The code starts by creating a Tkinter window called "Clock".

  Next, the code creates a function called time that will print out the current time on the label.

  The label is then created and given an ID of "label" with font size 80 and background color black.

  After 1000 milliseconds, it prints out the time again.

  Finally, mainloop() is executed which starts up ttk's event loop to wait for events to happen in this window.
  

 
