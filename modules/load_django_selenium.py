import sys
import os
import django

sys.path.append('E:/projects/scraping_test_task/brain_selenium_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'brain_selenium_project.settings'
django.setup()