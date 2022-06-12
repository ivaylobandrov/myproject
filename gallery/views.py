from django.shortcuts import render, redirect
from django.core.paginator import Paginator, PageNotAnInteger, EmptyPage
from django.contrib.auth.decorators import login_required
from rest_framework.permissions import AllowAny
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.views import APIView

from .forms import ImageForm
from .models import PresentationCard


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


class PresentationCardsView(APIView):
    permission_classes = (AllowAny,)
    renderer_classes = [TemplateHTMLRenderer]
    template_name = "gallery/gallery.html"

    def get(self, request, *args, **kwargs):
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
        context = {"cards": cards, "paginator": paginator}
        return render(request, self.template_name, context)


class ShowPresentationCardInfoView(APIView):
    def get(self, request, pk):
        card = PresentationCard.objects.get(id=pk)
        context = {"presentation_card": card}
        return render(request, "gallery/presentation_card.html", context)
