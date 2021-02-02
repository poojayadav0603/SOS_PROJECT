


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Course
from service.forms import CourseForm
from service.service.CourseService import CourseService
from django.http.response import JsonResponse
import json
from django.core import serializers

class CourseCtl(BaseCtl): 
    def get(self,request, params = {}):
        service=CourseService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res["data"]})

    def delete(self,request, params = {}):
        service=CourseService()
        c=service.get(params["id"])
        res={}
        if(c!=None):
            service.delete(params["id"])
            res["data"]=c.to_json()
            res["error"]=False
            res["message"]="Data is Successfully deleted"
        else:
            res["error"]=True
            res["message"]="Data is not deleted"
        return JsonResponse({"data":res["data"]})

    

    def search(self,request, params = {}):
        json_request=json.loads(request.body)
        if(json_request):
            params["courseName"]=json_request.get("courseName",None)
        service=CourseService()
        c=service.search(params)
        res={}
        data=[]
        for x in c:
            data.append(x.to_json())
        if(c!=None):
            res["data"]=data
            res["error"]=False
            res["message"]="Data is found"
        else:
            res["error"]=True
            res["message"]="record not found"
        return JsonResponse({"data":res})

    def form_to_model(self,obj,request):
        pk = int(request["id"])
        if(pk>0):
            obj.id = pk
        obj.courseName = request["courseName"]
        obj.courseDescription = request["courseDescription"]
        obj.courseDuration=request["courseDuration"] 
        return obj

    def request_to_form(self, requestForm):
      
        self.form["collegeName"] = requestForm.get("collegeName")
        self.form["collegeAddress"] = requestForm.get("collegeAddress", None)
        self.form["collegeState"] = requestForm.get("collegeState", None)
        self.form["collegeCity"] = requestForm.get("collegeCity", None)
        self.form["collegePhoneNumber"] = requestForm.get("collegePhoneNumber", None)
        self.form["id"]= requestForm.get( "id", None)

    def save(self,request, params = {}):        
        json_request=json.loads(request.body)     
        r=self.form_to_model(Course(), json_request)
        service=CourseService()
        c=service.save(r)
        res={}
        if(r!=None):
            res["data"]=r.to_json()
            res["error"]=False
            res["message"]="Data is Successfully saved"
        else:
            res["error"]=True
            res["message"]="Data is not saved"
        return JsonResponse({"data":res})

    # Template html of Role page    
    def get_template(self):
        return "orsapi/Course.html"          

    # Service of Role     
    def get_service(self):
        return CourseService()        


       



