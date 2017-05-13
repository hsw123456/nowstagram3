import unittest
from nowstagram import app


class NowstagramTest(unittest.TestCase):
    def setUp(self):
        print 'setUp'
        app.config['TESTING'] = True
        self.app = app.test_client()


    def tearDown(self):
        print 'tearDown'



    def login(self, username, password):
        return self.app.post('/login/',data={'username':username, 'password':password},
                             follow_redirects= True)

    def test_reg_login_logout(self):
        self.login('hsf','123')
        assert '-hsf' in self.app.open('/').data
