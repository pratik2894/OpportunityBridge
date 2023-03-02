from django.http import HttpResponse
from django.shortcuts import render,redirect
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib import messages
from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate,login,logout