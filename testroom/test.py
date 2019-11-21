from pdfminer.converter import TextConverter
from pdfminer.pdfinterp import PDFPageInterpreter, PDFResourceManager
from pdfminer.pdfpage import PDFPage
import re
import io
import json
import requests;
'''
re = requests.get("http://api.github.com")
#re = requests.get("http://www.bilibili.com");
#print(re);
for x in re.json():
    print(x + ": " +re.json().get(x));

#print(serializers.serialize('json',TestStudent.objects.all())
'''
pdf_path = "testroom/Student Information.pdf"
with open(pdf_path, 'rb') as fh:
    for page in PDFPage.get_pages(fh, 
                    caching=True,
                    check_extractable=True):
                resource_manager = PDFResourceManager()
                fake_file_handle = io.StringIO()
                converter = TextConverter(resource_manager, fake_file_handle)
                page_interpreter = PDFPageInterpreter(resource_manager, converter)
                page_interpreter.process_page(page)
                text = fake_file_handle.getvalue()
                #yield text
                # close open handles
                converter.close()
                fake_file_handle.close()

    #yield text
                # close open handles
converter.close()
fake_file_handle.close()
split_text = str(text).split()
#print(split_text)
#print(text)

reg = "\s[A-Z]{2,4}&?\s+[0-9][0-9][0-9]\s";
clist = re.findall(reg,text);
#print(re.findall(reg,text))
for index,element in enumerate(clist):
    element = element.replace(" ","");
    clist[index] = element;
    print(element);
print(clist);
jsFormat = json.dumps(clist)
print(jsFormat)
print(type(jsFormat))
from django.core import serializers
print(serializers.serialize("json",))


'''
class Transcript(models.Model):
    from django.db import models
    from django.contrib.postgres.fields import JSONField
    from django.contrib.postgres.fields import ArrayField

    id = models.IntegerField(primary_key=True)
    #quarter = models.ForeignKey(Quarter,on_delete=models.CASCADE)
    #cid = models.ForeignKey(Classes,on_delete=models.CASCADE)
    cid = ArrayField(
        models.IntegerField(blank=False)
    )
    def __str__ (self):
        return self.id;
#get_Transcript  upload endpoint                        (id,string) return string   return unformat transcript string
#get_classList   get studied classes from transcript    (string) return list           
#get_JS          make classes list into javascript      (list) return string        return formated string 
#save_transcript save javascript into database          (id,string) return boolean  return boolean to see if save success
'''
'''
for index, obj in enumerate(split_text):
            # regex expressions
            # {3,5} 3 to 5 characters
            # [A-Z] capital letters
            # | or 
            # (&amp;|&) ampersand
    skipping = False
    if re.search("^[A-Z]{2,5}$|^[A-Z]{2,4}\&$", obj):
                #if not skipping:
        if index < (len(split_text)-1) and re.search('^[0-9]{3}$', split_text[index + 1]):
                    #skipping = True
                    index_offset = index
                    build_string = ""
                    curernt_string = split_text[index]
                    #print("Start string " + curernt_string)
                    #print (re.search("[0-9].[0,9]", curernt_string))
                    while not re.search("[0-9].[0,9]", curernt_string): 
                        #print("current string " + curernt_string)
                        curernt_string = split_text[index_offset] + " "
                        build_string += curernt_string
                        index_offset += 1
                    #print(build_string)
                #if skip_count == 0:
                    #skip_count = 4
                    #skipping = #False
                    

#call the database def at last
'''