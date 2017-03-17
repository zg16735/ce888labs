# Lab5

## Lab Exercises 

- [ ] Load the data from the file ``jester-data-1.csv'
- [ ] Split the data into validation, test and training set with 80:10:10 proportions
* Use numpy split function to divide the data into three parts
- [ ] Use latent factor modelling to infer the hidden ratings of the users (they are labelled as "99" in the dataset) on the training set

- [ ] Calculate the performance of the algorithm in the validation dataset by looping through the dataset without training
- [ ] Change hyper-parameters (i.e. learning rates, number of iterations etc) as needed so you can get good results
- [ ] Report the MSE on the test dataset
- [ ] Use pandas to find the best and the worst rated jokes
