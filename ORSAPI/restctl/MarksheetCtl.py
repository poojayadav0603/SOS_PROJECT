


from django.http import HttpResponse
from .BaseCtl import BaseCtl
from django.shortcuts import render
from ORSAPI.utility.DataValidator import DataValidator
from service.models import Marksheet
from service.forms import MarksheetForm
from service.service.MarksheetService import MarksheetService
from django.http.response import JsonResponse
import json
from django.core import serializers

class MarksheetCtl(): 
    def request_to_form(self,requestForm):
        self.form["id"]  = requestForm["id"]
        self.form["rollNumber"] = requestForm["rollNumber"]
        self.form["name"] = requestForm["name"]
        self.form["physics"] = requestForm["physics"]
        self.form["chemistry"] = requestForm["chemistry"]
        self.form["maths"] = requestForm["maths"]
        self.form["student_ID"] = requestForm["student_ID"]



    def get(self,request, params = {}):
        service=MarksheetService()
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
        service=MarksheetService()
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
        print("marksheet search is called")
        json_request=json.loads(request.body)
        if(json_request):
            params["rollNumber"]=json_request.get("rollNumber",None)
        service=MarksheetService()
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
        obj.rollNumber = request["rollNumber"]
        obj.name = request["name"]
        obj.physics=request["physics"]
        obj.physics=request["physics"] 
        obj.chemistry=request["chemistry"] 
        obj.maths=request["maths"] 
        obj.student_ID=request["student_ID"]
        return obj

    def save(self,request, params = {}):        
        json_request=json.loads(request.body)     
        r=self.form_to_model(Marksheet(), json_request)
        service=MarksheetService()
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

    def input_validation(self):
        super().input_validation()
        inputError =  self.form["inputError"]
        if(DataValidator.isNull(self.form["rollNumber"])):
            inputError["rollNumber"] = "roll Number can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["name"])):
            inputError["name"] = "name can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["physics"])):
            inputError["physics"] = "physics can not be null"
            self.form["error"] = True

        if(DataValidator.isNull(self.form["chemistry"])):
            inputError["chemistry"] = "chemistry can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["maths"])):
            inputError["maths"] = "maths can not be null"
            self.form["error"] = True
        if(DataValidator.isNull(self.form["student_ID"])):
            inputError["student_ID"] = "student_ID can not be null"
            self.form["error"] = True

        return self.form["error"]        
    

    # Template html of Role page    
    def get_template(self):
        return "orsapi/Marksheet.html"          

    # Service of Role     
    def get_service(self):
        return MarksheetService()        


       



