from django.shortcuts import render, redirect, get_object_or_404
from django.views import View
from .forms import UserForm, LoginForm, PaymentForm
from django.views.generic.edit import FormView, CreateView
from .models import User

from django.contrib.auth.hashers import check_password, make_password
from .models import Match, Invoice
from django.db.models import Q
from info.models import Team
from datetime import date
from django.contrib.auth import login, logout, authenticate
# React imports
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from .serializers import UserSerializer
# Create your views here.

class HomeView(View):
    def get(self, request):
        return render(request, "booking/home_page.html", {
            "username": request.session["username"]
        })
    

class UserRegisterView(CreateView):
    model = User
    form_class = UserForm
    template_name = "booking/user_registration.html"
    success_url = "/login"

    def form_valid(self, form):
        # Hash the password before saving the user instance
        form.instance.password = make_password(form.cleaned_data['password'])
        return super().form_valid(form)

def main_view(request):

    return render(request, 'booking/main.html')
    

def login_view(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            user_name = form.cleaned_data['user_name']
            password = form.cleaned_data['password']
            
            try:
                user = User.objects.get(user_name=user_name)
                if check_password(password, user.password):
                    # Password matches, log in the user
                    name = user_name
                    request.session["username"] = name
                    request.session['user_id'] = user.pk
                    return render(request, "booking/home_page.html", {
                        "username": name
                    })
                else:
                    # Invalid password, show an error message
                    error_message = "Invalid username or password."
                    return render(request, 'booking/login.html', {'form': form, 'error_message': error_message})
            except User.DoesNotExist:
                # User does not exist, show an error message
                error_message = "Invalid username or password."
                return render(request, 'booking/login.html', {'form': form, 'error_message': error_message})
    else:
        form = LoginForm()
    return render(request, 'booking/login.html', {'form': form})

def logout1(request):
    logout(request)
    return redirect('login')

def upcoming_matches(request):
    teams = Team.objects.all()
    selected_team_id = request.GET.get("team")
    if selected_team_id:
        upcoming_matches = Match.objects.filter(match_name__contains=selected_team_id)
    else:
        upcoming_matches = Match.objects.filter(match_date__gte=date.today())

    context = {
        'upcoming_matches': upcoming_matches,
        'teams': teams,
    }
    return render(request, "booking/matches.html", context)

def select_stands(request, pk):
    match = get_object_or_404(Match, pk=pk)
    stands = [
        {'name': 'A', 'rate': 500, 'available_tickets': match.available_seats_A},
        {'name': 'B', 'rate': 1000, 'available_tickets': match.available_seats_B},
        {'name': 'C', 'rate': 1500, 'available_tickets': match.available_seats_C},
        {'name': 'D', 'rate': 2000, 'available_tickets': match.available_seats_D},
    ]
    if request.method == 'POST':
        total_tickets = sum(int(request.POST.get(f'tickets_{stand["name"]}', 0)) for stand in stands)
        if total_tickets == 0:
            return render(request, 'booking/select_stands.html', {'match': match, 'stands': stands, 'error_message': 'Please select at least 1 ticket.'})
        if total_tickets > 5:
            return render(request, 'booking/select_stands.html', {'match': match, 'stands': stands, 'error_message': 'You cannot book more than 5 tickets in total.'})
        
        selected_stands_data = []
        total_amount = 0
        for stand in stands:
            ticket_count = int(request.POST.get(f'tickets_{stand["name"]}', 0))
            if ticket_count > 0:
                selected_stands_data.append({'stand': stand['name'], 'num_tickets': ticket_count})
                total_amount += ticket_count * stand['rate']

        request.session["selected_stands"] = selected_stands_data
        request.session["total_amount"] = total_amount
        request.session["match_id"] = match.pk
        return redirect('check_out')
    
    return render(request, 'booking/select_stands.html', {'match': match, 'stands': stands})


def check_out(request):
    selected_stands = request.session.get('selected_stands', [])
    total_amount = request.session.get('total_amount', 0)

    return render(request, 'booking/checkout.html', {'selected_stands': selected_stands, 'total_amount': total_amount})


def payment_view(request):
    if request.method == 'POST':
        form = PaymentForm(request.POST)
        if form.is_valid():
            selected_stands = request.session.get("selected_stands")
            total_amount = request.session.get("total_amount")
            match_id = request.session.get("match_id")
            match = Match.objects.get(pk=match_id)
            print(match)
            print(selected_stands)
            print(total_amount)
            a=b=c=d=0
            for stands in selected_stands:
                if stands["stand"] == "A":
                    match.available_seats_A -= stands["num_tickets"]
                    a= stands["num_tickets"]
                elif stands["stand"] == "B":
                    match.available_seats_B -= stands["num_tickets"]
                    b= stands["num_tickets"]
                elif stands["stand"] == "C":
                    match.available_seats_C -= stands["num_tickets"]
                    c= stands["num_tickets"]
                elif stands["stand"] == "D":
                    match.available_seats_D -= stands["num_tickets"]
                    d= stands["num_tickets"]
            match.save()

            invoice = Invoice(
                user=User.objects.get(pk=request.session['user_id']),
                match=match,
                total_cost=total_amount,
                seats_in_stand_A=a,
                seats_in_stand_B=b,
                seats_in_stand_C=c,
                seats_in_stand_D=d,
            )
            invoice.save()
            return redirect('invoice')

    else:
        form = PaymentForm()
    
    return render(request, 'booking/payment.html', {'form': form})

def invoice_view(request):
    invoice_= Invoice.objects.filter(user=request.session['user_id'])[::-1]
    invoice_filtered=invoice_[0]
    return render(request, "booking/invoice.html", {
                "invoice": invoice_filtered
            })

def booked_tickets(request):
    invoices= Invoice.objects.filter(user=request.session['user_id']).order_by("match__match_date")
    return render(request, "booking/booked_tickets.html", {
        "invoices":invoices
    })


#React views
class UserRegisterAPIView(APIView):
    def post(self, request, format=None):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            # Hash the password before saving the user instance
            serializer.save(password=make_password(serializer.validated_data['password']))
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)