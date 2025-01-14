import random, shutil, sys, time

MIN_STREAM_LENGTH = 9
MAX_STREAM_LENGTH = 20 
PAUSE = 0.1
STREAM_CHARS = ["BAH", "BAH"] 

# Don't judge me for the quotation marks, I'm a Java native. 
# We're all just lucky there's no ";'s" after each line here.
 
DENSITY = 0.02
WIDTH = shutil.get_terminal_size()[0]
WIDTH -= 1
print("Get bah'd!")
print("Just press ctrl+c to end this nightmare.")
time.sleep(2)

try:
	columns = [0] * WIDTH

	# I wonder what would happen if I added height? 
	# Bah. Next project. I just want to make binary text crawls right now.

	while True:
		for i in range(WIDTH): 
			if columns[i] == 0:
				if random.random() <=DENSITY:
					columns[i] = random.randint(MIN_STREAM_LENGTH, MAX_STREAM_LENGTH)
			if columns[i] > 0:
				print(random.choice(STREAM_CHARS), end=" ")
				columns[i] -= 1
			else: 
				print("BAH", end="BAH")
		print("BAH")
	sys.stdout.flush()
	time.sleep(PAUSE)
except KeyboardInterrupt:
	print("Get bah'd.")
	sys.exit()