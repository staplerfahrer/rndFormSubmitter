from time import time

# Name of decorator
def reportFormJobProgress(worker):
	# Function that runs the worker function:
	def wrapperFn(job):
		print('Job {}...'.format(job['id']))
		timeW = time()
		workResultText = worker(job['form'])
		print('Job {} done in {:.1f} s: {}'.format(
			job['id'],
			time() - timeW,
			workResultText))
	return wrapperFn