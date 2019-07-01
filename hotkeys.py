from pynput import keyboard
import time
from os import system
from sys import platform

class HotKeys:
	def __init__(self, route):
		self.current = set()
		self.route = route
		self.COMBINATIONS = [
			{keyboard.Key.alt, keyboard.KeyCode(char='m')}
	]
		listener = keyboard.Listener(on_press=self.on_press,on_release=self.on_release)
		listener.start()

	def execute(self):
		route = self.route
		print(type(route))
		if self.current == self.COMBINATIONS[0]:
			self.clear()
			return route()
		else:
			print('pressed but not sent')

	def on_press(self, key):
		if any([key in COMBO for COMBO in self.COMBINATIONS]):
			self.current.add(key)
			if any(all(k in self.current for k in COMBO) for COMBO in self.COMBINATIONS):
				self.execute()

	def on_release(self, key):
		if any([key in COMBO for COMBO in self.COMBINATIONS]):
			self.current.remove(key)

	def clear(self):
		if platform == 'win32':
			system('cls')
		else:
			system('clear')
