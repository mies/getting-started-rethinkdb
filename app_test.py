from app import app

import unittest

class BookmarkTestCase(unittest.TestCase):

  def setUp(self):
    pass

  def tearDown(self):
    pass

  def test_bookmarks(self):
    tester = app.test_client(self)

    resp = tester.get('/', content_type='application/json')

    self.assertEqual(resp.status_code, 200)

if __name__ == '__main__':
  unittest.main()
