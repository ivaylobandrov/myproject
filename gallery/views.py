from django.contrib.auth.decorators import login_required
from django.shortcuts import redirect, render
from rest_framework.decorators import api_view, permission_classes
from rest_framework.pagination import PageNumberPagination
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from gallery.filters import CardFilter
from gallery.forms import ImageForm
from gallery.models import PresentationCard
from gallery.serializers import PresentationCardSerializer


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


@permission_classes([AllowAny])
@api_view(["GET"])
def show_cards_info(request):
    paginator = PageNumberPagination()
    paginator.page_size = 6
    cards = PresentationCard.objects.all()
    filterset = CardFilter(request.GET, queryset=cards)
    if filterset.is_valid():
        cards = filterset.qs
    result_page = paginator.paginate_queryset(cards, request)

    serializer = PresentationCardSerializer(result_page, many=True)
    return paginator.get_paginated_response(serializer.data)


def show_cards(request):
    return render(request, "gallery/gallery.html")


@api_view(["GET"])
def show_card_info(request, pk):
    card = PresentationCard.objects.get(id=pk)
    serializer = PresentationCardSerializer(card, many=False)
    return Response(serializer.data)


def show_card(request, pk):
    return render(request, "gallery/presentation_card.html")
