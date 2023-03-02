from django.http import HttpResponse,HttpResponseRedirect
from django.shortcuts import render
from .forms import usersForm
#imort your model here first
from category.models import category
from news.models import News
from product.models import Product
from contactme.models import contactme
from django.core.paginator import Paginator
from django.core.mail import send_mail
from django.core.mail import EmailMultiAlternatives