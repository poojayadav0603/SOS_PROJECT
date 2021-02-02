
from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.forms import UserForm
from service.models import  User
from service.service.UserService import UserService

class UserListCtl(BaseCtl):

    def request_to_form(self,requestForm):
        self.form["firstName"] = requestForm.get( "firstName", None)
        self.form["lastName"] =  requestForm.get( "lastName", None) 
        self.form["login_id"] =  requestForm.get( "login_id", None) 
        self.form["password"] =  requestForm.get( "password", None)
        self.form["confirmpassword"] =  requestForm.get( "confirmpassword", None)
        self.form["dob"] =  requestForm.get( "dob", None)
        self.form["address"] =  requestForm.get( "address", None)
        self.form["gender"] =  requestForm.get( "gender", None)
        self.form["mobilenumber"] =  requestForm.get( "mobilenumber", None)
        self.form["role_Id"] =  requestForm.get( "role_Id", None)
        self.form["role_Name"] =  requestForm.get( "role_Name", None)


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
        return "orsapi/UserList.html"          

    # Service of Role     
    def get_service(self):
        return UserService()        




