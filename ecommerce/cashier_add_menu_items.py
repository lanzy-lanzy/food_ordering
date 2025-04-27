from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required, permission_required
from .models import Reservation, MenuItem
from .forms import AddMenuItemsToReservationForm

@login_required
@permission_required('ecommerce.change_reservation', raise_exception=True)
def cashier_add_menu_items_to_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, id=reservation_id)

    if request.method == 'POST':
        form = AddMenuItemsToReservationForm(request.POST)
        if form.is_valid():
            menu_items = form.cleaned_data['menu_items']
            for item in menu_items:
                reservation.menu_items.add(item)
            reservation.save()
            messages.success(request, 'Menu items added to reservation successfully!')
            return redirect('cashier_reservations_list')
    else:
        form = AddMenuItemsToReservationForm()

    return render(request, 'cashier/add_menu_items_to_reservation.html', {
        'reservation': reservation,
        'form': form
    })
