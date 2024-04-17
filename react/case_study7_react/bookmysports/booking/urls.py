from django.urls import path
from . import views

urlpatterns = [
    path("registration", views.UserRegisterView.as_view(), name="registration"),
    path("",views.main_view, name="main"),
    path("login", views.login_view, name="login"),
    path("logout1", views.logout1, name="logout1"),
    path("home", views.HomeView.as_view(), name="home"),
    path('upcoming-matches/', views.upcoming_matches, name='upcoming_matches'),
    path("book-match/<int:pk>", views.select_stands, name="book_match"),
    path("checkout", views.check_out, name="check_out"),
    path("payment", views.payment_view, name="payment"),
    path("invoice", views.invoice_view, name='invoice'),
    path("booked-tickets", views.booked_tickets, name="booked_tickets"),
    #react part apis
    path('api/register/', views.UserRegisterAPIView.as_view(), name='register_api')

]
