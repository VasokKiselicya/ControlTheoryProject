from django.shortcuts import render


def handle_not_found_404(request, **kwargs):
    return render(request, "errors/404_not_found.html", content_type='text/html; charset=utf-8', status=404)
