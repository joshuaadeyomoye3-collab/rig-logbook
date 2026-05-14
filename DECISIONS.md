# DECISIONS.md — Rig Logbook

## 1. Why I used CharField with choices for shift_type instead of BooleanField
I could have used a boolean (is_day_shift: True/False) but I used a CharField 
with choices ('day'/'night') because it is more readable in the admin panel and 
easier to extend if we ever add a third shift type like 'standby'. A boolean 
would require a migration just to add a third option.

## 2. Why I used get_object_or_404 instead of .get()
Using .get() would raise an unhandled DoesNotExist exception if someone visits 
/log/999/ and that ID doesn't exist. get_object_or_404 returns a proper 404 
page instead — better user experience and safer for production.

## 3. Why I used TextField for incidents and equipment_status instead of CharField
CharField has a maximum length limit and is designed for short text. Incident 
descriptions and equipment status reports can be long and unpredictable in 
length, so TextField is the right choice — it has no length cap.

## 4. Why I made incidents and equipment_status optional (blank=True)
Not every shift has an incident or something notable about equipment. Forcing 
engineers to fill those fields when there is nothing to report would create 
noise in the data — entries like "N/A" or "none". blank=True means the field 
is only filled when there is something real to say.

## 5. Why I used a separate app-level urls.py instead of putting all URLs in rigproject/urls.py
Putting all URLs directly in the project-level urls.py works but does not scale. 
If a second app is added later, the URL file becomes messy. Keeping logbook URLs 
inside logbook/urls.py means each app owns its own routing — cleaner architecture 
and easier to maintain.

## 6. Why I ordered records by -shift_date (descending) by default
The most recent shift is always the most relevant to the incoming team. If we 
ordered by ascending date, engineers would have to scroll to the bottom every 
time just to see what happened last. Descending order means the latest log is 
always first.