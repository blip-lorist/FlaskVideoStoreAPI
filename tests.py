import os
import json
import video_store
import unittest
import tempfile
from video_store import app, db
from video_store.models import Customer, Movie, Rental

class VideoStoreTestCase(unittest.TestCase):

    def setUp(self):
        self.app = video_store.app.test_client()
        basedir = os.path.abspath(os.path.dirname(__file__))
        app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///' + os.path.join(basedir, 'test.db')
        db.create_all()

    def tearDown(self):
        db.drop_all()

    def test_zomg_endpoint(self):
        response = self.app.get('/zomg')
        assert 'It works!' in response.data

class CustomerRoutesTest(VideoStoreTestCase):

    def test_get_customers(self):
        customer_record = Customer('Eugene Victor Tooms', 'Wed, 29 Apr 2015 07:54:14 -0700', '66 Exeter Street', 'Boston', 'MA', '02116', '(666) 666-6666', 6.66)
        db.session.add(customer_record)
        db.session.commit()

        response = self.app.get('/customers/')
        assert 'Eugene Victor Tooms' in response.data

    def test_get_customers_sorted_by_name(self):
        customer_record1 = Customer('Fox Mulder', 'Wed, 29 Apr 2015 07:54:14 -0700', 'Apartment 42', 'Washington', 'DC', '02116', '(123) 456-7890', 5.00)
        customer_record2 = Customer('Dana Scully', 'Wed, 29 Apr 2015 07:54:14 -0700', 'Apartment 42', 'Washington', 'DC', '02116', '(123) 456-7890', 5.00)

        db.session.add(customer_record1)
        db.session.add(customer_record2)
        db.session.commit()

        response = self.app.get('/customers/name/page1')
        response_dict = json.loads(response.data)
        first_record = response_dict["customers"][0]["name"]
        second_record = response_dict["customers"][1]["name"]

        assert 'Dana Scully' in first_record
        assert 'Fox Mulder' in second_record

class MoviesRoutesTest(VideoStoreTestCase):

    def test_get_movies(self):
        movie_record = Movie('X-Files: Fight the Future', 'Alien popsicles', 'June 19, 1998', 6)
        db.session.add(movie_record)
        db.session.commit()

        response = self.app.get('/movies/')
        assert 'X-Files' in response.data

    def test_get_movies_sorted_by_name(self):
        movie_record1 = Movie('X-Files: I Want to Believe', "I want to believe this film didn't happen", 'July 24, 2008', 6)
        movie_record2 = Movie('X-Files: Fight the Future', 'Alien popsicles', 'June 19, 1998', 6)

        db.session.add(movie_record1)
        db.session.add(movie_record2)
        db.session.commit()

        response = self.app.get('/movies/title/page1')
        response_dict = json.loads(response.data)
        first_record = response_dict["movies"][0]["title"]
        second_record = response_dict["movies"][1]["title"]

        assert 'Fight the Future' in first_record
        assert 'I Want to Believe' in second_record

class RentalRoutesTest(VideoStoreTestCase):

    def test_get_movie_details(self):
        movie_record = Movie('The Lone Gunmen', "This would be a sweet movie", 'Nov 11, 2016', 6)

        db.session.add(movie_record)
        db.session.commit()

        response = self.app.get('/rentals/The Lone Gunmen/')
        response_dict = json.loads(response.data)

        assert 'The Lone Gunmen' in response_dict["movies"]["title"]

if __name__ == '__main__':
    unittest.main()
