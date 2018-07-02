from django.shortcuts import render
from .models import *
from .forms import *
from django.http import *
from django.contrib import messages


def contact(request):
    if request.method == 'POST':

        form = details_form(request.POST)
        if form.is_valid():
            form.save()
            form = details_form()
            messages.success(request, 'Details Sent Successfully')
        return render(request, 'contact.html', {'form': form})

    else:
        form = details_form()
        return render(request, 'contact.html', {'form': form})






# def contact(request):
# 	if request.method == 'POST':
#
# 		form = details_form(request.POST)
#
	# 	name = request.POST.get('name', '')
	# 	emailid = request.POST.get('emailid', '')
	# 	phone = request.POST.get('phone', '')
	# 	message = request.POST.get('message', '')
	# 	details_obj = user(name = name, emailid = emailid, phone = phone, message = message)
	# 	details_obj.save()
	# 	form = details_form()
    #
    #
    #
	# else:
	# 	form = details_form()
	# return render(request,'data.html',{'form':form})

