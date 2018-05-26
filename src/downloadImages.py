import urllib
import os
import argparse


class DownloadImage:

    def __init__(self, url_file):
        self.url_file = url_file

    def download_images(self):

        """Downloading the images from the urls provided in the file to the output directory"""

        # Checking if the output directory exists, If not exists create the directory output
        if not os.path.exists("../output"):
            os.mkdir("../output")

        with open(self.url_file) as f:
            print("Started downloading the images")
            for line in f:
                image = line.rpartition('/')[2]
                image = image.strip()
                image_path = os.path.join('../output', image)
                urllib.urlretrieve(line, image_path)
        print("Downloading the images completed")


def main(url_file):
    download = DownloadImage(url_file)
    download.download_images()


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='Downloading Images from web')
    parser.add_argument('--file', required=True, help='../file.txt')
    parser.print_help()
    args = parser.parse_args()
    main(args.file)
