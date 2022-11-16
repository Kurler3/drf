from django.urls import path

from . import views

urlpatterns = [
    # LIST + CREATE VIEW
    path('', views.ProductCreateAPIView.as_view()),
    # DETAIL VIEW
    path('<int:pk>/', views.ProductDetailAPIView.as_view()),
    # DELETE
    path('<int:pk>/delete/', views.ProductDeleteAPIView.as_view()),
    # UPDATE
    path('<int:pk>/update/', views.ProductUpdateAPIView.as_view()),
]
