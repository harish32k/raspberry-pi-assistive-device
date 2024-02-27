from detector import model_run
import threading

class thread(threading.Thread):
	def __init__(self, thread_name, thread_ID):
		threading.Thread.__init__(self)
		self.thread_name = thread_name
		self.thread_ID = thread_ID
		self.runvar = [True]
		
	def run(self):
		model_run(self.runvar)


if __name__ == '__main__':			
	thread1 = thread("cap_thread", 1000)
	thread1.start()
	import time
	for i in range(22):
		print("At", i)
		time.sleep(1)
	thread1.runvar[0] = False
	print("exit")
