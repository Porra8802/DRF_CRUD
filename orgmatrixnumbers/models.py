from email.policy import default
from django.db import models
from django.http import JsonResponse

class OrgMatrixNumbers(models.Model):
    
    sin_clasificar=models.CharField(max_length=150, default='[3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2]')
    clasificado=models.CharField(
        max_length=150, 
        default='[1, 2, 3, 4, 5, 6, 7, 8, 5, 3, 4, 7, 1]'
    )
   
    def orgnum(request):
        sin_clasificar=[3, 5, 5, 6, 8, 3, 4, 4, 7, 7, 1, 1, 2]
        sorted_data= sorted(sin_clasificar)
        repeated=[]
        new_data=[]
        for i in range(len(sorted_data)): 
            if i not in new_data:
                new_data.append(i)
            else:
                repeated.append(i)
        
        clasificado=new_data+repeated

        return JsonResponse(sin_clasificar, clasificado)

    def __str__(self) -> str:
        return self.clasificado


   
    
