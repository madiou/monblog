# blog/views.py
from django.core.paginator import Paginator  # Ajoute cette ligne
from django.shortcuts import render, get_object_or_404
from .models import Post, Comment, Category
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required

def home(request):
    query = request.GET.get('q')
    if query:
        posts = Post.objects.filter(title__icontains=query)
    else:
        posts = Post.objects.all()
    paginator = Paginator(posts, 5)  # 5 articles par page
    page_number = request.GET.get('page')
    posts = paginator.get_page(page_number)
    categories = Category.objects.all()
    return render(request, 'blog/home.html', {'posts': posts, 'categories': categories})

def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.filter(approved=True)
    return render(request, 'blog/post_detail.html', {'post': post, 'comments': comments})

@login_required
def add_comment(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == 'POST':
        body = request.POST.get('body')
        comment = Comment.objects.create(
            post=post,
            name=request.user.username,
            email=request.user.email,
            body=body
        )
        return HttpResponseRedirect(reverse('post_detail', args=[str(pk)]))
    return render(request, 'blog/add_comment.html')

@login_required
def add_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        date_posted = request.POST.get('date_posted', None)
        post = Post.objects.create(
            title=title, 
            content=content, 
            author=request.user, 
            date_posted=date_posted if date_posted else datetime.now()
        )
        # Envoie d'un email de notification
        send_notification_email(
            'Nouvel article à approuver',
            f'L\'article "{post.title}" a été ajouté et nécessite une approbation.',
            ['admin@example.com']  # Liste des emails des administrateurs
        )
        return HttpResponseRedirect(reverse('home'))
    return render(request, 'blog/add_post.html')
