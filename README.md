# AI & Law Mini-Course
 
## Logistics

- Date: Jan 22nd & 29th
- Location: Santa Clara University
- Time: 100 min & 4 hours of homework / session
- Audience: Graduate and Undergraduate (Non-CS major) Students
- Project: Topic Modeling of Supreme Court Documents 
 
## Description

The AI and Law Mini-course is designed to expose students to real-world use cases of Artificial Intelligence in law practice. We'll begin with a high-level overview of artificial intelligence concepts and techniques, then walk through an applied example of topic modeling for supreme court cases using Natural Language Processing. You'll also learn where to find public datasets for use in future research and applications.
 
## Setup

Make sure to follow the [AI-Workshop-Installation-Guides](https://github.com/AccelAI/AI-Workshop-Installation-Guides) to get your computer set up for the applied lab and homework sessions.

### Pull the Latest Version of this Repository

```
git pull origin master
```

## Mac OSX & Windows

Refer to this guide from Github for help - [Cloning a repository](https://help.github.com/articles/cloning-a-repository/#platform-mac)

**For Windows**

Download Git command prompt - https://git-scm.com/downloads


### Clone this Repository

Execute the following command in your terminal or git command prompt.

```
git clone https://github.com/AccelAI/AI-Law-Minicourse.git
```

If you are using the [Github desktop](https://services.github.com/on-demand/github-desktop/clone-repository-github-desktop):

1. Sign in to GitHub.com and GitHub Desktop.
2. On GitHub.com, navigate to the Code tab of the repository.
3. On the right side of the screen, click Clone or download.
4. Click Open in Desktop. This will open GitHub Desktop.
5. Select where you’d like to save it locally under Local Path
6. Click Clone.


### Docker (Optional)

If you are using Docker to access the Anaconda distribution:

Start Docker, e.g., using spotlight search (by pressing the cmd + space bar) or Finder to navigate to your Applications folder and double-clicking on the Docker icon

**Open Workshop Repository**

Open a new terminal window by pressing **cmd + t** and move into the workshop directory by executing:

```
cd ~/AI-Law-Minicourse
```

**If this command returns an error, your directory is located in a different file path** 



**Link Cloned Github Repository to Docker**

Link this directory to your Docker container by executing:

```
docker run -it --rm --name ai-law -v ~/AI-Law-Minicourse -p 8888:8888 -p 6006:6006
```

More details on sharing files from your local machine into a Docker container can be found here: https://github.com/rocker-org/rocker/wiki/Sharing-files-with-host-machine

### Installation Issues

Virtual Office Hours for students who struggle with downloads on Anaconda distribution locally or through Docker.

**Your computer must be set up to run an Anaconda distribution through Docker or locally prior to our first session on January 22nd** 

If you have a problem following the installation guides, set an appointment for a 15 min troubleshooting session - https://calendly.com/accelai/15min-technical/.


# Join Slack

Join our slack channel - http://bit.ly/accelai-slack. Once in slack, you'll receive an invite to the private channel setup for this course. We'll be sending any additional materials through the private slack channel.
 
# Table of Contents

## Session 1 Concepts
- Artificial Intelligence Overview
- Is AI taking over?
- Computational Law
- Moral & Ethical Dilemmas
- Data Collection
- Data Quality
- NLP Applied to Law
- Applied Example - Supreme Court Cases
- Assign Homework


## Session 2 Concepts
- What is Deep Learning?
- The rise of Deep Learning
- Convolutional Neural Networks
- Deep Learning for NLP
- Homework Review



# Homework

## Assignments

- Setup a Github Account
    * [Fork](https://guides.github.com/activities/forking/) this repository into your Github
    * Create a new repository called "AI-Law-Minicourse-HW"
    * Clone the **AI-Law-Minicourse-HW** to your local machine
    * Add a **Readme.md** where you'll be adding your notes for the homework
    * Apply [Markdown Formatting](https://guides.github.com/pdfs/markdown-cheatsheet-online.pdf) to this document along with your answers
    * Push the file from your local repository on your computer to the master branch on Github
        - Refer to the Github resources listed below if you get stuck! 

- Review the Applied Example covered in class - [Supreme Court Topic Modeling](./Supreme_Court_Topic_Modeling/)
    * For each step in this directory, write a paragraph or two of your interpretation of the code - in your own words describing what the code is doing
    * Include a description of the workflow being applied, what format the data is in during each step, what each function is doing, etc

- [Complete the Tutorial - Vector Representation of Words using TensorFlow](https://www.tensorflow.org/tutorials/word2vec)
    * Launch an empty Jupyter Notebook in your new **AI-Law-Minicourse-HW** local repository
        - If you downloaded Docker and are using the Docker-Hub image of Anaconda, you'll need to connect your new repository to your Docker instance
        - If you downloaded Anaconda locally, you should be able to launch jupyter notebook from the local directory and have access to the needed scientific packages
    * Make sure to import tensorflow into the Jupyter Notebook
    * Add the code from this tutorial in your new Jupyter Notebook, make sure it executes as decribed
        - Save your work intermittently
    * Push your saved work from your local repository to the Github repository for assessment
        - Successfult completion of this tutorial includes completing a push to Github with your new Jupyter Notebook which has run all the code in this tutorial.


## Reading & Videos

### Session 1

- [Computational law, symbolic discourse, and the AI constitution](https://www.wired.com/2016/10/computational-law-symbolic-discourse-and-the-ai-constitution/)

This article helps you to understand the semantics involved in applying written or human law to a format that can be understood by a computer. It also introduces ideas around *smart contracts* utlizing Blockchain technology.


- [From Data to AI - Machine Learning Canvas](https://medium.com/louis-dorard/from-data-to-ai-with-the-machine-learning-canvas-part-i-d171b867b047)

Make sure you understand the workflow process and each segment of the Machine Learning Canvas. As part of your assessment, you'll be given a Legal AI example and expected to fill out the Canvas to satisfy the end goal.

- [Topic Modeling With Python Video Lecture](https://youtu.be/BuMu-bdoVrU)
    * Watch the video on 1.5x or 2x speed
    * First half has the most relevant information for your understanding - watch up to 27:00 minutes.

Watch this video for an indepth explanation of Topic Modeling and algorithms applied in topic modeling. You'll be assessed on your understanding of NMF and TFIDF techniques.

    
- [Wisdom of the Crowd Predicts Supreme Court Decisions](https://www.technologyreview.com/s/609852/wisdom-of-the-crowd-accurately-predicts-supreme-court-decisions/?set=)

This article is intended to inspire you regarding the possibilities of applying AI and Machine Learning techniques to law and politics.

- [A Beginners Guide to Deep Learning](https://youtu.be/nCPf8zDJ0d0)
    * Watch the video on 1.5x or 2x speed

This lecture will prime you for a indepth overview of Deep Learning which we'll be covering in session 2 of this minicourse.


 
### Session 2
- [Improving Decision Analytics with Deep Learning: The Case of Financial Disclosures](https://arxiv.org/pdf/1508.01993.pdf)

- [New Theory Cracks Open the Black Box of Deep Learning](https://www.quantamagazine.org/new-theory-cracks-open-the-black-box-of-deep-learning-20170921)
    * [Related Video: Information Theory of Deep Learning by Naftali Tishby](https://youtu.be/bLqJHjXihK8)

- Assessment - How much did you learn? Vocabulary, Fluency, Context.

## Supplemental Materials

### Assignments

These are available for students who take a keen interest in applying the code themselves:
- [Topic Modeling in SciKit Learn](/Homework/Topic-Modeling/)



### Readings

- [How Machines Learn to Be Racist - Propublica](https://www.propublica.org/article/breaking-the-black-box-what-facebook-knows-about-you)
- [Machine Learning Basics, Ch 5 Deep Learning Book](http://www.deeplearningbook.org/contents/ml.html)
- [Deep Learning Applications NLP, Ch 12 Pg 456 - 473 of Deep Learning Book](http://www.deeplearningbook.org/contents/applications.html)

### Deep Learning Tutorials

- Deep Learning tutorials: http://deeplearning.net/tutorials
- Stanford deep learning tutorials with simple programming assignments and reading list http://deeplearning.stanford.edu/wiki/
- Recursive Autoencoder class project: 
    http://cseweb.ucsd.edu/~elkan/250B/learningmeaning.pdf
- Graduate Summer School: Deep Learning, Feature Learning:
    http://www.ipam.ucla.edu/programs/gss2012/
- ICML 2012 Representation Learning tutorial: 
    http://www.iro.umontreal.ca/~bengioy/talks/deep-learning-tutorial2012.html

 
### Computing Resources
- Python
    * [Codeacademy Learn Python](https://www.codecademy.com/learn/learn-python)
    * [Python 3 Basics Tutorial Series](https://www.youtube.com/playlist?list=PLQVvvaa0QuDe8XSftW-RAxdo6OmaeL85M)

- Anaconda Distribution
    * [Anaconda Docs Getting Started Guide](https://conda.io/docs/user-guide/getting-started.html)

- Jupyter Notebook
    * [Jupyter/IPython Notebook Quick Start Guide](https://jupyter-notebook-beginner-guide.readthedocs.io/en/latest/)
    * [Jupyter Notebook Tutorial: The Definitive Guide](https://www.datacamp.com/community/tutorials/tutorial-jupyter-notebook)
    * [Running Tensorflow in Jupyter Notebook - StackOverflow](https://stackoverflow.com/questions/43216256/running-tensorflow-in-jupyter-notebook)
    * [Jupyter Notebook Tutorial: Introduction, Setup, and Walkthrough](https://www.youtube.com/watch?v=HW29067qVWk)

- Web Scraping
    * [Web Scraping with Python Cheat Sheet](https://blog.hartleybrody.com/web-scraping-cheat-sheet/)

- Github
    * [How to Collaborate On GitHub](https://code.tutsplus.com/tutorials/how-to-collaborate-on-github--net-34267)
    * [GitHub Collaboration Best Practices](https://github.com/ideaconsult/etc/wiki/GitHub-Collaboration-Best-Practices)
    * [Collaboration with Git and GitHub Video](https://youtu.be/SCZF6I-Rc4I)

- Command Line
    * [Codecademy Learn the Command Line](https://www.codecademy.com/courses/learn-the-command-line/lessons/navigation/exercises/your-first-command)
    * [Mac Terminal Cheat Sheet](https://skillcrush.com/wp-content/uploads/2016/04/1a-TerminalCommandsCheatsheetMac.pdf)
    * [Windows Command Line Cheat Sheet](http://www.cs.columbia.edu/~sedwards/classes/2015/1102-fall/Command%20Prompt%20Cheatsheet.pdf)
 
 
### Civic Data Resources
- [Data.gov](https://www.data.gov/)
- [Free Law Project](https://free.law/)
- [usa.gov/statistics](https://www.usa.gov/statistics)
- SEC Filings - You can get all SEC filings that public companies make on the SEC's website: https://www.sec.gov/edgar/searchedgar/companysearch.html
- Here's a scraper that'll grab different types of SEC filings in bulk from the SEC website: https://github.com/javedqadruddin/EDGAR
 
# References
- Topic Modeling of Supreme Court Documents:
https://github.com/emilyinamillion/supreme-court-topics-overtime
- NLP in Python:
https://www.analyticsvidhya.com/blog/2017/01/ultimate-guide-to-understand-implement-natural-language-processing-codes-in-python/
- Non Negative Matrix Factorization:
https://en.wikipedia.org/wiki/Non-negative_matrix_factorization
- TF-IDF: http://www.tfidf.com/

