from django.contrib import auth, messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import AuthenticationForm, PasswordChangeForm
from django.http import HttpRequest, HttpResponse
from django.shortcuts import redirect, render
from django.views.decorators.http import require_GET, require_http_methods

from users.forms import UserCreation


@require_http_methods(["GET", "POST"])
def create(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = UserCreation(request.POST)

        if form.is_valid():
            form.save()
            messages.success(request, "Usuário criado com sucesso!")
            return redirect("users:login")

        messages.error(request, "Erro ao criar usuário.")
        return render(request, "users/create.html", {"form": form})

    form = UserCreation()

    return render(request, "users/create.html", {"form": form})


@require_http_methods(["GET", "POST"])
def login(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)

        if form.is_valid():
            username = form.get_user()
            auth.login(request, username)
            return redirect("home")

        return render(request, "users/login.html", {"form": form})

    form = AuthenticationForm()

    return render(request, "users/login.html", {"form": form})


@login_required
@require_http_methods(["GET", "POST"])
def logout(request: HttpRequest) -> HttpResponse:
    auth.logout(request)
    return redirect("home")


@login_required
@require_http_methods(["GET", "POST"])
def update(request: HttpRequest) -> HttpResponse:
    if request.method == "POST":
        form = PasswordChangeForm(request.user, request.POST)

        if form.is_valid():
            form.save()
            auth.update_session_auth_hash(request, form.user)
            request.session["came_from_update"] = True
            return redirect("users:success")

        return render(request, "users/update.html", {"form": form})

    form = PasswordChangeForm(request.user)

    return render(request, "users/update.html", {"form": form})


@login_required
@require_GET
def success(request: HttpRequest) -> HttpResponse:
    if request.session.pop("came_from_update", False):
        return render(request, "users/success.html")

    return redirect("home")
