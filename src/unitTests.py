import os
import unittest



class TestDOwnloadImage(unittest.TestCase):

    def test_check_file(self):
        self.assertTrue(os.stat('../urls/urls.txt').st_size > 0)

    def test_check_urls(self):
        with open('../urls/urls.txt') as f:
            for line in f:
                self.assertTrue(line.startswith('http'))

    def test_check_download(self):
        num_urls = 0
        num_images = 0
        with open('../urls/urls.txt') as f:
            num_urls = sum(1 for _ in f)
        num_images = len([name for name in os.listdir('../output')])
        self.assertTrue(num_urls  == num_images)


if __name__ == '__main__':
    unittest.main()