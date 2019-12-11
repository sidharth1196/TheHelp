from django.shortcuts import render, redirect
from WorkOrder.forms import QuoteForm
from User.models import Worker, UserProfile
from WorkOrder.models import  Quote, Order
import datetime
# Create your views here.

def create_quote(request, worker_id, userprofile_id):
    generated = False
    if request.method == 'POST':
        quote_form = QuoteForm(data = request.POST)
        if quote_form.is_valid():
            quote = quote_form.save(commit=False)
            quote.modified_date = datetime.datetime.now()
            worker = Worker.objects.get(id=worker_id)
            user = UserProfile.objects.get(user__id=userprofile_id)
            quote.user_id = user
            quote.worker_id = worker
            quote.save()
            generated = True
    else:
        quote_form = QuoteForm()
    return render(request, 'WorkOrder/quote.html', {'quote_form':quote_form, 'generated': generated})

def confirm_booking(request, worker_id, quote_id):
    q = Quote.objects.get(id=quote_id)
    q.processed = True
    q.save()
    o = Order.objects.create(title=q.title, quote=q, amount=q.charge, status='Accepted', worker=q.worker_id, user=q.user_id)
    return redirect('/user/user_login/workerprofile/%d' %worker_id)

def completion(request, worker_id, order_id):
    o = Order.objects.get(id=order_id)
    o.completed_date = datetime.datetime.now()
    o.status = 'Completed'
    o.save()
    w = Worker.objects.get(user__id = worker_id)
    w.total_money = w.total_money + o.amount
    w.save()
    return redirect('/user/user_login/workerprofile/%d' %worker_id)