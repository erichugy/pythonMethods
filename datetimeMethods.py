import datetime as dt

def is_weekday(date:dt.datetime):
  """
    Returns whether the given date is a weekday or a weekend.
    dt.datetime.weekday() returns a number 0-6 where 0 is monday and 6 is sunday.
  """
  return date.weekday() < 5
  
def next_workday_8am():
  """Returns the next workday at 8am as a datetime object.

  A workday is defined as any day from Monday through Friday. If the current time is before 8am on a workday,
  the function will return 8am of the current day. Otherwise, it will return the next workday at 8am.
  """
  now = datetime.datetime.now()

  # If it is before 8am on a workday, return 8am of the current day
  if now.hour < 8 and now.weekday() in range(0, 5):
      return now.replace(hour=8, minute=0, second=0, microsecond=0)

  # Otherwise, find the next workday at 8am
  days_ahead = 1
  while True:
      next_day = now + datetime.timedelta(days=days_ahead)
      if next_day.weekday() in range(0, 5):  # weekday() returns 0 for Monday, 1 for Tuesday, etc.
          return next_day.replace(hour=8, minute=0, second=0, microsecond=0)
      days_ahead += 1
  
