from pynput.mouse import Button,Controller
from pynput import keyboard
import pyautogui
while True:
	def newtab():
		cords = pyautogui.locateCenterOnScreen(r"C:\Users\admin\Downloads\Minecraft_hook1.png")
		print(cords)
		
	newtab()



#mouse = Controller()
#mouse.click(Button.left,1)
