

from django.contrib import admin
from django.urls import path,include
from task import views
from rest_framework.routers import DefaultRouter


router=DefaultRouter()
router.register('candidateapi',views.CandidateModelViewSet,basename='candidate')
router.register('testapi',views.Test_scoreModelViewSet,basename='test')
urlpatterns = [
    path('admin/', admin.site.urls),
    path('',include(router.urls)),
    path('score/', views.get_highest),

]
