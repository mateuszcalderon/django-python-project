<p align="center">
  <img src="https://github.com/devicons/devicon/blob/master/icons/django/django-plain.svg" height="60" width="60" style="margin-right: 20px;">
  <img src="https://github.com/devicons/devicon/blob/master/icons/python/python-original.svg" height="60" width="60">
</p>

<div align="center">
  <h1>Django and Python Project</h1>
</div>

## Resources:
To learn about Django and its functionality, I followed the tutorials from the YouTube channel **Webdesign em Foco**. You can watch the first Django tutorial video in the series [here](https://www.youtube.com/watch?v=zcjBIt6rwTY).

## Installation:
Follow the steps below to set up and run this project locally.

### 1. Install Python
If you don't have Python installed yet, download it from the official website:
- [Python Official Website](https://www.python.org/)
After installing, verify the installation and check the version by running the following command in your Command Prompt: ` python --version `

### 2. Create a Virtual Environment
It's highly recommended to use a virtual environment to manage your project dependencies. This ensures isolation and prevents conflicts with other Python projects.<br/>
To create a virtual environment:
  1. Navigate to the directory where you want to set up your Django project. You can use your Command Prompt.
  2. Run the following command to create a virtual environment: ` python -m venv venv `
  3. To activate the virtual environment, run the command: ` ...\venv\Scripts\activate `
Once activated, your Command Prompt should display the virtual environment name, indicating that you're working within it.

### 3. Install Django
With the virtual environment active, install Django using pip: ` pip install django `

### 4. Start a new Django project
Now that Django is installed, you can create your Django project by running the following command: ` django-admin startproject myproject . ` and then ` python manage.py startapp myapp `
(replace ` myproject ` and ` myapp ` with your preferred names).

### 5. Install Database (Optional for MySQL)
If you plan to use MySQL locally (as I did), you'll need to set up a web development environment. I recommend WampServer, but feel free to use your preferred stack. Download WampServer [here](https://www.wampserver.com/en/).

### 6. Install IDE
There are many IDEs to choose from. For this project, I used PyCharm, which you can download [here](https://www.jetbrains.com/pycharm/).

### 7. Install mysqlclient
To allow Django to communicate with MySQL database, install the mysqlclient package: ` pip install mysqlclient `

### 8. Database Migration
Run the following command to apply database migrations and set up your database schema: ` python manage.py migrate `

### 9. Run Server
Finally, you can start Django's development server with this command: ` python manage.py runserver `<br/>
Now, open your web browser and go to http://localhost:8000 to see your Django project running locally.

## Development Environment:
This project was developed using the following tools and versions:
  - Django: 5.1.2
  - mysqlclient: 2.2.4
  - PyCharm: 2024.2.1 (Community Edition)
  - Python: 3.12.6
  - WampServer: 3.3.5 

## Project Disclaimer:
**Note:** The primary goal of this project was to develop and enhance my skills in Django and Python. While the application includes CSS and HTML, these are not the main focus of the project, and the Front End code may not adhere to the best practices or modern standards.<br/>
Please consider this project as a learning exercise for Back End development with Python and Django.

## Contact:
Feel free to reach out to me with any questions, suggestions, or feedback!<br/>
[![GitHub](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/github.svg)](https://github.com/mateuszcalderon)
[![Instagram](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/instagram.svg)](https://www.instagram.com/mateuszcalderon/)
[![LinkedIn](https://github.com/CLorant/readme-social-icons/blob/main/large/filled/linkedin.svg)](https://www.linkedin.com/in/mateuszcalderonreis/)
