from django.http import Http404, HttpResponse
from django.shortcuts import render_to_response
import datetime

# Local method
#def current_datetime(request):
#	current_date = datetime.datetime.now()
#	return render_to_response('current_datetime.html', locals())
# Older Method
#from django.template.loader import get_template 
#from django.template import Context
#def current_datetime(request):
#	now = datetime.datetime.now()
#	t = get_template('current_datetime.html')
#	html = t.render(Context({'current_date': now}))
#	return HttpResponse(html)
def current_datetime(request):
	now = datetime.datetime.now()
	return render_to_response('current_datetime.html', {'current_time': now})

def hours_ahead(request, offset):
	try:
		offset = int(offset)
	except ValueError:
		raise Http404
	dt = datetime.datetime.now() + datetime.timedelta(hours=offset)
#	It's a bad version
#	html = "<html><body>In %s hour(s), it will be %s.</body></html>" % (offset, dt)
	return render_to_response('hours_ahead.html', {'hour_offset': offset, 'next_time': dt})