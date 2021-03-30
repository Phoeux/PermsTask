from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter

from api import views

router = DefaultRouter()
router.register('user', views.UserModelView, basename='user'),
router.register('plotter', views.PlotterModelView, basename='plotter'),
router.register('pattern', views.PatternModelView, basename='pattern'),
router.register('plotter_pattern', views.PlotterPatternModelView, basename='plotter_pattern'),
router.register('perms', views.PermissionsModelView, basename='perms'),
router.register('plotter_obj_perms', views.PlotterUserObjectPermissionModelView, basename='plotter_obj_perms'),
router.register('pattern_obj_perms', views.PatternUserObjectPermissionModelView, basename='pattern_obj_perms'),

urlpatterns = [
    path('', include((router.urls, 'api'))),
    path('seaborn/', views.SeabornStats.as_view(), name='seaborn'),
]
