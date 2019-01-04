import requests
import queue
import threading
from time import time
import formGenerator
from decorators import reportFormJobProgress


formPostUrl = 'http://'
formTemplate = \
{
	'staticName1':'staticValue1',
	'staticName2':'staticValue2',
}
workerThreads = 10
numFormsToPost = 100

def main(formPostUrl, formTemplate, workerThreads, numFormsToPost):
	# Worker consumes the queue
	def sender():
		@reportFormJobProgress
		def send(form):
			resp = requests.post(formPostUrl, data=form)
			if resp.status_code != 200:
				print(resp.text)
			return resp.status_code
		
		while True:
			job = q.get()
			if job is None:
				break
			send(job)
			q.task_done()

	timeAllStart = time()

	# Create queue with work to do
	q = buildQueue(formTemplate, numFormsToPost)

	# Threads to launch workers
	threads = []
	for i in range(workerThreads):
		t = threading.Thread(target=sender)
		t.start()
		threads.append(t)
	
	# Block until all threads are done
	q.join()

	for i in range(workerThreads):
		# End worker loops
		q.put(None)
	for t in threads:
		t.join()
	
	print('Total time: {} s'.format(time() - timeAllStart))

def buildQueue(formTemplate, numFormsToPost):
	q = queue.Queue()
	timeQ = time()
	for i in range(numFormsToPost):
		q.put({
			'id': i,
			'form': formGenerator.getForm(formTemplate)
		})
		print('Job built: {}'.format(i))
	print('Queue built in {:.1f} s'.format(time() - timeQ))
	return q

if __name__ == '__main__':
	main(formPostUrl, formTemplate, workerThreads, numFormsToPost)
