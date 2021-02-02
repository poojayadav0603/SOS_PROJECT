


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Subject
from service.forms import SubjectForm
from service.service.SubjectService import SubjectService

from django.http.response import JsonResponse
import json
from django.core import serializers

class SubjectCtl(): 
    def get(self,request, params = {}):
        service=SubjectService()
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
        service=SubjectService()
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
            params["subjectName"]=json_request.get("subjectName",None)
                        
        service=SubjectService()
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
        obj.subjectName = request["subjectName"]
        obj.subjectDescription = request["subjectDescription"]
        obj.dob=request["dob"] 
        obj.course_ID=request["course_ID"]
        obj.courseName=request["courseName"]
        
        return obj
 


    def save(self,request, params = {}):        
        json_request=json.loads(request.body)     
        r=self.form_to_model(Subject(), json_request)
        service=SubjectService()
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
        return "orsapi/Subject.html"          

    # Service of Role     
    def get_service(self):
        return SubjectService()        


       



