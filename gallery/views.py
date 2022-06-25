from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from rest_framework.decorators import api_view
from rest_framework.response import Response

from .forms import ImageForm
from .models import PresentationCard
from .serializers import PresentationCardSerializer


def create_presentation_card(request):
    form = ImageForm()

    if request.method == "POST":
        form = ImageForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return render(request, "gallery/thanks.html")
    context = {"form": form}
    return render(request, "gallery/first.html", context)


@login_required(login_url="login")
def delete_presentation_card(request, pk):
    presentation_card = PresentationCard.objects.get(id=pk)

    if request.method == "POST":
        presentation_card.delete()
        return redirect("gallery")
    context = {"object": presentation_card}
    return render(request, "gallery/delete_presentation_card.html", context)


@login_required(login_url="login")
def update_presentation_card(request, pk):
    presentation_card = PresentationCard.objects.get(id=pk)
    form = ImageForm(instance=presentation_card)

    if request.method == "POST":
        form = ImageForm(request.POST, instance=presentation_card)
        if form.is_valid():
            form.save()
            return redirect("gallery")

    context = {"form": form}
    return render(request, "gallery/update_presentation_card.html", context)


@api_view(['GET'])
def show_cards_info(request):
    cards = PresentationCard.objects.all()
    page = request.GET.get("page")
    results = 6
    paginator = Paginator(cards, results)

    try:
        cards = paginator.page(page)
    except PageNotAnInteger:
        page = 1
        cards = paginator.page(page)
    except EmptyPage:
        page = paginator.num_pages
        cards = paginator.page(page)

    serializer = PresentationCardSerializer(cards, many=True)
    return Response(serializer.data)


def show_cards(request):
    return render(request, "gallery/gallery.html")


@api_view(['GET'])
def show_card_info(request, pk):
    card = PresentationCard.objects.get(id=pk)
    serializer = PresentationCardSerializer(card, many=False)
    return Response(serializer.data)


def show_card(request, pk):
    return render(request, "gallery/presentation_card.html")
