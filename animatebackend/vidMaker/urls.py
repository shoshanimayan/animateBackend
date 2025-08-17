from django.urls import path
from .views import ffmpegHealthAPIView
from .views import ffmpegGenerateVideo

urlpatterns = [
    path('status/', ffmpegHealthAPIView.as_view(), name='ffmpeg_status_check'),
    path('generate/', ffmpegGenerateVideo.as_view(), name='ffmpeg_generate_video'),

]