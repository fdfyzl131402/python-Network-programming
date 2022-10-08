import urllib.request
import gevent
from gevent import monkey
monkey.patch_all()


def downloader(file_name, img_url):
    req = urllib.request.urlopen(img_url)
    img_content = req.read()

    with open(file_name, "wb") as f:
        f.write(img_content)


def main():
    gevent.joinall([
        gevent.spawn(downloader, "1.jpg", "https://anchorpost.msstatic.com/cdnimage/anchorpost/1081/e7/00bd17b56f5e837f6ef1764e0d279e_1663_1651932063.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp"),
        gevent.spawn(downloader, "2.jpg", "https://anchorpost.msstatic.com/cdnimage/anchorpost/1004/ee/f0240b331423deb001e5d82b562182_1663_1664863202.jpg?imageview/4/0/w/338/h/190/blur/1/format/webp")
    ])


if __name__ == "__main__":
    main()