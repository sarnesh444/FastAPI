# FastAPI
A Python library to build APIs real quick!

[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

### Input Code 
![alt text](https://github.com/sarnesh444/FastAPI/blob/master/basecode.JPG)

### Sample Output
![alt text](https://github.com/sarnesh444/FastAPI/blob/master/browser.JPG)

![alt text](https://github.com/sarnesh444/FastAPI/blob/master/postman.JPG)

## Tools used

* [FastAPI](https://fastapi.tiangolo.com/) a python package that can help build robust APIs real quick.

* [Numpy](https://numpy.org/) NumPy is a library for the Python programming language, adding support for large, multi-dimensional arrays and matrices, along with a large collection of high-level mathematical functions to operate on these arrays.

* [Pickle](https://docs.python.org/2/library/pickle.html) “Pickling” is the process whereby a Python object hierarchy is converted into a byte stream, and “unpickling” is the inverse operation, whereby a byte stream (from a binary file or bytes-like object) is converted back into an object hierarchy.

## Prerequisites

This repo assumes you use Python 3.x.

### Dependencies
Install the dependencies using PIP the package manager for python

```
pip install uvicorn
pip install fastapi
```

### Additonal

* Model Building
  * Build your ML model like this [one](https://github.com/sarnesh444/FastAPI/blob/master/model.py)
  * After building the model to escape the overhead of training the model upon every request to the API it is recommended to pickle the model.
  * With the help of pickle library we save the trained model,so now upon a request only a prediction would be made and the model will not be trained all over again.
 
### Source code
Find the source code [here](https://github.com/sarnesh444/FastAPI/blob/master/fastapiapp.py)

##### I always thought writing APIs was a tough business but with FastAPI writing simple APIs was never this easy.

### Use Case

When working as a team the ML Engineer might not want to grant access to the model's source code to a developer so the solution is to build a SimpleAPI which the developer can call using one of the methods GET/POST/PUT and fetch the models results.
 
 ### Alternatively....
 An API can be built even with [Flask](https://flask.palletsprojects.com/en/1.1.x/) but having the experience of working with both,I find FastAPI more easy.

## Try it out...

1. [Clone](https://github.com/sarnesh444/FastAPI.git) this repo and try it out I am sure you would not regret using it.

## Meta 

| Name | Github | LinkedIn | E-mail | Phone|
| --- | --- | --- | --- | --- |
| Saranesh ManiRatna.K | [@saranesh](https://github.com/sarnesh444) | [@saranesh](https://www.linkedin.com/in/saranesh-kanumuri-17a7a5181/) |[E-mail](mailto:sarnesh444@gmail.com) | [(+91) 8500717519](tel:+918500717519)

#### This project is NOT meant for production and hasn't been tested thoroughly.


