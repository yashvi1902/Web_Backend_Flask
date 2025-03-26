# Web Backend Flask Project

## Team Members
- Yashvi Navadia
- Darshil Gabani
- Devarsh Jani

## Features
- JWT Authentication
- Public & Admin Routes
- File Upload & Validation
- Error Handling
- CRUD Support

## Setup Environment
python3 -m venv venv
source venv/bin/activate

## Install All Packages
pip3 install -r requirements.txt

## Initialize the Database
CREATE DATABASE flask_api;

## Create user table
CREATE TABLE users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(255) NOT NULL,
    email VARCHAR(100) DEFAULT NULL
);

## Run Application
python3 run.py


