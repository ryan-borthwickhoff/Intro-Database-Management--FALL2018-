#!/usr/bin/env python
from mrjob.job import MRJob
class SalaryMax(MRJob):

	def mapper(self, _, line):
		president = str(line.rstrip())
		yield(None, president)
		
	def reducer(self, key, values):
		Presidentlist = []
		for president in Presidentlist:
			preslist.append(salary)
		topten = sorted(salarylist, reverse=True)[0:10]
		for salary in topten:
			yield ("salary", salary)

if __name__ == '__main__':
    SalaryMax.run()