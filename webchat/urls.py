from django.urls import path
from .views import WebChatTop

urlpatterns = [
    path('top/', WebChatTop.as_view(), name='top'),  # 追記
]
