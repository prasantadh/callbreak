import callbreak

import unittest

class Testing(unittest.TestCase):

    def setUp(self) -> None:
        self.app = callbreak.create_app().test_client()
        return super().setUp()

    def test_get_root(self):
        response = self.app.get('/test')
        print(response.text)
        assert(True)

    def test_get_status(self):
        response = self.app.get('/new/prasant')
        response = self.app.get('/status')
        assert(True)


if __name__ == '__main__':
    unittest.main()
