import base64
from django.shortcuts import render
from django.http import HttpResponse
picture_path = "/root/picture/{}"
pdf_path = "/root/pdf/{}"


def runoob(request):
    name = "个人简历"
    return render(request, "runoob.html", {"name": name})


def get_picture(request):
    picture_name = request.GET.get("picture_name", '')
    f = open(picture_path.format(picture_name), "rb")
    picture = f.read()
    # data = base64.b64encode(picture)
    data = picture
    resp = HttpResponse(content=data, content_type="image/png")
    return resp



def get_pdf(request):
    pdf_name = request.GET.get("pdf_name", '')
    f = open(pdf_path.format(pdf_name), "rb")
    data = f.read()
    resp = HttpResponse(content=data, content_type="application/pdf")
    return resp
