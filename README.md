# FSND-CapstoneP-CastingAgency
UDACITY FSND Capstone project

Casting Agency Specifications  
The Casting Agency models a company that is responsible for creating movies and managing and assigning actors to those movies.   

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



flask db migrate , have to change codes inside models.py. But if use manage.py. it is independent.

python manage.py db init
python manage.py db migrate
python manage.py db upgrade

heroku3 instead of heroku


