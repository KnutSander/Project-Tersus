from django.http import HttpResponse
from CC.models import RiskGroup


def showRiskGroups(request):
	all_groups = RiskGroup.objects.all().values('name')
	return HttpResponse(all_groups)
