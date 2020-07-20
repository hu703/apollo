from django.urls import path
from app import views

app_name = 'app'
urlpatterns = [
    path('',views.index,name='index'),  # 配置访问首页的路由
    path('login',views.login,name='login'),
    path('safeb/',views.safeB,name='safeb') # 配置安全等级为B的路由  特性B
]