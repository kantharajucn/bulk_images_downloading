import os
import unittest
from downloadImages import DownloadImage


class TestDownloadImage(unittest.TestCase):

    def setUp(self):
        print('TestDownloadImage.__init__')
        self.url_file = "../urls/urls.txt"
        self.output = "../output"
        self.download = DownloadImage(self.url_file)

    def test_check_file(self):
        self.assertTrue(os.stat(self.url_file).st_size > 0)

    def test_check_urls(self):
        with open(self.url_file) as f:
            for line in f:
                self.assertTrue(line.startswith('http'))

    def test_download(self):
        self.assertTrue(len(os.listdir("../urls")),0)

    def test_verify_output(self):
        with open(self.url_file) as f:
            num_urls = sum(1 for _ in f)
        num_images = len([name for name in os.listdir(self.output)])
        self.assertTrue(num_urls == num_images)


if __name__ == '__main__':
    unittest.main()
