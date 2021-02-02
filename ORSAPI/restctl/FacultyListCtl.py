




from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.forms import FacultyForm
from service.models import  Faculty
from service.service.FacultyService import FacultyService 

class FacultyListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["firstName"] = requestForm.get( "firstName", None)
        self.form["lastName"] =  requestForm.get( "lastName", None) 
        self.form["email"] =  requestForm.get( "email", None) 
        self.form["password"] =  requestForm.get( "password", None) 
        self.form["address"] =  requestForm.get( "address", None) 
        self.form["gender"] =  requestForm.get( "gender", None) 
        self.form["dob"] =  requestForm.get( "dob", None) 
        self.form["college_ID"] =  requestForm.get( "college_ID", None) 
        self.form["subject_ID"] =  requestForm.get( "subject_ID", None) 
        self.form["course_ID"] =  requestForm.get( "course_ID", None) 
       
   

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
        return "orsapi/AddFacultyList.html"          

    # Service of Role     
    def get_service(self):
        return FacultyService()        


