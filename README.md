# Python-Newsfeed
A Tech Blog were individuals can log in and post interesting articles. Users can also comment and vote on other posts. Built using Python, MySQL, SQLAlchemy, and Jinja2.

## Description

This project helped me learn more about the Python language. Using given frontend templates, I set up Python webserver (Flask) to render the frontend.

* To create the backend, the database was setup using pymysql and the database connection to the frontend was setup in Flask. 
SQLAlchemy was used to create models, sync models with the Database, add model validations, and create API routes (using the Blueprint object). 

* During each call to the server, I used the Flask 'g object' to store data during the server request to the database (context) and then ensured the database connection was closed when the request ended and the context was destroyed.

* User logins and persistent sessions were created in the Flask app using API routes and using the global object 'request', and I set up password encryption using bycrpt and cryptography with some salt. I added error handling using 'try .... except' statements. 

* The app was set up to conditionally show pages of the website based on whether the user is logged in or not, and decorators were used to protect the API routes from users who aren't logged in. 

* I used Jinja2 to create custom filter functions in template files (date format, URL format, plural words) and implemented them in the template files to make for a better user experience. 


![Front_Page](https://github.com/Samantha-Ruth/Python-Newsfeed/assets/64170123/ff98f9a3-bfcb-405f-9fb6-c0e95296f92b)


## Table of Contents

* [Installation](#installation)
* [Usage](#usage)
* [Links](#links)
* [Questions](#questions)

## Installation

If the user already has python installed on their device, they can download this project, create a virtual environment (. venv/bin/activate). Install flask and then start the flask server (export FLASK_APD = app, python3 =m flask run).
"pip install flask wsqlalchemy pymysql python-dotenv bcrypt cryptography" to download the required dependencies (respectively).  In order to access the mysql2 shell,  they would need to create a .env file with the following, replacing <username> and <user password> with the users own username and password: 
  
DB_URL=mysql+pymysql://root:<password>@localhost/python_news_db

Where <password> is your personal mysql password. 


To ensure the user is connected to the correct database, navigate to the root folder of the project, and then open the mysql2 shell and enter "source db/schema.sql".  Then enter "USE python_news_db" to use the database file. Exit the mysql2 shell by entering "exit" into the command line.

Next, seed the database with data by entering "python seeds.py" into the command line.  The database and required tables are now created, selected, and contain data.  

Finally, connect the server by entering "python3 -m flask run" into the command line.


## Usage

When the user gets to the homepage, they will be presented with a list of existing blog posts and comments.  At the top of the webpage, the user has an option to login.  Once they click on the login link, the user has the option to log in or create a new login account. Once the user logs in, they are taken to a dashboard of the posts they have created.  They are given the option to add a new post, change the title of the post, or delete the post.  They also have the option to comment on other posts and upvote posts they like. 


## Links


The link to the project is here:

The url of the Git repository is here: https://github.com/Samantha-Ruth/python-newsfeed


## Questions

If you have any questions about the repo, open an issue or you can find more of my work at (https://gitHub.com/Samantha-Ruth).


