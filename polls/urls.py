from django.urls import path
from . import views
urlpatterns=[
    path('',views.toLogin_view),
    path('index/',views.Login_view),
    path('register/',views.register_view),
    path('toregister/',views.toregister_view),
    path('chart/',views.chart_view),
    path('get_data/', views.get_data),
    path('stock_data/', views.stock_data,name="stock_data"),
    path('code_data/', views.code_data,name="code_data"),
    path('code_data2/', views.code_data2,name="code_data2"),
    path('stock_chart/', views.stock_chart,name='stock_chart'),
    path('test/', views.test),
    path('drag/', views.drag,name="drag"),
    path('extract/', views.extract_content, name='extract_content'),
    path('views/', views.your_view, name='your_view'),
    path('views2/', views.view_s),
    path('match/', views.match,name='match'),
    path('match2/', views.match2,name='match2'),
    path('matchdata/', views.match_data, name='match_data'),
    # path('matchresult/', views.get_latest_newmatch_values, name='matchresult'),
    path('matchre/', views.match_views,name="matchre"),
    path('Rresult/', views.Rresult,name="Rresult"),
    path('wait/', views.wait,name="wait"),
    path('wait2/', views.wait2,name="wait2"),
    path('resultmatch/', views.resultmatch,name="resultmatch"),

]