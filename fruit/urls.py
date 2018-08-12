from django.conf.urls import url
from fruit.views import *

urlpatterns = [
    url(r'^$', Fruit_list.as_view(), name="fruitview"),
    url(r'^only/$', Fruit_list_only.as_view(), name="fruitview_only"),    
    url(r'^(?P<pk>\d+)/$', fruit_page, name="currentfruit"),

]