from django.shortcuts import render
from .models import Post


def post_list(request):
    qs = Post.objects.all()
    query = request.GET.get('query', '')
    if query:
        qs = qs.filter(message__icontains=query)
    # instagram/templates/instagram/post_list.html
    return render(request, 'instagram/post_list.html', {
        'post_list': qs,
        'query': query
    })
