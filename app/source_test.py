import unittest
from models import source

Source = source.Source


class SourceTest(unittest.TestCase):
    '''
    Test Class to test the behaviour of the Source class.
    '''

    def setUp(self):
        '''
        Set up method that will run before every Test.
        '''
        self.new_source = Source('national-geographic','National Geographic','eporting our world daily','http://news.nationalgeographic.com','science')

    def test_instance(self):
        self.assertTrue(isinstance(self.new_source,Source))


if __name__ == '__main__':
    unittest.main()
