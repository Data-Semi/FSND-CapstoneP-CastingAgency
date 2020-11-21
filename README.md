# FSND Capstone Project
UDACITY FSND Capstone project
This is the capstone project of Full Stack web developer Nano Degree by Udacity.
In this project I will deploy the Flask application to Heroku. The application uses Role-Based Access Control(RBAC) by Auth0, a third-party authentication system.  

I could apply all skills that I have learned in the Udacity's Full Stack web developer Nano Degree course, including architecturing relational database, modeling data objects with SQLAlchemy, writing, testing and documenting a RESTful Flask API, integrating third-party authentication system.

This project is coded in Python3 and is styled to PEP 8 Style Guide.  

## Casting Agency Specifications  
The Casting Agency models could be used by user that is responsible for creating movies and managing and assigning actors to those movies.   

## Getting Started
### Pre-requisites and Local Development
You should already have Python3, pip and node installed on your local machines
To create a virtual environment on MacOS, run:
```python3 -m venv env```
To activate the virtual environment, run:
```source env/bin/activate```
## About the Stack
### Backend
On MacOS, to set up all the dependencies, run:
```pip install requirements.txt```
To run the application on your local machine, run:
```python3 app.py```
The application is hosted on https://sheltered-bayou-87289.herokuapp.com/ and can also be run locally at http://127.0.0.1:5000/ .
The PostgreSQL database is hosted on Heroku. If you want to run locally using your local databse, you can modify the following fields in the models.py file:
```database_name =<your_database_name>, database_path = <your_database_path```

### Frontend
Work in Progress
### Authentication Set Up
Tokens can be found in the setup.sh file.
### Testing
To run the tests locally, you need to have PostgreSQL installed on your local machines already.
To set up a test database, replace the following fields on the test_app.py file:
```db_user =<your username>```
To run the tests, run: 
```python3 test_app.py ```
## API Reference
### Getting Started
- Base URL: This app is hosted on: https://sheltered-bayou-87289.herokuapp.com/, or it can be run locally on http://127.0.0.1:5000/
- Authentication: This version of the application requires authentication for all endpoints

### Error Handling
Errors are returned as JSON objects in the following format:
```
{
  "success": False,
   "error": 400,
   "message": "Bad Request"
}
```
The API will return these error types when requests fail:
- 400: Bad Request
- 404: Not Found
- 422: Unprocessable
- 405: Method Not Allowed
- 500: Internal Server Error

If authentication is required, these error types will be returned when requests fail:
- 401 : Errors regarding authorization headers or token (i.e: "Token expired")
- 403: Permission not found
- 400: Invalid header
### Roles and Permissions
There are 3 roles:
- Casting Assistant: Can view actors and movies
- Casting Director: Can view actors and movies, add or delete an actor from the database, and modify actors or movies
- Producer: Have all permissions

### Endpoints
#### GET /actors (Casting Assistant, Casting Director, Producer)
- General: Returns a list of all actors objects and success value
- Sample:
```
{
  "actors": [
    {
      "age": 33,
      "gender": "Female",
      "name": "Angelina Jolie"
    },
    {
      "age": 23,
      "gender": "Female",
      "name": "Natalie Brown"
    }
  ],
  "success": true
}
```
#### GET /movies (Casting Assistant, Casting Director, Producer)
- General: Returns a list of all movies objects and success value
- Sample:
```
{
  "movies": [
    {
      "release date": "2019-07-07",
      "title": "Ava"
    },
    {
      "release date": "2010-12-10",
      "title": "Boba"
    }
  ],
  "success": true
}
```

#### POST /actors (Casting Director, Producer)
- General: Creates a new actor using JSON request parameters and returns success value, newly created actor
- Sample: Response for a request with following body {"name": "Brad P", "age": 45, "gender": "Male"} and the appropriate header: 

```
{
  "new actor added": {
    "age": 45,
    "gender": "Male",
    "name": "Brad P"
  },
  "success": true
}
```
#### POST /movies (Producer)
- General: Creates a new movie using JSON request parameters and returns success value, newly created movie
- Sample: Response for a request with following body {"title": "Avatar", "release_date": "2020-01-03"} and the appropriate header:
```
{
  "new movie added": {
    "release_date": "2020-01-03",
    "title": "Avatar"
  },
  "success": true
}
```
#### DELETE /actors/<<int:id>> (Casting Director, Producer)
- General: Deletes an actor from the database by id and returns success value and id of the deleted actor
- Sample: Response for a request to delete an actor with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### DELETE /movies/<<int:id>> (Producer)
- General: Deletes a movie from the database by id, returns success value and id of the deleted movie
- Sample: Response for a request to delete a movie with id=2 and the appropriate header:
```
{
  "deleted": 2,
  "success": true
}
```
#### PATCH /actors/<<int:id>> (Casting Director, Producer)
- General: Modifies an actor by id using JSON request parameters and returns success value and id of the modified actor
- Sample: Response for a request to modify an actor with id=3, with the following body {"name": "Tien Le","age": "22","gender": "Female"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
#### PATCH /movies/<<int:id>> (Casting Director, Producer)
- General: Modifies a movie by id using JSON request parameters; returns success value and id of the modified movie
- Sample: Response for a request to modify a movie with id=3, with the following body{"title": "Mat Biec", "release_date": "2020-01-02"} and the appropriate header:
```
{
  "success": true,
  "updated": 3
}
```
## Authors
Tien Le
## Acknowledgements
I would like to thank Udacity for the idea suggestion of this project







Models:  

Movies with attributes title and release date    
Actors with attributes name, age and gender  
Endpoints:  
GET /actors and /movies   
DELETE /actors/ and /movies/  
POST /actors and /movies and  
PATCH /actors/ and /movies/  
Roles:  
Casting Assistant  
Can view actors and movies  
Casting Director  
All permissions a Casting Assistant has and…  
Add or delete an actor from the database  
Modify actors or movies  
Executive Producer  
All permissions a Casting Director has and…  
Add or delete a movie from the database  
Tests:  
One test for success behavior of each endpoint  
One test for error behavior of each endpoint  
At least two tests of RBAC for each role  


### Testing
To run the tests locally, you need to have PostgreSQL installed on your local machines already.
To set up a test database, replace the following fields on the test_app.py file:
```db_user =<your username>```
To run the tests, run:
dropdb CastingAgencyTest
createdb CastingAgencyTest 

```source ./setup.sh ```

```python3 test_app.py ```

To monitor the test database contents.
psql CastingAgencyTest
select * from "Movie";
select * from "Actor";

https://casting-agency-program.herokuapp.com/
set git remote heroku to https://git.heroku.com/casting-agency-program.git



flask db migrate , have to change codes inside models.py. But if use manage.py. it is independent.

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

heroku3 instead of heroku


