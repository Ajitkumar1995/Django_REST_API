from rest_framework.pagination import PageNumberPagination,LimitOffsetPagination,CursorPagination
class Mypagination(PageNumberPagination):
    page_size=5
    page_query_param = 'mypage' #default value is page
    page_size_query_param = 'num'
    max_page_size = 15
    last_page_strings = ('endpage',) #default value is('Last')

class Mypagination2(LimitOffsetPagination):
    default_limit = 15
    limit_query_param = 'mylimit'
    offset_query_param = 'myoffset',
    max_limit = 20

class Mypagenation3(CursorPagination):
    ordering = 'esal' #ascending
    #ordering = '-esal' #descending
    page_size = 5


