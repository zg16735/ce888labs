# Lab7

## Lab setup

Type the following in the command prompt (connect remotely via ``ssh mlvm@mlvm``)

* ``pip install --upgrade tensorflow``
* ``pip install --upgrade keras`` 

* Train a neural network to learn how to perform classification of images from mnist - see here [https://www.kaggle.com/c/digit-recognizer/leaderboard](https://www.kaggle.com/c/digit-recognizer/leaderboard)

## Lab Exercises 

- [ ] run ``python mnist.py`` and note somewhere the test accuracy score
* The test accuracy score is 0.9286.
- [ ] Modify the code to add one more layer of 64 ``relu`` units and record the score
* The score is 0.9739.
- [ ] Modify the code so that you are able to add as many layers of ``relu`` units as you want, controlled by a variable called ``n_hidden_layers``
- [ ] Add a Dropout layer with strength of 0.5
- [ ] Play around with different scores and optimise on the number of layers, trying to find the optimal hyperparameters
* I change the number of hidden_layers to 3 and add 128 dense layer. The val_acc in the end is 0.9801, which is bigger than 0.98. 
  I think I have the optimal hyperparameters. 

