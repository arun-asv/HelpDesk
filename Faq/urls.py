from django.urls import path
from .views import FaqList, FaqDetail

urlpatterns = [
    path('faqlist/',FaqList.as_view(),name='faqlist'),
    path('<int:pk>',FaqDetail.as_view(),name='faqdetail'),
]