from django.urls import path
from .views import DepartmentList, DepartmentDetail

urlpatterns=[
    path('list/', DepartmentList.as_view(), name='department-list'),
    path('<int:pk>', DepartmentDetail.as_view(), name='department-detail')
]