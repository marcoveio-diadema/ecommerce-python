from django.shortcuts import render

# summary
def cart_summary(request):
    context = {

    }
    return render(request, "cart/cart_summary.html", context)

# add
def cart_add(request):
    context = {
        
    }
    return render(request, "cart/cart_add.html", context)

# delete
def cart_delete(request):
    context = {
        
    }
    return render(request, "cart/cart_delete.html", context)

# update
def cart_update(request):
    context = {
        
    }
    return render(request, "cart/cart_update.html", context)