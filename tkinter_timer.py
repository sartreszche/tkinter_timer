# Tkinter timer

from Tkinter import *
import time

class Application(Frame):
	"""
	Creates a frame and adds button and canvas to display timer count
	"""
	
	def createWidgets(self):
		self.QUIT = Button(self)
		self.QUIT["text"] = "Quit"
		self.QUIT["fg"] = "red"
		self.QUIT["command"] = self.quit
		self.QUIT.pack({"side": "left"})

		self.start_timer = Button(self)
		self.start_timer["text"] = "Start"
		self.start_timer["command"] = self.start_timer

		self.start_timer.pack({"side": "left"})

		self.stop_timer = Button(self)
		self.stop_timer["text"] = "Stop"
		self.stop_timer["command"] = self.stop_timer

		self.stop_timer.pack({"side": "left"})

		self.reset_timer = Button(self)
		self.reset_timer["text"] = "Reset"
		self.reset_timer["command"] = self.reset_timer

		self.reset_timer.pack({"side": "left"})


	def __init__(self, master=None):
		Frame.__init__(self, master)
		self.pack()
		self.createWidgets()


class Timer():
	"""
	Timer class which creates a timer and has start, stop and reset methods
	"""
	def __init__(self, func=time.perf_counter):
		display_time = 0.0
		self._func = func
		self._start = None

	def start(self):
		if self._start is not None:
			raise RuntimeError("Already started")
		self._start = self._func()

	def stop(self):
		pass

	def reset():
		pass	


root = Tk()
app = Application(master=root)
app.mainloopd()
root.destroy()
