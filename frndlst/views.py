from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from frndlst.frndSerializers import *

# Create your views here.

class frnd(APIView):
    def get_user(self, id):
        try:
            model = frnd_list.objects.get(id=id)
            print("model get user ", model)
            return model

        except frnd_list.DoesNotExist:
            print("get user id ", id)
            return Response(f'User with employee id {id} is not found in Database',
                            status=status.HTTP_404_NOT_FOUND)

    def get(self, request):
        model = frnd_list.objects.all()
        print("get start function")
        # serializer = serializerClass(model,many=True)
        serializer = Frnd_listClass(model, many=True)
        return Response(serializer.data)

    def post(self, request):
        # model = Users.objects.all()
        serializer = Frnd_listClass(data=request.data)

        if (serializer.is_valid()):
            serializer.save()
            print("\n\n---------------------")
            print("data post: ", serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            # return "SignUp successfull!!!"
            return Response("successfull!!!", status.HTTP_201_CREATED)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def put(self, request, id):
        serializer = Frnd_listClass(self.get_user(id), data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response("Put successfull !!!", status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    def delete(self, request, id):
        model = self.get_user(id)
        model.delete()
        print("deleted user", id)
        return Response(status=status.HTTP_204_NO_CONTENT)



    '''
    def post(self, request):
        serializer = Frnd_listClass(data=request.data)
        print("data",request.data)
        if (serializer.is_valid()):
            serializer.save()
            print("seriali value",serializer.data)
            print("\n\n---------------------")
            print("data post: ", serializer.data)
            print("data post type : ", type(serializer.data))
            print("\n-----------------------")
            return Response("Operation successfull!!!", status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
'''
    '''
def getF(request,id=0):
        print("inside getf")


        if request.method=='POST':
            user_post_data= JSONParser().parse(request)
            print(" user post data: ", user_post_data)
            user_serializer= Frnd_listClass(data=user_post_data)

            if user_serializer.is_valid():
                print("inside user serializer")
                user_serializer.save()
                print("serial value", user_serializer.data)
                return JsonResponse(" successfull!!!",safe= False)

            return JsonResponse(user_serializer.errors,safe=False)
'''