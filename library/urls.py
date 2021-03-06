from django.conf.urls import url, include

# from library.views import BookBorrowView
from . import views

urlpatterns = [
    url('^$', views.index, name='index'),
    url('^books/$', views.BookListView.as_view(), name="books"),
    url('book/(?P<pk>\d+)$', views.BookDetailView.as_view(), name='book-detail'),
    url('book/borrow$', views.book_borrow, name='book-borrow'),
    url('book/reserve$', views.book_reserve, name='book-reserve'),
    # url('^book/(?P<pk>\d+)/update/$', views.book_update, name='book-update'),
    # 我的借书
    url('^mybooks/$', views.LoanedBooksByUserListView.as_view(), name='my-borrowed'),
    url('^mybooks-return/$', views.mybooks_return, name='mybooks-return'),
    url('^mybooks-renew/$', views.mybooks_renew, name='mybooks-renew'),
    # 我的预约
    url('^myreserves/$', views.ReservedBook.as_view(), name='my-reserves'),
    url('^reserve/borrow$', views.reserve_borrow, name='reserve-borrow'),
    # 我的罚款
    url('^mypenalties/$', views.Penalties.as_view(), name='my-penalties'),
    url('^penalty/pay$', views.penalty_pay, name='penalty-pay'),
    # 注册和登录
    url('accounts/', include('django.contrib.auth.urls')),
    url('^accounts/register/$', views.register.as_view(), name="register"),
    # url('^book/create/$', views.BookCreate.as_view(), name="book-create"),
    # url('^book/borrow/$', require_POST(BookBorrowView.as_view()), name='book-borrow'),
    # url('book/(?P<pk>\d+)/delete/$', views.BookDelete.as_view(), name='book-delete'),
]
