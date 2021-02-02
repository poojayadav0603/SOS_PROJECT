


from service.models import Subject
from service.utility.DataValidator import DataValidator
from .BaseService import BaseService

'''
It contains Student business logics.   
'''
class SubjectService(BaseService):
    
    def search(self,params):
        q = self.get_model().objects.filter()

        val = params.get("id",None)
        if( DataValidator.isInt(val)):
            q= q.filter( id = val)

        val = params.get("subjectName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( subjectName = val)

        val = params.get("subjectDescription",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( subjectDescription = val)

        val = params.get("dob",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( dob = val)

        val = params.get("course_ID",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( course_ID = val)

        val = params.get("courseName",None)
        if( DataValidator.isNotNull(val)):
            q= q.filter( courseName = val)
        
        return q
        # val = params.get("college_ID",None)
        # if( DataValidator.isNotNull(val)):
        #     q= q.filter( college_ID = val)

        # val = params.get("collegeName",None)
        # if( DataValidator.isNotNull(val)):
        #     q= q.filter( collegeName = val)
        

    def get_model(self):
        return Subject
