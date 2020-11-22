import os
import unittest
import json
from flask_sqlalchemy import SQLAlchemy
from flask_cors import CORS

from app import create_app
from models import setup_db, Movie, Actor

assistant_token = os.environ.get('ASSISTANT_TOKEN')
director_token = os.environ.get('DIRECTOR_TOKEN')
producer_token = os.environ.get('PRODUCER_TOKEN')
db_user = "postgres"


class CastingAgencyTest(unittest.TestCase):
    def setUp(self):
        self.app = create_app()
        self.client = self.app.test_client
        self.database_name = "casting_agency_test"
        self.database_path = "postgresql://{}/{}".format('localhost:5432',
                                                         self.database_name)
        self.headers_assistant = {'Content-Type': 'application/json',
                                  'Authorization': assistant_token}
        self.headers_director = {'Content-Type': 'application/json',
                                 'Authorization': director_token}
        self.headers_producer = {'Content-Type': 'application/json',
                                 'Authorization': producer_token}
        setup_db(self.app, self.database_path)

        with self.app.app_context():
            self.db = SQLAlchemy()
            self.db.init_app(self.app)
            self.db.create_all()
        self.new_actor = {
                        "name": "Brad Pitt",
                        "age": 57,
                        "gender": "male",
                        }
        self.new_movie = {
                        "title": "The Curious Case of Benjamin Button",
                        "release_date": "2008-12-25T00:00:00.000Z",
                        }

    def tearDown(self):
        """Executed after reach test"""
        pass

    def test_200_get_actors(self):
        res = self.client().get('/actors', headers=self.headers_producer)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['actors'])

    def test_200_get_movies(self):
        res = self.client().get('/movies', headers=self.headers_producer)
        self.assertEqual(res.status_code, 200)
        data = json.loads(res.data)
        self.assertEqual(data['success'], True)
        self.assertTrue(data['movies'])

    def test_422_post_actors_failed(self):
        res = self.client().post('/actors', headers=self.headers_producer,
                                 json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], "Unprocessable")
        self.assertEqual(data['success'], False)

    def test_422_post_movies_failed(self):
        res = self.client().post('/movies', headers=self.headers_producer,
                                 json={})
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 422)
        self.assertEqual(data['message'], "Unprocessable")
        self.assertEqual(data['success'], False)

    def test_200_post_actors(self):
        res = self.client().post('/actors', headers=self.headers_producer,
                                 json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['new actor added']))

    def test_200_post_movies(self):
        res = self.client().post('/movies', headers=self.headers_producer,
                                 json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertTrue(len(data['new movie added']))

    def test_200_delete_actor(self):
        res = self.client().delete('/actors/5', headers=self.headers_producer)
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 5).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertEqual(actor, None)

    def test_200_delete_movie(self):
        res = self.client().delete('/movies/5', headers=self.headers_producer)
        data = json.loads(res.data)
        movie = Movie.query.filter(Movie.id == 5).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['deleted'], 5)
        self.assertEqual(movie, None)

    def test_404_actor_not_found(self):
        res = self.client().delete('/actors/99', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "Not Found")
        self.assertEqual(data["success"], False)

    def test_404_movie_not_found(self):
        res = self.client().delete('/movies/99', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['message'], "Not Found")
        self.assertEqual(data["success"], False)

    def test_200_patch_actors(self):
        res = self.client().patch('/actors/2', headers=self.headers_producer,
                                  json=self.new_actor)
        data = json.loads(res.data)
        actor = Actor.query.filter(id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 2)

    def test_200_patch_movies(self):
        res = self.client().patch('/movies/2', headers=self.headers_producer,
                                  json=self.new_movie)
        data = json.loads(res.data)
        movie = Movie.query.filter(id == 2).one_or_none()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(data['success'], True)
        self.assertEqual(data['updated'], 2)

    def test_404_actor_not_found_patch_actors(self):
        res = self.client().patch('/actors/1000',
                                  headers=self.headers_producer,
                                  json=self.new_actor)
        data = json.loads(res.data)
        actor = Actor.query.filter(id == 1000).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_404_movie_not_found_patch_movies(self):
        res = self.client().patch('/movies/1000',
                                  headers=self.headers_producer,
                                  json=self.new_movie)
        data = json.loads(res.data)
        movie = Movie.query.filter(id == 1000).one_or_none()
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_404_actors_not_found_get_actors(self):
        Actor.query.delete()
        res = self.client().get('/actors', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_404_movies_not_found_get_movies(self):
        Movie.query.delete()
        res = self.client().get('/movies', headers=self.headers_producer)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 404)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Not Found")

    def test_403_delete_movie_not_permitted(self):
        res = self.client().delete('/movies/4',
                                   headers=self.headers_director)
        data = json.loads(res.data)
        # movie = Movie.query.filter(Movie.id == 4).one_or_none()
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

    def test_403_post_movie_not_permitted(self):
        res = self.client().post('/movies', headers=self.headers_director,
                                 json=self.new_movie)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

    def test_403_patch_actor_not_permitted(self):
        res = self.client().delete('/actors/4',
                                   headers=self.headers_assistant)
        data = json.loads(res.data)
        actor = Actor.query.filter(Actor.id == 4).one_or_none()
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

    def test_403_post_actor_not_permitted(self):
        res = self.client().post('/actors', headers=self.headers_assistant,
                                 json=self.new_actor)
        data = json.loads(res.data)
        self.assertEqual(res.status_code, 403)
        self.assertEqual(data['success'], False)
        self.assertEqual(data['message'], "Permission not found")

# Make the tests conveniently executable
if __name__ == "__main__":
    unittest.main()
