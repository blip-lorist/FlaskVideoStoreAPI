import os
import video_store
import unittest
import tempfile
from video_store import app, db

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
        # import pdb; pdb.set_trace()

if __name__ == '__main__':
    unittest.main()
