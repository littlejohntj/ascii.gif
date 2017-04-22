import subprocess
import os
import sys
import time
import threading

def worker():
	j = 0
	while True:
		subprocess.call(['clear'])
		print frame_dict[j]
		time.sleep(0.05)
		j += 1
		j %= frame_count

def start_thread():
	thread = threading.Thread(target=worker, args=())
	thread.daemon = True
	thread.start()

frame_dict = {}
i = 0

gif_name = raw_input("Enter the name of the GIF: ")
subprocess.call(["convert", gif_name, "frames%03d.png"])
frames = filter(lambda x: 'frames' in x,  os.listdir(os.getcwd()))
frame_count = len(frames)

raw_input("Get ready for the GIF!! Press enter when ready!! (It looks best if you shrink your text)")

for frame in frames:
	with open('out-file.txt', 'w') as f:
	    subprocess.call(['img2txt.py', frame], stdout=f)
	with open('out-file.txt', 'r') as f:
		frame_dict[i] = '\n'.join([" ".join(list(l)) for l in f.read().split('<pre>')[1].split('</pre>')[0].split('\n')])
		print frame_dict[i]
		i += 1

start_thread()

while True:
	raw_input()
	break

for frame in frames:
		os.remove(frame)

subprocess.call(['clear'])
os.remove('out-file.txt')








