from django.http import HttpResponse
from django.template import loader
from django.shortcuts import render
from .models import *


def index(request):
    sector_list = Sector.objects.all()
    template = loader.get_template('kiosk/index.html')
    context = {'sectors': sector_list}
    return HttpResponse(template.render(context, request))


def landing(request):
    template = loader.get_template('kiosk/landing.html')
    context = {'announcements': Announcements.objects.first()}
    return HttpResponse(template.render(context, request))


def projects(request, sector_id):
    sector_name = Sector.objects.get(pk=sector_id).sector_text
    project_list = Project.objects.filter(sector=sector_id)
    return render(request, 'kiosk/sector.html', {'projects': project_list, 'sectorname': sector_name, 'sid': sector_id})


def artifacts(request, project_id):
    p = Project.objects.get(pk=project_id)
    project_name = p.project_text
    sector_name = p.sector.sector_text
    di = DiscussionItem.objects.filter(discussion_id=project_id)
    alist = Artifact.objects.filter(project=project_id)
    return render(request, 'kiosk/project.html',
                  {'artifacts': alist, 'projectname': project_name, 'sectorname': sector_name,
                   'sid': p.sector.id, 'pid': project_id, 'discussion': di})


def artifact(request, artifact_id):
    ar = Artifact.objects.get(pk=artifact_id)
    di = DiscussionItem.objects.filter(discussion_id=artifact_id, discussion_type=2)
    return render(request, 'kiosk/artifact.html',
                  {'artifact': ar, 'projectname': ar.project.project_text, 'sectorname': ar.project.sector.sector_text,
                   'discussion': di});
