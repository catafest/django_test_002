from datetime import datetime, timedelta
from calendar import HTMLCalendar
from .models import Event

class Calendar(HTMLCalendar):
	def __init__(self, year=None, month=None):
		self.year = year
		self.month = month
		super(Calendar, self).__init__()

	def formatday(self, day, events):
		events_per_day = events.filter(start_time__day=day)
		day_event = ''
		for event in events_per_day:
			day_event += f'<li> {event.title} </li>'

		if day != 0:
			return f"<td><span class='date'>{day}</span><ul> {day_event} </ul></td>"
		return '<td></td>'

	# formats a week as a tr 
	def formatweek(self, theweek, events):
		week = ''
		for day_event, weekday in theweek:
			week += self.formatday(day_event, events)
		return f'<tr> {week} </tr>'

	# formats a month as a table
	# filter events by year and month
	def formatmonth(self, withyear=True):
		events = Event.objects.filter(start_time__year=self.year, start_time__month=self.month)

		my_calendar = f'<table border="0" cellpadding="0" cellspacing="0" class="calendar">\n'
		my_calendar += f'{self.formatmonthname(self.year, self.month, withyear=withyear)}\n'
		my_calendar += f'{self.formatweekheader()}\n'
		for week in self.monthdays2calendar(self.year, self.month):
			my_calendar += f'{self.formatweek(week, events)}\n'
		return my_calendar