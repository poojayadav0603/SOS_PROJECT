


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import User
from service.forms import UserForm
from service.service.UserService import UserService
from django.http.response import JsonResponse
import json
from django.core import serializers
from django.contrib.sessions.models import Session

class LoginCtl(BaseCtl):
    def request_to_form(self, requestForm):
        self.form["login_id"] = requestForm["login_id"]
        self.form["password"] = requestForm["password"]
        

    def form_to_model(self,obj,request):
        obj.login_id = request["login_id"]
        obj.password = request["password"]
        return obj



    def logout(self,request,params = {}):

        Session.objects.all().delete()
        self.form["error"]=False
        self.form["message"]="Logout successfully"
        res=JsonResponse({"form":self.form})
        return res



    def auth(self,request,params = {}):
        json_request=json.loads(request.body)    
        q = User.objects.filter()
        res={}
        if(json_request.get("login_id")!=None ):
            q= q.filter( login_id = json_request.get("login_id"))  
        if(json_request.get("password")!=None ):
            q= q.filter( password = json_request.get("password"))
        userList = q
        if (userList.count() > 0):
            self.form["error"]=False
            self.form["message"]="Login Successfully"
            request.session["user"] = userList[0]        
            data= userList[0].to_json()
            self.form["sessionKey"]=request.session.session_key
            self.form["data"]=data
            res=JsonResponse({"form":self.form})

        else:
            self.form["error"]=True
            self.form["message"]="Login Id and Password is wrong"
            res=JsonResponse({"form":self.form})
        return res


    # Template html of Role page    
    def get_template(self):
        return "orsapi/Login.html"          

    # Service of Role     
    def get_service(self):
        return UserService()        