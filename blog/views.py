from django.shortcuts import render
from django.utils import timezone
from .models import Post
from django.shortcuts import render, get_object_or_404
from .forms import PostForm
from django.shortcuts import redirect
<<<<<<< HEAD
from django.shortcuts import render
from .models import Rating
from django.http import JsonResponse
=======
>>>>>>> 9502574 (retake)
def post_list(request):
    posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('published_date')
    return render(request, 'blog/post_list.html', {'posts': posts})
def post_detail(request, pk):
    post = get_object_or_404(Post, pk=pk)
    return render(request, 'blog/post_detail.html', {'post': post})
def post_new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/post_edit.html', {'form': form})
def post_edit(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('post_detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/post_edit.html', {'form': form})
def post_remove(request, pk):
    post = get_object_or_404(Post, pk=pk)
    post.delete()
<<<<<<< HEAD
    return redirect('post_list')   
def main_view(request):
    obj = Rating.objects.filter(score=0).order_by("?").first()
    context ={
        'object': obj
    }
    return render(request, 'ratings/main.html', context)


def rate_image(request):
    if request.method == 'POST':
        el_id = request.POST.get('el_id')
        val = request.POST.get('val')
        print(val)
        obj = Rating.objects.get(id=el_id)
        obj.score = val
        obj.save()
        return JsonResponse({'success':'true', 'score': val}, safe=False)
    return JsonResponse({'success':'false'}) 
=======
    return redirect('post_list')
>>>>>>> 9502574 (retake)
