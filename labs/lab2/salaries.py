import matplotlib
matplotlib.use('Agg')

import pandas as pd
import random
import matplotlib.pyplot as plt
import seaborn as sns

import numpy as np 




# def permutation(statistic, error):


def mad(arr):
    """ Median Absolute Deviation: a "Robust" version of standard deviation.
        Indices variabililty of the sample.
        https://en.wikipedia.org/wiki/Median_absolute_deviation 
        http://stackoverflow.com/questions/8930370/where-can-i-find-mad-mean-absolute-deviation-in-scipy
    """
    arr = np.ma.array(arr).compressed() # should be faster to not use masked arrays.
    med = np.median(arr)
    return np.median(np.abs(arr - med))


if __name__ == "__main__":
	#df = pd.read_csv('./customers.csv')
	df = pd.read_csv('./vehicles.csv')
	print df.columns
	sns_plot = sns.lmplot(df.columns[0], df.columns[1], data=df, fit_reg=False)

	sns_plot.axes[0,0].set_ylim(0,)
	sns_plot.axes[0,0].set_xlim(0,)

	sns_plot.savefig("scaterplot.png",bbox_inches='tight')
	sns_plot.savefig("scaterplot.pdf",bbox_inches='tight')

	data1 = df.values.T[0][0:79]
	data = df.values.T[1][0:79]
	
	print ("Mean: %f")%(np.mean(data1))
	print ("Median: %f")%(np.median(data1))
	print ("Var: %f")%(np.var(data1))
	print ("std: %f")%(np.std(data1))
	print ("MAD: %f")%(mad(data1))
	
	print ("Mean: %f")%(np.mean(data))
	print ("Median: %f")%(np.median(data))
	print ("Var: %f")%(np.var(data))
	print ("std: %f")%(np.std(data))
	print ("MAD: %f")%(mad(data))

	plt.clf()
	sns_plot2 = sns.distplot(data1, bins=20, kde=False, rug=True).get_figure()

	axes = plt.gca()
	axes.set_xlabel('Current fleet') 
	axes.set_ylabel('Fleet count')

	sns_plot2.savefig("current histogram.png",bbox_inches='tight')
	sns_plot2.savefig("current histogram.pdf",bbox_inches='tight')
	
	plt.clf()
	sns_plot3 = sns.distplot(data, bins=20, kde=False, rug=True).get_figure()
	
	axes = plt.gca()
	axes.set_xlabel('New fleet') 
	axes.set_ylabel('Fleet count')
	
	sns_plot3.savefig("new histogram.png",bbox_inches='tight')
	sns_plot3.savefig("new histogram.pdf",bbox_inches='tight')


	