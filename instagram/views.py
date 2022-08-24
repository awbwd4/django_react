from django.views.generic import ListView
from django.shortcuts import render
from django.http import HttpRequest, HttpResponse
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


def post_detail(request: HttpRequest, pk: int) -> HttpResponse:
    response = HttpResponse()
    response.write("hello world")
    response.write("hello world")
    response.write("hello world")
    response.write("hello world")
    return response


def archives_year(request: HttpRequest, year: int) -> HttpResponse:
    return HttpResponse(f"{year}년 archives")
