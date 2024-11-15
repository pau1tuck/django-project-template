# apps/public/views/main_content_view.py
import logging
from typing import Any, Dict

from django.shortcuts import render as django_render
from django.views import View
from django_htmx import http as htmx


class MainContentView(View):
    url: str = ""
    context: Dict = {}

    def __init__(self, **kwargs):
        super().__init__(**kwargs)

        if not hasattr(self, "template_name"):
            cls_name_str = self.__class__.__name__.lower()
            self.template_name = f"{cls_name_str}/{cls_name_str}.html"

    def get(self, request, *args, **kwargs):
        logging.warning("GET method not implemented.")
        if self.template_name:
            logging.warning("Will attempt to render template as-is.")
            return self.render()
        raise NotImplementedError

    def post(self, request, *args, **kwargs):
        raise NotImplementedError

    def dispatch(self, request, *args, **kwargs):
        if request.htmx:
            if request.GET.get("hx-get", "") == "page":
                self.context["base_template"] = "_base.html"
            else:
                self.context["base_template"] = "_partial.html"
        else:
            self.context["base_template"] = "_base.html"
        return super().dispatch(request, *args, **kwargs)

    def render(
        self,
        request: Any = None,
        template_name: str = None,
        context: Dict = None,
        push_url=None,
    ):
        request = request or self.request
        template_name = template_name or self.template_name
        context = context or self.context

        response = django_render(request, template_name, context)

        if push_url:
            response = htmx.push_url(response, url=push_url)

        # if request.htmx and self.url:
        #     ic("using push_url with", self.url)
        #     return push_url(response, self.url)

        return response
