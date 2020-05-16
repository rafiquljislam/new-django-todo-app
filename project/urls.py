from django.contrib import admin
from django.urls import path

from todo import views as todoViews

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', todoViews.IndexView.as_view(), name='home'),
    path('complate/<int:id>/', todoViews.ComplateView.as_view(), name='complate'),
    path('deletecomplete/', todoViews.DeleteCompleteView.as_view(), name='deletecomplete'),
    path('deleteall/', todoViews.DeleteAllView.as_view(), name='deleteall'),
]
