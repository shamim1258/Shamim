# Rest API example

This example shows the function and class based views keeping all the files and we can use the class based views.py file or function based from below.

**urls.py**

     urlpatterns = [
       path('admin/', admin.site.urls),
       path('students/', views.students_list),
       path('students/', views.students_details),
     ]

**Models.py**  

    class Students(models.Model):
      id = models.IntegerField(primary_key=True)
      name = models.CharField(max_length = 20)
      score = models.DecimalField(max_digits=10,decimal_places=3)

      def __str__(self):
        return self.id+self.name+self.score
        
**serializers.py**

     from rest_framework import serializers
     from students.models import Students

     class StudentSerializers(serializers.ModelSerializer):
       class Meta:
         model = Students
         fields = ["id","name","score"]
         
**Views.py**
This views file is for the function based views

     from students.models import Students
     from students.serializers import StudentSerializers
     from rest_framework.response import Response
     from rest_framework import status
     from rest_framework.decorators import api_view

     @api_view(['GET','POST'])
     def students_list(request):
       if request.method == 'GET':
         students = Students.objects.all()
         serializers = StudentSerializers(students,many=True)
         return Response(serializers.data)

       elif(request.method == 'POST'):
         serializers = StudentSerializers(data=request.data)
         if serializers.is_valid():
            serializers.save()
            return Response(serializers.data,status=status.HTTP_201_CREATED)
       return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

     api_view(['GET','PUT','DELETE'])
     def students_details(request,pk):
       try:
         student = Students.objects.get(pk=pk)
       except Students.DoesNotExist:
         return Response(status=status.HTTP_404_NOT_FOUND)

       if request.method == 'GET':
         serializers = StudentSerializers(Students)
         return Response(serializers.data)

       elif request.method == 'PUT':
         serializers = StudentSerializers(Students,request.data)
         if serializers.is_valid():
            serializers.save()
            return Response(serializers.data)
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

       elif request.method == 'DELETE':
         Students.delete()
         return Response(status=status.HTTP_204_NO_CONTENT)
         
**Views.py**
This views file used for class based views keeping rest of the other files same.

     from students.models import Students
     from students.serializers import StudentSerializers
     from rest_framework.response import Response
     from rest_framework import status
     from rest_framework.views import APIView
     
     class SturdentList(APIView):
       def get(self, request):
         students = Students.objects.all()
         serializers = StudentSerializers(students,many=True)
         return Response(serializers.data)
         
       def post(self, request):
         serializers = StudentSerializers(data=request.data)
           if serializers.is_valid():
             serializers.save()
             return Response(serializers.data,status=status.HTTP_201_CREATED)
         return Response(serializers.errors,status=status.HTTP_400_BAD_REQUEST)

    class SturdentList(APIView):
         def get_object(self, pk):
             try:
                 return Students.objects.get(pk=pk)
             except Students.DoesNotExist:
                 raise Http404

         def get(self, request, pk, format=None):
             students = self.get_object(pk)
             serializer = StudentSerializers(students)
             return Response(serializer.data)

         def put(self, request, pk, format=None):
             students = self.get_object(pk)
             serializer = StudentSerializers(students, data=request.data)
             if serializer.is_valid():
                 serializer.save()
                 return Response(serializer.data)
             return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

         def delete(self, request, pk, format=None):
             students = self.get_object(pk)
             students.delete()
             return Response(status=status.HTTP_204_NO_CONTENT)
