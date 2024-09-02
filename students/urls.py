from students import views
from django.urls import path
from .views import edit_student, delete_student
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', views.student_list, name='student_list'),
    path('create/', views.student_create, name='student_create'),
    #path('home/', views.home, name='home'),
    # Other URL patterns...
    path('student/<int:student_id>/edit/', edit_student, name='edit_student'),
    path('student/<int:student_id>/delete/', delete_student, name='delete_student'),
    path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    # Your other URL patterns...


] 
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


