
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.forms import SubjectForm
from service.models import  Subject
from service.service.SubjectService import SubjectService

class SubjectListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["subjectName"] = requestForm.get( "subjectName", None)
        self.form["subjectDescription"] =  requestForm.get( "subjectDescription", None) 
        self.form["dob"] =  requestForm.get( "dob", None) 
        self.form["mobileNumber"] =  requestForm.get( "mobileNumber", None)
        self.form["course_ID"] =  requestForm.get( "course_ID", None)
        self.form["courseName"] =  requestForm.get( "courseName", None)


    def display(self,request,params={}):
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list})
        return res

    def submit(self,request,params={}):
        self.request_to_form(request.POST)
        self.page_list = self.get_service().search(self.form)
        res = render(request,self.get_template(),{"pageList":self.page_list, "form":self.form})
        return res
        
    def get_template(self):
        return "orsapi/SubjectList.html"          

    # Service of Role     
    def get_service(self):
        return SubjectService()        




