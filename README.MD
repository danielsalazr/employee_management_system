<br />
<div align="center">
<h3 align="center">Employee Management</h3>
  <p align="center">
    This is a project to manage employee information to your company. 
  </p>
</div>

### Built With

* ![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54)
* ![Django](https://img.shields.io/badge/django-%23092E20.svg?style=for-the-badge&logo=django&logoColor=white)
* ![MySQL](https://img.shields.io/badge/MySQL-005C84?style=for-the-badge&logo=mysql&logoColor=white)


<!-- GETTING STARTED -->
## Getting Started

To get a local copy up and running follow these steps.

### Prerequisites

* Python 10 [https://www.python.org/downloads/](https://www.python.org/downloads/)
* MySQL [https://dev.mysql.com/downloads/installer/](https://dev.mysql.com/downloads/installer/)
* Install requerimets.txt file dependencies using pip [requeriments.txt installarion guide](https://note.nkmk.me/en/python-pip-install-requirements/)

### Recommended Tools
* IntelliJ Community [https://www.jetbrains.com/idea/download/](https://www.jetbrains.com/idea/download/)
* Postman [https://www.postman.com/downloads/](https://www.postman.com/downloads/)

### Installation


1. Clone the follow repository
   ```sh
   https://github.com/danielsalazr/Sistema_de_empleados.git
   ```
2. Create a new database in MySQL running this script
   ```
   python3 manage.py makemigrations
   python3 manage.py migrate
   ```
3. Create the .env file settings as the example in proyect.
   ```yml
   SECRET_KEY=DJANGO_SETTINGS_KEY
   DEBUG=FALSE
   NAME_DB=SOME_NAME_AT_YOUR_PREFERENCE
   USER_DB=YOUR_USER_DB
   PASS_DB=YOUR_PASSWORD
   PORT=3306
   ```
4. Open Swagger UI 
   ```
   python3 manage.py runserver
   ```
<!-- USAGE -->
## Usage

1. Open [http://localhost:8000/](http://localhost:8000/) in your web browser
<!-- 4. execute the endpoint "dish-rest-controller"/POST/dish/ to create a dish", the restaurant could exist to create dish
5. execute the endpoint "dish-rest-controller"/PATCH/dish/{id}/ to change price and description to existing dish -->
<!-- ROADMAP -->
<!-- ## Tests

- Right-click the test folder and choose Run tests with coverage -->