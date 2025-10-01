import sys
import os
import django

sys.path.append('E:/projects/scraping_test_task/brain_playwright_project') 
os.environ['DJANGO_SETTINGS_MODULE'] = 'brain_playwright_project.settings'
django.setup()