from django.views import View
from django.shortcuts import render

class HomeView(View):
    template_name = 'login/base.html'
    def get(self, request):
        # <view logic>
         return render(request, self.template_name)


