from typing import Pattern
from django.urls import path
from . import views

urlpatterns=[
    # path('january',views.index_jan),
    # path('february',views.index_feb),
    # path('<month>',views.every_month), (here,<var_name> is for dynamic input 
    path("",views.home_page,name='index'),
    path("<int:month>",views.num_months),
    path("<str:month>",views.get_months, name='month_info')  #(<slug>->'<str:var_name> consider i/p as string)
    
]