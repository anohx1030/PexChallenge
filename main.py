from PIL import Image
from multiprocessing import Process
import urllib2
import threading

def link_generator():
    fi = open('output.csv', 'w')
    with open('urls.txt') as f:
        for line in f:
            yield line, fi

    fi.close()

def link_opener():
    for link, fi in link_generator():
        image = Image.open(urllib2.urlopen(link))
        yield link, image, fi

def csv_writer():
    for url, image, fi in link_opener():
        w,h = image.size
        pixels = sorted(image.getcolors(w*h))
        line = ""
        line += url.rstrip() + ";"
        line += str(pixels[-1][1]) + ";"
        line += str(pixels[-2][1]) + ";"
        line += str(pixels[-3][1]) + "\n"
        fi.write(line)

csv_writer()
# threading.Thread(target=csv_writer).start()