from django.http import HttpResponse
from django.shortcuts import render

def home_page_view(request, *args, **kwargs):
    title = "Hello World"
    my_context = {
        "page_title": title
    }
    return HttpResponse(render(request, "home.html", my_context))

def old_home_page_view(request, *args, **kwargs):
    title = "Hello World"
    my_context = {
        "page_title": title
    }
    return HttpResponse("""<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="UTF-8">
    <title>{page_title}</title>
  </head>

  <body>
    <h1>{page_title}</h1>
    <p>Welcome to the {page_title} page.</p>
  </body>
</html>
""".format(**my_context))