import numpy as np
import cv2
from PIL import ImageGrab
try:
    from PIL import Image
except ImportError:
    import Image
import pytesseract
import time as TIME


print("capturing screen and doing work.....")
while 1:
	TIME.sleep(3)

	floor_num = ImageGrab.grab(bbox=(744,414,797,436))    #grabs a screenshot of floor
	image_np = np.array(floor_num)

	bon_num = ImageGrab.grab(bbox=(1000,497,1035,522))    #grabs a screenshot bon %
	image_np2 = np.array(bon_num)

	time_num = ImageGrab.grab(bbox=(732,663,785,688))    #grabs a screenshot time
	image_np3 = np.array(time_num)

	mod_num = ImageGrab.grab(bbox=(1000,518,1032,540))    #grabs a screenshot of mod %
	image_np4 = np.array(mod_num)


	inv_flr = cv2.bitwise_not(image_np)
	inv_bon = cv2.bitwise_not(image_np2)
	inv_time = cv2.bitwise_not(image_np3)
	inv_mod = cv2.bitwise_not(image_np4)


	cv2.imwrite('flr.png',inv_flr)
	cv2.imwrite('bon.png',inv_bon)
	cv2.imwrite('time.png',inv_time)
	cv2.imwrite('mod.png',inv_mod)



	floor = pytesseract.image_to_string('flr.png')
	bon = pytesseract.image_to_string('bon.png')
	time = pytesseract.image_to_string('time.png')
	mod = pytesseract.image_to_string('mod.png')


	winterface = [floor,bon,time,mod]
	print(winterface)
	line = winterface[0] + ' ' + winterface[1]+ ' ' + winterface[2] + ' '+ winterface[3] + '\n'
	blank_line = True

	for i in line:
		if i != ' ':
			blank_line = False

	if blank_line == False:
		log = open("log.txt",'a+')
		log.write(line)
		log.close()
		blank_line = True
input()
