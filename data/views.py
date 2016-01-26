from django.views import generic
from django.contrib.auth import authenticate
from django.http import HttpResponse

from .models import Payment


class IndexView(generic.ListView):
	template_name = 'data/index.html'
	context_object_name = 'payments_list'

	def get_queryset(self):
		return Payment.objects.order_by('-created_at')[:5]


def login(request):
	user = authenticate(username='priveras', password='scoobydoo')
	if user is not None:

		if user.is_active:
			 login(request, user)
		else:
			 return HttpResponse("User is not valid")

	else:
		 return HttpResponse("That user doesn't exist")
		

def profile(request):
	return HttpResponse("Hello motherfucker")