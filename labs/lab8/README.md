# Lab8

* Train a network to do sentiment analysis on IMDB data sets - actual data from here [http://ai.stanford.edu/~amaas/data/sentiment/](http://ai.stanford.edu/~amaas/data/sentiment/)

## Lab Exercises 

- [ ] run ``python imdb.py`` and note somewhere the test accuracy score
It take too much time to run the whole program. The accuracy score of the first Epoch is 0.7582.
- [ ] Modify the code to add one more layer of 64 ``relu`` units after the embedding layer record the score (i.e. add a dense followed by an "activation" layer)
* Codes: x = Embedding(max_features, 64, dropout=0.2)(x)
* The accuracy score of the first Epoch is 0.7093.
- [ ] Modify the code and add a dropout layer after the relu layer
* Codes: x = Dropout(0.2)(x)
* The accuracy score of the first Epoch is 0.7490.
- [ ] Remove the layers you have added previously Convolution layer followed by a relu non-linearity and global max pooling (see lecture notes)
- [ ] Modify the code and add an LSTM layer in place of the convolution layer
- [ ] Use both an LSTM layer and a Convolution layer and merge the results with a Merge layer
* The accuracy score of the first Epoch is 0.7677.
