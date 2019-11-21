#import unittest;
from django.test import TestCase;
from rest_framework.test import APIRequestFactory;
from ...models import *;
from ...views import *;

#  /home/pmx990/文档/DR# python3 manage.py test composeexample.test.unit_test.ut.checkViews
#  remember to use newenv/bin/activate to make the enviroment if your are not using docker

class checkViews(TestCase):
    def setUp(self):
        print("init");

    def  tearDown(self):
        print("end");

    def test_01(self):
        pdf_path = "composeexample/Student Information.pdf"
        #print(FileUploadViewTest.extract_text_by_page(pdf_path))
        raw_str = FileUploadViewTest.extract_text_by_page(pdf_path)
        list1 = FileUploadViewTest.convert_to_list(raw_str)
        jsonf = FileUploadViewTest.convert_to_json(list1)
        FileUploadViewTest.save_to_db(jsonf,1)
        q = Student(id=1)
        print(q.classes)
