# Lab6

## Lab Exercises 

- [ ] Use a seaborn pairplot ``sns.pairplot()'' to visualise your data
* ![pairplot](./pairplot.png?raw=true)
- [ ] Loop over different cluster size starting from 2 until 10, using all the features present and pick the one with the lowest silhouette score
* When the clster size is 2, Silhouette Coefficient is 0.284 and it is the lowest of all.
- [ ] Save 10 runs for each cluster size and use a seaborn pointplot without joining the lines
to plot the confidence intervals for the silhouette score
* ![pointplot](./Kmeans.png?raw=true) 
- [ ] Change your clusterer to ``AgglomerativeClustering'' and re-do the above experiment - what do you observe?
* ![pointplot](./Agg.png?raw=true)
* From the pointplot, I can see s_score varies from number of n_cluster. When the cluster number is 6, s_score has the biggest changing range. 