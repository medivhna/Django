from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

# Older Method
#from django.template.loader import get_template 
#from django.template import Context
#def current_datetime(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_date': now}))
#	return HttpResponse(html)

def current_date(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_date': now})
def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return HttpResponse(html)