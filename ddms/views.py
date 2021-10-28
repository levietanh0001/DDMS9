from django.shortcuts import render
from django.contrib.auth.decorators import login_required

from drugs.views import Drug

@login_required(login_url='login')
def dashboard(request):
    # total_product = Product.objects.count()
    # total_supplier = Supplier.objects.count()
    # total_buyer = Buyer.objects.count()
    # total_oder = Order.objects.count()
    # orders = Order.objects.all().order_by('-id')
    drug_count = Drug.objects.all().count()
    context = {
        'drug_count': drug_count
        # 'product': total_product,
        # 'supplier': total_supplier,
        # 'buyer': total_buyer,
        # 'order': total_oder,
        # 'orders': orders
    }
    return render(request, 'dashboard.html', context)


def base(request):
    context = {}
        # main dir: templates
    return render(request, 'base/base.html', context)


def store_dashboard(request):
    context = {}
        # main dir: templates
    return render(request, 'oscar/dashboard/base.html', context)


def store_catalogue(request):
        # main dir: templates
    return render(request, 'oscar/base.html')