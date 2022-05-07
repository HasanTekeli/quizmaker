from django.urls import path, re_path
from .views import (exam_detail_update, 
                        ExamListView, 
                        exam_detail,
                        ArchivedExamListView,
                        archive_exam
                        )

app_name = 'quiz'

urlpatterns = [
    path('', ExamListView.as_view(), name='exam_list'),
    path('archived/', ArchivedExamListView.as_view(), name='archived_exam_list'),
    path('<int:exam_id>/archive_exam/', archive_exam, name='archive_exam'),
    path('<int:exam_id>/duzenle/', exam_detail_update, name='exam_detail_update'),
    path('<int:exam_id>/', exam_detail, name='exam_detail'),
    
]
