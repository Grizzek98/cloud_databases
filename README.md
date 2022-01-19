# Overview

This program is a simple cloud-based shopping cart / store system. It allows you to see and modify a list of products stored in the cloud. It also allows you to modify a shopping cart that will estimate the total cost of products inside.

This program creates a connection to a Google Firebase Firestore database in order to retrieve or modify data in the "store".

The purpose of writing this software was to learn how Google Cloud Databases work, and how to interact with them.

[Software Demo Video](http://youtube.link.goes.here)

# Cloud Database

Google Firebase Firestore

The general structure is composed of CATEGORY -> PRODUCT
Categories can contain many Products and Products contain 
'name' and 'price' fields stored in JSON format

# Development Environment

* Visual Studio Code
* Python 3.9.9
    * Python firebase_admin library

# Useful Websites

{Make a list of websites that you found helpful in this project}
* [Code First With Hala - Youtube Playlist](https://www.youtube.com/watch?v=Hh4IAwcZBLM&list=PLs3IFJPw3G9LW-rGJ8EBMaCd8OxGm_qQe&index=1)
* [Google Firebase](https://firebase.google.com/docs/firestore)

# Future Work

* Cart save / load functionality
* View indexed lists when adding / removing data from database
* Restructure 'database.py' so that only one return_category method
    is required
* Fix printed UI when giving input for adding / removing data from database