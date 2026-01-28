def manage_roster(enrolled, drop_requests, waitlist):
    for student in drop_requests:
        enrolled.discard(student)
       
    if len(enrolled) < 5:
        while len(enrolled) < 7 and len(waitlist) > 0:
            student = waitlist.pop()
            enrolled.add(student)
    return len(enrolled)