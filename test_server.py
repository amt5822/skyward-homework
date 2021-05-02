import unittest
from server import app

""" This class tests the homepage html content and the /health/ route."""

class TestServer(unittest.TestCase):
    """ Function to test the homepage."""
    def test_home(self):
        home_test = app.test_client(self)
        response = home_test.get('/', content_type='html/text')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'Hooray, you did it!\n')

    def test_health(self):
        """ Function to test status code return and JSON msg."""
        health_test= app.test_client(self)
        response = health_test.get('/health/')
        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.data, b'{"Status":"Ok"}\n')

    def test_no_path(self):
        """ Function to test status code return of 404 when non existent path is entered."""
        health_test= app.test_client(self)
        response = health_test.get('/choochoo/')
        self.assertEqual(response.status_code, 404)



if __name__ == '__main__':
    unittest.main()
