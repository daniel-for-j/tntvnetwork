from django.core.paginator import Paginator
from django.shortcuts import render
from http.client import HTTPResponse
from django.contrib import messages
from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User, auth
from django.core.mail import send_mail
from django.conf import settings

# Create your views here.


def home(request):
    categories = Categories.objects.all()
    postSlider = Post.objects.all().order_by('-date')[:4]
    politicsLatestPost = Post.objects.filter(category__category_name="Politics").order_by('-date')[:1]
    politicsPosts = Post.objects.filter(category__category_name="Politics").order_by('-date')[:6]
    metroPosts = Post.objects.filter(category__category_name="Metro").order_by('-date')[:6]
    metroLatestPost = Post.objects.filter(category__category_name="Metro").order_by('-date')[:1]
    entertainmentLatestPost = Post.objects.filter(category__category_name="Entertainment").order_by('-date')[:1]
    entertainmentPosts = Post.objects.filter(category__category_name="Entertainment").order_by('-date')[:6]
    recentPosts = Post.objects.all().order_by('-date')[:4]
    return render(request, 'index.html',
                  {'categories': categories,
                   'slidePosts': postSlider, 
                   'politicsLatestPosts': politicsLatestPost, 
                   'politicsPosts': politicsPosts,
                   'metroPosts': metroPosts,
                   'metroLatestPosts': metroLatestPost, 
                   'entertainmentLatestPost': entertainmentLatestPost, 
                   'entertainmentPosts': entertainmentPosts,
                   'recentPosts':recentPosts
                   })
def category(request,category):
    categories = Categories.objects.all()
    recentPosts = Post.objects.all().order_by('-date')[:4]
    # Pagination 
    singleCategory =  Post.objects.filter(category__category_name=category).order_by('-date')[:1]
    categoryPosts = Post.objects.filter(category__category_name=category).order_by('-date')
    categoryPaginator = Paginator(categoryPosts,10)
    page = request.GET.get('page')
    categoryPage = categoryPaginator.get_page(page)
    return render(request, 'category.html', {
        'category': categoryPage,
        'categories': categories,
        'singleCategory':singleCategory,
        'recentPosts':recentPosts
    })

def singlePost(request,post_id):
    categories = Categories.objects.all()
    recentPosts = Post.objects.all().order_by('-date')[:4]
    post = Post.objects.get(id=post_id)
    return render(request, 'single-post.html',{
        'post':post,
        'categories': categories,
        'recentPosts':recentPosts

    })