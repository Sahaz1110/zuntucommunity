from django.contrib import admin
from django.urls import path, include
from students import views  # Correct import statement

urlpatterns = [
    path('admin/', admin.site.urls),
    path('students/', include('students.urls')),  # Include URLs from the students app
# Other URL pat
    #path('student/<int:student_id>/delete/', delete_student, name='delete_student'),
    #path('student/<int:student_id>/', views.student_detail, name='student_detail'),

    # Your other URL patterns...


] #+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)