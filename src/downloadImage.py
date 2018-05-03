import urllib
import os


class DownloadImage:

    def download_images(self, file_name):
        try:
            with open(file_name) as f:
                for line in f:
                    image = line.rpartition('/')[2]
                    image_path = os.path.join('../output', image)
                    urllib.urlretrieve(line, image_path)
        except IOError:
            print("Could not read file {}".format(file_name))


def main():
    download = DownloadImage()
    file_name = os.path.join('../urls/', 'urls.txt')
    download.download_images(file_name)


if __name__ == '__main__':
    main()
