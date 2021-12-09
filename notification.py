import time 
from plyer import notification 
if __name__ == '__main__':
	while True:
		notification.notify(
		title = "Kindly have some break",
		message ="Walking and some physical activity is necessary for the body as sitting against the screen may harm your body on long run.",
		app_icon = r"C:\Users\DELL\Downloads\walk.ico",
		timeout= 5
		)
		time.sleep(3600)