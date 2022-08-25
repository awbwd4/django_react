from django.views.generic import ListView, DetailView
from django.shortcuts import get_object_or_404, render
from django.http import HttpRequest, HttpResponse, Http404
from .models import Post


post_list = ListView.as_view(model=Post)


# def post_list(request: HttpResponse):
#     qs = Post.objects.all()
#     query = request.GET.get('query', '')
#     if query:
#         qs = qs.filter(message__icontains=query)
#     # instagram/templates/instagram/post_list.html
#     return render(request, 'instagram/post_list.html', {
#         'post_list': qs,
#         'query': query
#     })


# def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
#     post = get_object_or_404(Post, pk=pk)

#     # try:
#     #     post = Post.objects.get(pk=pk)
#     # except Post.DoesNotExist:
#     #     raise Http404

#     return render(request, 'instagram/post_detail.html', {
#         'post': post
#     })


post_detail  = DetailView.as_view(model=Post)



def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f"{year}년 archives")
