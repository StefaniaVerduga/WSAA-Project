# Web Services and Applications Project

Course: HDip in Science in Data Analytics
Module: Web Services and Applications
Author: Stefania Verduga

## Introduction:

This repository serves as the culmination of the Web Services and Applications module within the Higher Diploma in Science in Data Analytics at Atlantic Technical University.

The project focuses on a Perfume Inventory Management System developed using Python and Flask for the backend, and HTML for the frontend.

## Purpose:

The purpose of this repository is to provide a comprehensive solution for managing perfume inventory, allowing users to view, add, update, and delete perfume entries.

## Documents contained in this repository:

* 1. README file which contains a description of the project and other information of interest.
* 2. Perfumes_db.sql: this SQL script creates the database perfumes_db and switches to it. It creates a table named 'perfumes' with columns for 'id', 'Name', 'Brand', 'Size_ml', 'Price_eur', and 'Gender'.
* 3. Dbconfig.py file that contains configuration details for connecting to the MySQL database.
* 4. Server.py: this Python file contains the Flask server code. It defines routes for interacting with the server, such as '/perfumes' for retrieving all perfumes, '/perfumes/<id>' for retrieving a specific perfume by ID, and routes for creating, updating, and deleting perfumes.
It utilizes methods from the perfumesdao module to perform CRUD operations on the database.
* 5. Perfumesdao.py: this Python file contains the Database Access Object (DAO) class 'perfumeDAO'. It defines methods for performing CRUD operations on the perfumes table in the MySQL database.
Methods include 'create', 'getAll', 'findById', 'update', and 'delete'.
* 6. Perfumes.html: this HTML file defines the structure and layout of the web page for viewing and interacting with perfumes. It includes a table for displaying perfume data, buttons for creating, updating, and deleting perfumes, and a form for entering perfume details.
JavaScript code is embedded within the HTML to handle user interactions, such as showing/hiding the form, submitting data via AJAX requests, and updating the table dynamically.

## Features:

* View a list of available perfumes.
* Add new perfume entries to the inventory.
* Update existing perfume entries with new information.
* Delete unwanted perfume entries from the inventory.

## System Requirements:

To run or modify the application locally, the latest version of Python is required. Anaconda provides an easily accessible version suitable for Windows, Mac, or Linux operating systems. Alternatively, web-based versions are available.

## Usage:

Access the application in your web browser at http://127.0.0.1:5000/
Use the provided functionality to manage perfume inventory effectively.

## Dependencies:

* Flask.
* REST API.
* SQL database.
* HTML / Javascript.
* AJAX requests to perform CRUD operations.

By following the guidelines provided in this repository, users can seamlessly manage their perfume inventory with ease and efficiency.