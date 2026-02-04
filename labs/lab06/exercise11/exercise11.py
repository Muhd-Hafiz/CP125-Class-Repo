def get_student_courses(enrollments, student_id):
    """Return set of courses this student has completed."""
    completed = []
    for sid, course in enrollments:
            if sid == student_id and course not in completed:
                completed.append(course)
    return set(completed)

def find_missing_courses(completed_courses, required_courses):
    """Return set of required courses not yet completed."""
    missing = []
    for course in required_courses:
        if course not in completed_courses:
            missing.append(course)
    return set(missing)

def build_student_report(students, enrollments, required_courses):
    """Return sorted list of tuples (student_id, missing_count) for students with missing courses."""
    incomplete = []
    for student_id in students:
        completed_courses = get_student_courses(enrollments, student_id)
        missing_courses = find_missing_courses(completed_courses, required_courses)
        if len(missing_courses) > 0:
            incomplete.append((student_id, len(missing_courses)))

    return sorted(incomplete, key=lambda x: (-x[1], x[0]))


def find_incomplete_students(enrollments, required_courses):
    """Find students who haven't completed all required courses."""
    students = set()
    for student_id, i in enrollments:
        students.add(student_id)
        
    return build_student_report(students, enrollments, required_courses)