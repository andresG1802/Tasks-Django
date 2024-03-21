from django.urls import path , include
from rest_framework import routers
from tasks import views

router = routers.DefaultRouter()
router.register(r'tasks',views.TaskView,'tasks')

urlpatterns = [
    path("api/", include(router.urls))
]
# YA ESTAN CREADA CON ESTA LISTA DE ARRIBA
# GET 
# POST 
# PUT 
# DELETE