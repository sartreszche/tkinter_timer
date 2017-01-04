# tutorial code from https://docs.python.org/2/library/tkinter.html#a-simple-hello-world-program
#
# In using Tkinter for the first time, 
# I had trouble getting Tkinter import 
# to work in Windows 10.
#
# Note the following:
# 1.  32-bit version of Python is recommended
# 2.  Make sure to add Python installation folder
#      to your path in Windows
# 3.  You may need to try an earlier version of
#      Python (v. 2.7.13 fails to install for me
#       at this time but 2.7.12 succeeds.)
# 4.  'tkinter' is the package name
#	   for Python v. 3.x while 'Tkinter' is 
#       the package name for v. 2.x 
# Tkinter timer 2

from Tkinter import *

class Application(Frame):
	def say_hi(self):
		print "Hello world!"

	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		self.QUIT.pack({"side": "left"})

		self.hi_there = Button(self)
		self.hi_there["text"] = "Hello",
		self.hi_there["command"] = self.say_hi

		self.hi_there.pack({"side": "left"})

	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()

root = Tk()
app = Application(master=root)
app.mainloop()
root.destroy()
