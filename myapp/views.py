from rest_framework.response import Response
from rest_framework.views import APIView
from .models import TrackerModel
import time
from .openapi import Textinitiator,ImageInitiator
from .models import ImageSearch as ImgSearch,Textsearch
from .serializers import TextSerializer,Imageserializer


class firstView(APIView):
    def get(self,request):
        return Response({"res":"installation Succesful"})

class searchInfo(APIView):
    def post(self,request):
        value = request.data["text"]
        currentTime = round(time.time())
        tracker = TrackerModel.objects.get(id=1)
        timeDif = currentTime - tracker.lastupdated 
        if timeDif > 60:
            tracker.lastupdated = currentTime
            tracker.textcount = 0
            tracker.save()
            response = Textinitiator(value)
            Textsearch.objects.create(text=value)
            history = TextSerializer(Textsearch.objects.all().order_by("-time",),many=True).data
            length = history[0:10]
            return Response({"res":f"request Successfully reseted new time is {currentTime}","data":response,"history":length})
        if tracker.textcount < 17:
            tracker.textcount = tracker.textcount + 1
            tracker.save()
            response = Textinitiator(value)
            Textsearch.objects.create(text=value)
            history = TextSerializer(Textsearch.objects.all().order_by("-time",),many=True).data
            length = history[0:10]
            return Response({"res":f"request succesfull count is now {tracker.textcount + 1}","data":response,"history":length})
        else:
            return Response({"res":f" {60-timeDif} seconds"},status=201)

    
class ImageSearch(APIView):
    def post(self,request):
        print(request.data)
        value = request.data["text"]
        currentTime = round(time.time())
        tracker = TrackerModel.objects.get(id=1)
        timeDif = currentTime - tracker.imglastupdated
        if timeDif > 60:
            tracker.imglastupdated = currentTime
            tracker.imageCount = 0
            tracker.save()
            response = ImageInitiator(value)
            ImgSearch.objects.create(text=value)
            history = Imageserializer(ImgSearch.objects.all().order_by("-time",),many=True).data
            return Response({"res":f"request Successfully reseted new time is {currentTime}","data":response,"history":history[0:10]})
        if tracker.imageCount < 46:
            tracker.imageCount = tracker.imageCount + 2
            tracker.save()
            response = ImageInitiator(value)
            ImgSearch.objects.create(text=value)
            history = Imageserializer(ImgSearch.objects.all().order_by("-time",),many=True).data
            return Response({"res":f"request succesfull count is now {tracker.imageCount + 2}","data":response,"history":history[0:10]})
        else:
            return Response({"res":60-timeDif},status=201)


class NavBarList(APIView):
    def get(self,request):
        texts = TextSerializer(Textsearch.objects.all().order_by("-time",),many=True).data[0:10]
        images = Imageserializer(ImgSearch.objects.all().order_by("-time",),many=True).data[0:10]
        return Response({"texts":texts,"images":images})