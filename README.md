# Anime Recommendation System
This project implements a recommendation engine for anime shows based on their genres using TF-IDF Vectorization and Cosine Similarity. It deploys a Flask-based web application to provide anime recommendations based on user input. The backend uses PostgreSQL to store and retrieve data, and the engine outputs top recommended anime shows for cross-analysis and database integration.

## Table of Contents
#### Project Overview
#### Features
#### Installation
#### Usage
#### Project Structure
#### Key Files and Folders
#### Technologies Used
#### Acknowledgements
#### Project Overview

## Problem Statement
Given transaction data of anime shows, we aim to develop a recommendation system that suggests similar anime shows based on their genre, helping users discover new shows they might enjoy.

## Objectives
#### Recommend similar anime shows based on genre.
#### Store recommendation results in a PostgreSQL database.
#### Deploy a Flask-based web application for user interaction.
#### Solution Approach

## This project follows a systematic approach:

#### Data Processing: Reads anime data, fills missing values, and preprocesses genre data.
#### TF-IDF Vectorization: Extracts important features from the 'genre' column.
#### Cosine Similarity: Computes similarity scores between different anime genres.
#### Flask App: Provides an interface where users input their preferred anime, and the engine outputs recommendations.

## Features
#### Anime Recommendations: Retrieves top anime recommendations based on user input.
#### Database Integration: Saves results in a PostgreSQL database.
#### Web-Based Interface: User-friendly interface to request and view recommendations.
#### Installation
#### Prerequisites
#### Python 3.x
#### PostgreSQL Database
#### Required Python libraries (can be installed via requirements.txt)

## Steps
#### Clone the repository:
#### git clone https://github.com/yourusername/Anime-Recommendation-System.git
#### cd Anime-Recommendation-System
#### Install dependencies:
#### pip install -r requirements.txt

## Database Setup:

#### Create a PostgreSQL database named recommenddb.
#### Update PostgreSQL credentials in app.py and main script.

## Prepare Data and Models:

#### Place your dataset in the project directory.
#### Run the preprocessing and model training script to save the tfidf_matrix and cosine_matrix using joblib.
#### Run the Flask App:

#### python app.py
#### Access the Application: Open your browser and navigate to http://127.0.0.1:5000.

#### Usage
#### Start the App: After setting up the environment, run app.py to start the Flask app.
#### Input Anime and Get Recommendations:
#### On the home page, enter the name of an anime and the number of top recommendations.
#### Click 'Submit' to view recommendations, which will also be saved to the PostgreSQL database.
#### View Saved Data: Check the saved recommendations in your PostgreSQL database under the table top_10.

## Project Structure

#### Anime-Recommendation-System/
#### ├── templates/
#### │   ├── index.html               # Homepage template
#### │   ├── data.html                # Results template
#### ├── anime.csv                    # Dataset file
#### ├── app.py                       # Main Flask application
#### ├── matrix                       # Saved TF-IDF matrix
#### ├── cosine_matrix                # Saved cosine similarity matrix
#### ├── requirements.txt             # Dependencies
#### └── README.md                    # Project Documentation
#### Key Files and Folders
#### app.py: Main Flask app file, containing routes, database connections, and the recommendation function.
#### anime.csv: Dataset with anime shows, genres, ratings, etc.
#### matrix: Saved TF-IDF model for genre feature extraction.
#### cosine_matrix: Saved cosine similarity matrix for anime recommendations.
#### templates/: Contains HTML files for web app pages.

## Technologies Used
#### Programming Language: Python

## Libraries:
#### pandas, joblib, sklearn (TF-IDF, Cosine Similarity)
#### sqlalchemy and psycopg2 (Database connections)
#### Database: PostgreSQL
#### Framework: Flask for web interface

## Acknowledgements
#### This project is based on public datasets and open-source libraries in Python. Special thanks to the contributors of sklearn, pandas, and the Flask and PostgreSQL communities.
