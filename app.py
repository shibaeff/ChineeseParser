from flask import Flask
import subprocess

app = Flask(__name__)

@app.route('/')
def hello_world():
    # when request is made, some routine is triggerd
    scrapy_line = "scrapy crawl s1"
    scrapy = subprocess.Popen(scrapy_line.split(), stdout=subprocess.PIPE)
    output, error = scrapy.communicate()

    base_line = "python base_composer.py"
    base_composer = subprocess.Popen(scrapy_line.split(), stdout=subprocess.PIPE)
    output, error = base_composer.communicate()

    return 'Done', 200

if __name__ == '__main__':
    my_awesome_app.run()