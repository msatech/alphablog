from django.shortcuts import render,redirect
from .models import *
from django.http import HttpResponse
import json
from alphablog.settings import BASE_URL
from django.contrib.auth.decorators import login_required

from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
# Create your views here.
def Blog(request):
    if request.method == "POST":
        b = request.POST.get('term')
        blog = Blogs.objects.filter(title__icontains=b)
        
    else:
        blog = Blogs.objects.all()
    category = Category.objects.all()
    color = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'default']
    latestblogs = Blogs.objects.all()[:6]
    recentarticle = Blogs.objects.all()[:8]
    newarticle = Blogs.objects.order_by('-id')[:1]

    blog = Paginator(blog, 9)
    page = request.GET.get('page')
    try:
        blog = blog.page(page)
    except PageNotAnInteger:
        blog = blog.page(1)
    except EmptyPage:
        blog = blog.page(blog.num_pages)

    
    return render(request, 'main.html',{
        'categoryList': category,
        'blogs': blog,
        'colors': color,
        'latestblogs': latestblogs,
        'recentarticle':recentarticle,
        'newarticle':newarticle,
    })

from django.http import JsonResponse

def Autocomplete(request):
        if 'term' in request.GET:
            qs = Blogs.objects.filter(title__icontains=request.GET.get('term'))
            titles = list()
            for blog in qs:
                titles.append(blog.title)
            return JsonResponse(titles, safe=False)
        return render(request, 'main.html')


def Single_Post(request, slug):
    blog = Blogs.objects.get(slug=slug)
    category = Category.objects.all()
    color = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'default']
    latestblogs = Blogs.objects.all()[:6]
    recentarticle = Blogs.objects.all()[:6]
    comments = Comments.objects.filter(blog__slug = slug)
    totalcomment = Comments.objects.filter(blog__slug = slug).count()
    replycomments = CommentReply.objects.filter(blog__slug = slug)
    replycommentcount = CommentReply.objects.filter(blog__slug = slug).count()
    keywords = Keywords.objects.filter(blog=blog)
    totalcomments = totalcomment + replycommentcount
    
    return render(request, 'singleblog.html',{
        'categoryList': category,
        'blog': blog,
        'colors': color,
        'latestblogs': latestblogs,
        'recentarticle':recentarticle,
        'comments': comments,
        'replycomments':replycomments,
        'totalcomments':totalcomments,
        'keywords':keywords,
        'title': blog.title,
        'description':blog.metaDescription,

    })

def CommentSave(request, slug):
    if request.method == "POST":
        commentcontent = request.POST.get('comment')
        name = request.POST.get('name')
        email = request.POST.get('email')
        blog = Blogs.objects.get(slug=slug)
        user = User.objects.get(username=name)
        Comments.objects.create(blog=blog, user=user, comment=commentcontent, email=email)
    return redirect(BASE_URL + 'single-post/'+ str(slug))

def CommentDelete(request, slug, id):
    
    comment = Comments.objects.get(pk=id)
    comment.delete()
    return redirect(BASE_URL + 'single-post/'+ str(slug))

def ReplyComment(request, slug, user, id):
    if request.method == "POST":
        replycomment = request.POST.get('reply')
        previouscomment = Comments.objects.get(pk=id)
        userdata = User.objects.get(username=user)
        blog = Blogs.objects.get(slug=slug)
        CommentReply.objects.create(previouscomment=previouscomment, blog=blog, replycomment=replycomment, user=userdata )
        
    return redirect(BASE_URL + 'single-post/'+ str(slug))

def ReplyCommentDelete(request, slug, id):
    
    replycomment = CommentReply.objects.get(pk=id)
    replycomment.delete()
    return redirect(BASE_URL + 'single-post/'+ str(slug))

def CategoryWiseBlog(request, blogcategory):
    
    ncategory = Category.objects.get(title = blogcategory)
    print(ncategory)
    blog = Blogs.objects.filter(category=ncategory)
    print(blog)
    category = Category.objects.all()
    color = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'default']
    latestblogs = Blogs.objects.all()[:6]
    recentarticle = Blogs.objects.all()[:8]
    return render(request, 'main.html',{
        'categoryList': category,
        'blogs': blog,
        'colors': color,
        'latestblogs': latestblogs,
        'recentarticle':recentarticle,
    })

def NewHome(request):
    if request.method == "POST":
        b = request.POST.get('term')
        blog = Blogs.objects.filter(title__icontains=b)
        
    else:
        blog = Blogs.objects.order_by('?').all()
    category = Category.objects.all()
    color = ['primary', 'secondary', 'success', 'danger', 'warning', 'info', 'light', 'dark', 'default']
    latestblogs = Blogs.objects.all()[:6]
    recentarticle = Blogs.objects.all()[:8]
    newarticle = Blogs.objects.order_by('-id')[:1]
    firstblog = Blogs.objects.order_by('?').first()
    secondblog = Blogs.objects.order_by('?').first()
    random_category = Category.objects.order_by('?').first()
    random_blog = Blogs.objects.filter(category=random_category)
    random_comment = Comments.objects.order_by("?").first()
    blog = Paginator(blog, 9)
    page = request.GET.get('page')
    try:
        blog = blog.page(page)
    except PageNotAnInteger:
        blog = blog.page(1)
    except EmptyPage:
        blog = blog.page(blog.num_pages)

    
    return render(request, 'newhome.html',{
        'categoryList': category,
        'blogs': blog,
        'colors': color,
        'latestblogs': latestblogs,
        'recentarticle':recentarticle,
        'newarticle':newarticle,
        'firstblog': firstblog,
        'secondblog': secondblog,
        'random_blogs':random_blog,
        'random_comment': random_comment,
    })