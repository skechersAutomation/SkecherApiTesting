import os 
import datetime


basename = "allure-results" 
suffix = datetime.datetime.now().strftime("%y-%m-%d_%H-%M-%S")
filename = "".join([basename, suffix])
print(f'pytest --alluredir {filename} ./SUITES')
os.system(f'pytest --alluredir {basename} ./SUITES')
