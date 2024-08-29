from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import MenuItem, Order
from .forms import OrderForm

# View to display the menu
def menu_view(request):
    menu_items = MenuItem.objects.all()  # Fetch all menu items from the database
    return render(request, 'menu.html', {'menu_items': menu_items})

# View to handle placing an order
def place_order(request):
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()  # Save the order to the database
            return redirect('order_success')  # Redirect to a success page
    else:
        form = OrderForm()
    return render(request, 'place_order.html', {'form': form})

# View to show order success page
def order_success(request):
    return render(request, 'order_success.html')

# View to display order status
def order_status(request, order_id):
    try:
        order = Order.objects.get(id=order_id)  # Fetch the specific order by ID
    except Order.DoesNotExist:
        return HttpResponse('Order not found', status=404)
    
    return render(request, 'order_status.html', {'order': order})

# View to display home page
def home(request):
    return render(request, 'home.html')

