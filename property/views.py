from django.http import HttpResponseRedirect
from django.shortcuts import redirect, render
from .models import Tombstone, User, Comment
from .forms import AddTombstone, AddComment
from django.contrib.auth import logout
from django.contrib.auth.decorators import login_required
from datetime import datetime
from django.contrib import messages


# Create your views here.
def home_screen_view(request, *args, **kwargs):
    all_tombstones = Tombstone.objects.all()
    context = {"tombstones": all_tombstones}
    return render(
        request,
        "property/home.html",
        context,
    )


def authorization_screen_view(request, *args, **kwargs):
    return render(
        request,
        "property/authorization.html",
    )


def logout_view(request):
    logout(request)
    return redirect(
        "home",
    )


@login_required(login_url="/authorization/")
def add_tomb_screen_view(request, *args, **kwargs):
    if request.method == "POST":
        form = AddTombstone(request.POST, request.FILES)
        if form.is_valid():
            user = request.user
            company_name = request.POST.get("company_name")
            birth_year = request.POST.get("birth_year")
            death_year = request.POST.get("death_year")
            alternate_name = request.POST.get("alternate_name")
            people = request.POST.get("people")
            link = request.POST.get("link")
            characteristic = request.POST.get("characteristic")
            description = request.POST.get("description")
            death_cause = request.POST.get("death_cause")
            count_employee = request.POST.get("count_employee")
            revenue = request.POST.get("revenue")
            score_company = request.POST.get("score_company")
            tombstone = Tombstone(
                user_id=user,
                create_date=datetime.now(),
                company_name=company_name,
                logo=form.cleaned_data["logo"],
                birth_year=birth_year,
                death_year=death_year,
                alternate_name=alternate_name,
                people=people,
                link=link,
                characteristic=characteristic,
                description=description,
                death_cause=death_cause,
                count_employee=count_employee,
                revenue=revenue,
                score_company=score_company,
            )
            tombstone.save()
            return redirect("home")
    else:
        form = AddTombstone()
    data = {
        "form": form,
    }
    return render(
        request,
        "property/add_tomb.html",
        data,
    )


def searched_tomb_screen_view(request, *args, **kwargs):
    if request.method == "POST":
        searched = request.POST["searched"]
        searched_tombstones = Tombstone.objects.filter(company_name__icontains=searched)
        context = {
            "searched": searched,
            "searched_tombstones": searched_tombstones,
        }
        return render(
            request,
            "property/searched_tomb.html",
            context,
        )
    else:
        return render(request, "property/searched_tomb.html")


def new_tomb_screen_view(request, *args, **kwargs):
    new_tombstones = Tombstone.objects.all().order_by("-birth_year")
    context = {
        "new_tombstones": new_tombstones,
    }
    return render(
        request,
        "property/new_tomb.html",
        context,
    )


def old_tomb_screen_view(request, *args, **kwargs):
    old_tombstones = Tombstone.objects.all().order_by("birth_year")
    context = {
        "old_tombstones": old_tombstones,
    }
    return render(
        request,
        "property/old_tomb.html",
        context,
    )


def new_add_tomb_screen_view(request, *args, **kwargs):
    new_add_tombstones = Tombstone.objects.order_by("-create_date")
    context = {
        "new_add_tombstones": new_add_tombstones,
    }
    return render(
        request,
        "property/new_add_tomb.html",
        context,
    )


def old_add_tomb_screen_view(request, *args, **kwargs):
    old_add_tombstones = Tombstone.objects.order_by("create_date")
    context = {
        "old_add_tombstones": old_add_tombstones,
    }
    return render(
        request,
        "property/old_add_tomb.html",
        context,
    )

@login_required(login_url="/authorization/")
def tombstone_screen_view(request, tombstone_id):    
    tombstone = Tombstone.objects.get(tombstone_id=tombstone_id)
    comments = Comment.objects.filter(tombstone_id=tombstone)  
    user = User.objects.all()
    request_user = User.objects.get(user=request.user)

    if request.method == "POST":
        form = AddComment(request.POST)
        if form.is_valid():
            comment = request.POST.get("comment")
            created_at = datetime.now()
            user = request_user
            comment = Comment(
                comment=comment,
                created_at=created_at,
                user=user,
                tombstone=tombstone,
            )
            comment.save()
            messages.success(request, "Ваш комментарий успешно отправлен!")
            return HttpResponseRedirect(request.path)
    else:
        form = AddComment()

    context = {
        "tombstone": tombstone,
        "form": form,
        "user": user,
        "comments": comments,
    }
    return render(
        request,
        "property/tombstone.html",
        context,
    )


def profile_screen_view(request, user_id):
    user = request.user
    social_auth = User.objects.get(id=user.id)
    user_tombstones = Tombstone.objects.filter(user_id=user)
    context = {
        "user": social_auth,
        "user_tombstones": user_tombstones,
    }
    return render(request, "property/profile.html", context)
