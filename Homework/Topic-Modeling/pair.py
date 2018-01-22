import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import TfidfVectorizer
import matplotlib.pyplot as plt


class nmf(object):
	def __init__(self):
		
		self.W = None
		self.H = None
		self.n = V.shape[0]
		self.m = V.shape[1]
		
		self.error = []

	def fit(self, V, k=None):
		self.V = V.todense()

		self.k = int(self.m * 0.5) if k == None else k
		self.init()

		for i in range(10):
			print i
			out = np.linalg.lstsq(a=self.W, b=self.V)
			self.H = out[0]
			self.H = self.force_to_zero(self.H)

			out = np.linalg.lstsq(a=self.H.T, b=self.V.T)
			self.W = out[0].T
			self.W = self.force_to_zero(self.W)
			
			self.compute_error()

	def force_to_zero(self, H):
		for i in xrange(H.shape[0]):
			H[i][H[i] < 0] = 0
		return H

	def init(self):
		self.W = np.random.random((self.n, self.k))

	def compute_error(self):
		e = self.V - self.W.dot(self.H)
		self.error.append(np.sum(np.square(e)))


if __name__ == '__main__':
	df = pd.read_pickle('data/articles.pkl')
	corpus = df.content.values
	v = TfidfVectorizer(max_features=5000,stop_words='english')
	V = v.fit_transform(corpus)
	features = v.get_feature_names()


	n = nmf()
	n.fit(V)

	plt.ion()
	plt.show()
	fig = plt.plot(figsize=(12,6))
	plt.plot(n.error)





