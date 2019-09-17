from django.urls import path
from django.urls import register_converter

from reports.converters import DateUrlConverter
from reports.views import UserReportView
from reports.views import UserReportCSVView
from reports.views import UserReportXMLView


register_converter(DateUrlConverter, 'd.m.Y')

# Не очень красиво сделано, но всё до идеала доводить долго
urlpatterns = [
    path('<str:username>/operations/<d.m.Y:date_from>/', UserReportView.as_view()),
    path('<str:username>/operations/<d.m.Y:date_from>/<d.m.Y:date_to>/', UserReportView.as_view()),

    path('<str:username>/operations/csv/<d.m.Y:date_from>/', UserReportCSVView.as_view()),
    path('<str:username>/operations/csv/<d.m.Y:date_from>/<d.m.Y:date_to>/', UserReportCSVView.as_view()),

    path('<str:username>/operations/xml/<d.m.Y:date_from>/', UserReportXMLView.as_view()),
    path('<str:username>/operations/xml/<d.m.Y:date_from>/<d.m.Y:date_to>/', UserReportXMLView.as_view()),
]
