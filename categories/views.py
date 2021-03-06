from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required

from .models import Category, SubCategory
from pages.decorators import allowed_users


@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer', 'logassistant'])
def view_categories(request):
    queryset = SubCategory.objects.all().order_by('category')
    context = {
        "object_list": queryset
    }
    return render(request, "view_categories.html", context)

# Category Views
@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def cat_create(request):
    if request.method == "POST":
        c_name = request.POST.get('name')
        new = Category.objects.create(name=c_name)

        return redirect("/categories/", {})

    return render(request, "create_cat.html", {})
@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def cat_update(request, id):
    if request.method == "GET":
        obj = get_object_or_404(Category, id=id)
        context = {
            "object": obj
        }
        return render(request, "update_cat.html", context)

    if request.method == "POST":
        obj2 = get_object_or_404(Category, id=id)

        obj2.name = request.POST.get('name')
        obj2.save()

        return redirect("/categories/", {})


@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def subcat_create(request):
    if request.method == "GET":
        queryset = Category.objects.all()
        context = {
            "object_list": queryset
        }
        return render(request, "create_subcat.html", context)
    if request.method == "POST":
        c_name = request.POST.get('name')
        c_depreciation = request.POST.get('depreciation')

        data = request.POST.get('category')
        c_category = Category.objects.get(id=data)
        print(request.POST)

        new = SubCategory.objects.create(name=c_name, category= c_category, depreciation_length=c_depreciation)

        return redirect("/categories/", {})


@login_required(login_url='login')
@allowed_users(allowed_roles=['logco', 'logmanager', 'logofficer'])
def subcat_update(request, id):
    if request.method == "GET":
        obj = get_object_or_404(SubCategory, id=id)
        queryset = Category.objects.all()
        context = {
            "object": obj,
            "object-list": queryset
        }
        return render(request, "update_subcat.html", context)

    if request.method == "POST":
        obj2 = get_object_or_404(SubCategory, id=id)

        obj2.name = request.POST.get('name')
        obj2.depraciation_length = request.POST.get('depreciation')

        data = request.POST.get('category')
        obj.category = Category.objects.get(id=data)
        obj2.save()

        return redirect("/categories/", {})



@login_required(login_url='login')
@allowed_users(allowed_roles=['logco'])
def subcat_delete(request, custodian_id):
    obj = get_object_or_404(Category, id=custodian_id)
    obj.delete()

    return redirect("/custodians/", {})