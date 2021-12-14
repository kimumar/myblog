from django.shortcuts import render, redirect, get_object_or_404
from .models import Post, PostForm, CommentMessage, CommentForm, Sub, SubForm
from django.contrib import messages
from user.decorators import unauthenticated_user, allowed_users
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from django.conf import settings
from django.core.paginator import Paginator

# Create your views here.

def index(request):
    if request.method == 'POST':
        form = SubForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Thanks! You have successfully subscribed to our newsletter..")
            return redirect('/')

    form = SubForm
    posts = Post.objects.all()

    p = Paginator(Post.objects.all(), 5)
    page = request.GET.get('page')
    pag = p.get_page(page)

    context = {
        'posts':posts,
        'pag': pag,
        'form': form,
    }
    return render(request, 'index.html', context)

def blogs(request, pk):
    post = get_object_or_404(Post, id=pk)
    comments = post.comments.filter(active=True)
    comment = None
    # Comment posted
    if request.method == 'POST':
        comment= CommentForm(data=request.POST)
        if comment.is_valid():

            # Create Comment object but don't save to database yet
            comment = comment.save(commit=False)
            # Assign the current post to the comment
            comment.post = post
            # Save the comment to the database
            comment.save()
    else:
        comment = CommentForm()


    context = {
        'post':post,
        'comments':comments,
        'comment':comment,
    }

    return render(request, 'blog_details.html', context)

# @login_required
# @allowed_users(allowed_roles=['admin'])
# def updates(request, pk):
#     blogs = CommentMessage.objects.get(id=pk)
#     comment = CommentForm(instance=blogs)

#     if request.method == 'POST':
#         comment = CommentForm(request.POST, instance=blogs)
#         if comment.is_valid():
#            comment.save
#         return redirect('/')
        

#     context = {
#         'comment':comment,
        
#     }
#     return render(request, 'comment-update.html', context)

# @login_required
# @allowed_users(allowed_roles=['admin'])
# def deleteco(request, pk):
#     comments = CommentMessage.objects.get(id=pk)

#     if request.method == "POST":
#         comments.delete()
#         return redirect('/')


#     context = {
#         'comments':comments,
#     }

#     return render(request, 'comment-delete.html', context)

@login_required
def about(request):
    return render(request, 'about.html')

@login_required
def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        

        send_mail(
            name,
            message,
            'kimumar55@gmail.com',
            ['oladeleumaradisa19@gmail.com'],
            fail_silently=False)
    
    return render(request, 'contact.html')

@login_required
@allowed_users(allowed_roles=['admin'])
def create(request):
    post = PostForm()
    if request.method == 'POST':
        post = PostForm(request.POST, request.FILES)
        if post.is_valid():
            post.save()
        return redirect('index')

    context = {
        'post':post,
    }
    return render(request, 'create.html', context)

# @login_required
# @allowed_users(allowed_roles=['admin'])
# def update(request, pk):
#     blog = Post.objects.get(id=pk)
#     post = PostForm(instance=blog)

#     if request.method == 'POST':
#         post = PostForm(request.POST, instance=blog)
#         if post.is_valid():
#             post.save
#         return redirect('index')
        
#     context = {
#         'post':post,
        
#     }
#     return render(request, 'create.html', context)

# @login_required
# @allowed_users(allowed_roles=['admin'])
# def delete(request, pk):
#     post = Post.objects.get(id=pk)

#     if request.method == "POST":
#         post.delete()
#         return redirect('index')


#     context = {
#         'post':post,
#     }

#     return render(request, 'confirm_delete.html', context)