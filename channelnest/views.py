# -*- coding: utf-8 -*-
import re, requests, datetime, json

from django.shortcuts import get_object_or_404, render
from django.http import HttpResponse, Http404, JsonResponse
from .models import Video


# output = ', '.join([v.title for v in latest_videos_list])
def index(request):
    videos = Video.objects.order_by('date_created')[:3]
    context = {'videos': videos}
    return render(request, 'video/index.html', context)


def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video/video.html', {'video': video})


def videoSubmit(request):
    return render(request, 'video/videoSubmit.html')


def videoCheck(request):
    videoURL = request.POST['url']

    matches = re.search('/https?:\/\/video.nest.com\/clip\/([a-f0-9]{32})(\.mp4)?/',videoURL)
    if not matches:
        raise Http404("That doesn't appear to be a valid URL")

    # See if we already have it
    video = Video.objects.get(pk=matches.group(1))
    if video:
        raise HttpResponse("We already have this video.", status=400)

    # See if it exists at Nest
    response = requests.head(videoURL)
    if response.status_code == requests.codes.ok:
        # We got one!
        video = Video(id=matches.group(1), title='TBD', type=1, date_created=datetime.now())

        # Get the page proper to get the title
        page = requests.get(videoURL)
        if page.status_code == requests.codes.ok:
            rawTitle = re.search("/\<title\>(.*)\<\/title\>/i", page.content)
            title = rawTitle.group(1)
            title.replace(' | Nest', '')
            video.title = title

        video.save()

        return JsonResponse({
            'success': 'It worked!',
            'id': matches.group(1)
        })

    return JsonResponse({'error': "Url didn't check out. Double check your copy & paste skills."})