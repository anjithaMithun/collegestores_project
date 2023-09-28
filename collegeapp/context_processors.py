from .models import Department, Courses


def menu_links(request):
    links = Department.objects.all()
    return dict(links=links)


def course_links(request):
    links1 = Courses.objects.all()
    return dict(links1=links1)
