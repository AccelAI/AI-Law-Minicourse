## NYT articles

For this assignment, we will apply the NMF algorithm to a corpus of NYT articles to discover latent topics.  The NYT sections (topics) are great, but we don't know how they relate to patterns in article content.  Let us see what insights we can mine out of our corpus!  We will be starting with our bag of words matrix.  Use the 1405 articles located in the data directory.

### Preliminaries

1. Read the articles.pkl file using the read_pickle function in pandas. Look at the result and understand the structure of your data. Once you are comfortable with the data, store the 'content' series you read in, as this is what we will be working with for the rest of the assignment.


2. Use the [CountVectorizer](http://scikit-learn.org/stable/modules/generated/sklearn.feature_extraction.text.CountVectorizer.html) from scikit-learn (or Tfidf) to turn the content of the news stories into a document-term matrix.  Choose a reasonable value (like 5000) for max_features when initializing the vectorizer.


3. Use the get_feature_names method of your vectorizer to store the word represented by each column of your document-term matrix.

### Implementing your own NMF
With the document matrix (our bags of words), we can begin implementing the NMF algorithm.

1. Create a NMF class that is initialized with a document matrix (bag of words or tf-idf) __V__.  As arguments (in addition to the document matrix) it should also take parameters __k__ (# of latent topics) and the maximum # of iterations to perform.

  First we need to initialize our weights (__W__) and features (__H__) matrices.

2. Initialize the weights matrix (__W__) with positive random values to be a __n x k__ matrix, where __n__ is the number of documents and __k__ is the number of latent topics.

3.  Initialize the feature matrix (__H__) to be __k x m__ where __m__ is the number of words in our vocabulary (i.e. length of bag).  Our original document matrix (__V__) is a __n x m__ matrix.  __NOTICE: shape(V) = shape(W * H)__

4. Next implement your class's `fit()` method. Use a least-squares error metric when we update the matrices __W__ and __H__. This allows us to use the `numpy.linalg.lstsq` solver.
To start, we will update __H__ by calling `lstsq`, holding __W__ fixed and minimizing the sum of squared errors predicting the document matrix. Since these values should all be at least 0, clip all the values in __H__ after the call to `lstsq`.

5. Use the `lstsq` solver to update __W__ while holding __H__ fixed. The `lstsq` solver assumes it is optimizing the right matrix of the multiplication (e.g. x in the equation __Ax=b__). So you will need to get creative so you can use it and have the dimensions line up correctly.  Brainstorm on paper or a whiteboard how to manipulate the matrices so that `lstsq` can get the dimensionality correct and optimize __W__. __hint: it involves transposes.__ Clip __W__ appropriately after updating it with `lstsq` to ensure it is at least 0.

6. Inside your class's `fit()` method, repeat steps 4 and 5 for a fixed number of iterations, or until convergence (i.e. __cost(V, W*H)__ is close to 0).

7. Return the computed weights matrix and features matrix.

### Using Your NMF Function

1. Write a method that uses __W__, __H__, and the document matrix (__V__) to calculate and return the mean-squared error (of __V - WH__).

2. Using argsort on each topic in __H__, find the index values of the words most associated with that topic.  Combine these index values with the word-names you stored in the __Preliminaries__ section to print out the most common words for each topic.


### Built-In NMF


1. Use the scikit-learn NMF algorithm to compute the [Non-Negative Matrix factorization](http://scikit-learn.org/dev/auto_examples/applications/topics_extraction_with_nmf_lda.html) of our documents.  Explore what "topics" are returned.

2. Run the code you wrote for the __Using Your NMF Function__ section on the SKlearn classifier.  How close is the output to what you found using your own NMF classifier?

3. Can you add a title to each latent topic representing the words it contains?

4.  Now that you have labeled the latent features with what topics they represent, explore strongest latent features for a few articles.  Do these make sense given the article? You will have to go back to the raw data you read in to do this.

5. How do the NYT sections compare to the topics from the unsupervised learning?  What are the differences?  Why do you think these differences exist?



#### Extra:


1. Define a function that displays the headlines/titles of the top 10 documents for each topic.
1. Define a function that takes as input a document and displays the top 3 topics it belongs to.
1. Define a function that ensure consistent ordering between your NMF class and the sklearn NMF class.
