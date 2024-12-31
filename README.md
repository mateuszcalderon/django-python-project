<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" height="60" width="60" style="margin-right: 20px;">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>Django and Python Project</h1>
</div>

## Resources:
To learn about Django and its role, I followed the tutorials from the YouTube channel **Webdesign em Foco**. You can check out his first Python tutorial video [here](https://www.youtube.com/watch?v=zcjBIt6rwTY).

## Installation:
### 1. Install Python
If you don't have Python installed on your system, download it from the official website:
- [Python Official Website](https://www.python.org/)

You can check if Python is installed correctly and verify its version by running ` python --version ` on your Command Prompt.

### 2. Create a Virtual Environment
It's highly recommended to use a virtual environment to keep your project dependencies isolated and avoid conflicts with other Python projects.<br/>
To create a virtual environment:
  1. Navigate to the directory where you want to set up your Django project. You can use your Command Prompt.
  2. Then, run the following command to create your virtual environment: ` python -m venv venv `
  3. To activate the virtual environment, run the command: ` ...\venv\Scripts\activate `

### 3. Install Django
With your virtual environment activated, install Django using pip: ` pip install django `

### 4. Start a new Django project
Now that Django is installed, you can create your Django project by running the following command: ` django-admin startproject myproject . ` and then ` python manage.py startapp myapp `
(replace ` myproject ` and ` myapp ` with your preferred names)

### 5. Install Database
To use MySQL database and run this project locally, as I did, you have to download a web development environment. My suggestion is WampServer but feel free to use your favorite web development environment. Download WampServer [here](https://www.wampserver.com/en/).

### 6. Install IDE
There are dozens of IDEs available for download and you can choose the one you are most comfortable with. My project was developed using PyCharm and you can download it clicking [here](https://www.jetbrains.com/pycharm/).

### 7. Install mysqlclient
mysqlclient allows Python programs to connect to MySQL and MariaDB databases and perform CRUD (Create, Read, Update, Delete) operations. You can install mysqlclient using pip: ` pip install mysqlclient `

### 8. Database Migration
The ` python manage.py migrate ` command applies database migrations in a Django project, ensuring the database schema is up-to-date with the defined models. It creates, modifies, or deletes tables and columns based on migration files, keeping the database structure synchronized with your code. Just run it on your Command Prompt and your database will already be configured.

### 9. Run Server
The ` python manage.py runserver ` command starts Django's built-in development server, allowing you to run your project locally. Run it on your Command Prompt and you finally will be able to develop your Django project.

## Development Environment:
This project was developed using the following tools and versions:
  - Django: 5.1.2
  - mysqlclient: 2.2.4
  - PyCharm: 2024.2.1 (Community Edition)
  - Python: 3.12.6
  - WampServer: 3.3.5 

## Project Disclaimer:
**Note:** The primary goal of this project was to develop and enhance my skills in Django and Python. While the application includes  CSS and HTML, these are not the main focus of the project, and the Front End code may not adhere to the best practices or modern standards.<br/>
Please consider this project as a learning exercise for Back End development with Python and Django.

## Contact:
Feel free to reach out to me with any questions, suggestions, or feedback!<br/>
[![Instagram](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/instagram.svg)](https://www.instagram.com/mateuszcalderon/)
[![LinkedIn](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/linkedin.svg)](https://www.linkedin.com/in/mateuszcalderonreis/)
[![GitHub](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/github.svg)](https://github.com/mateuszcalderon)
