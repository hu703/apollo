from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),  # 配置访问首页的路由
    path('safe/',views.safeA,name='safe')  # 配置访问安全等级A的路由
]