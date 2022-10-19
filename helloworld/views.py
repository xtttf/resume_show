from django.shortcuts import render

def runoob(request):
    name = "个人简历"
    return render(request, "runoob.html", {"name": name})