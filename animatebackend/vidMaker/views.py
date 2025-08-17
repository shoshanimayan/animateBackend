from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from helpers.ffmpegCheck import isFfmpegInstalled
from helpers.datauriConvert import SaveDataUriToPng, ClearFolder
from helpers.ffmpegPngToVid import createVideoFromPngs
from rest_framework import serializers
from django.http import FileResponse
import os



class ffmpegHealthAPIView(APIView):
    def get(self, request, format=None):
        hasFfmpeg = isFfmpegInstalled()
        return Response({'available':hasFfmpeg }, status=status.HTTP_200_OK)
    
class ffmpegGenerateVideo(APIView):
    def post(self, request, format=None):
        if 'images' not in request.data:
            return Response({"error": f"Expected 'images' as a list in the request body. got {request.data['images']} "},
                            status=status.HTTP_400_BAD_REQUEST)

        images = request.data['images']
        processed_value = len(images)
        ClearFolder("/vidMaker/output")
        ClearFolder("/vidMaker/input")
        SaveDataUriToPng(images,os.getcwd()+"/vidMaker/input","frame",len(str(processed_value)))
        createVideoFromPngs("/vidMaker/input","/vidMaker/output/output.mp4","frame%0"+str(len(str(processed_value)))+"d.png")
        video = open(os.getcwd()+"/vidMaker/output/output.mp4", 'rb')
        response = FileResponse(video, content_type='video/mp4')
        response['Content-Disposition'] = f'attachment; filename=output.mp4' 
        return response
