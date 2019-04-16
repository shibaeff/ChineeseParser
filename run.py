import subprocess
scrapy_line = "scrapy crawl s1"
scrapy = subprocess.Popen(scrapy_line.split(), stdout=subprocess.PIPE)
output, error = process.communicate()

base_line = "python base_composer.py"
scrapy = subprocess.Popen(scrapy_line.split(), stdout=subprocess.PIPE)
output, error = process.communicate()
