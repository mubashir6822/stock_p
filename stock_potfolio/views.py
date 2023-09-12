from django.shortcuts import render, get_object_or_404, redirect
from .models import Stock
from .forms import StockForm,StockStatus, News, Holding

def home(request):
    return render(request, 'portfolio/home.html')

def stock_list(request):
    stocks = Stock.objects.all()
    stock_statuses = StockStatus.objects.all()
    news = News.objects.all()
    holdings = Holding.objects.all()

    context = {
        'stocks': stocks,
        'stock_statuses': stock_statuses,
        'news': news,
        'holdings': holdings,
    }

    return render(request, 'portfolio/stock_list.html', context)

def stock_detail(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    return render(request, 'portfolio/stock_detail.html', {'stock': stock})

def stock_create(request):
    if request.method == 'POST':
        form = StockForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm()
    return render(request, 'portfolio/stock_create.html', {'form': form})

def stock_update(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        form = StockForm(request.POST, instance=stock)
        if form.is_valid():
            form.save()
            return redirect('stock_list')
    else:
        form = StockForm(instance=stock)
    return render(request, 'portfolio/stock_update.html', {'form': form, 'stock': stock})


def stock_delete(request, stock_id):
    stock = get_object_or_404(Stock, pk=stock_id)
    if request.method == 'POST':
        stock.delete()
        return redirect('stock_list')
    return render(request, 'portfolio/stock_confirm_delete.html', {'stock': stock})