# -*- coding: utf-8 -*-
import re, requests, datetime

from django.shortcuts import get_object_or_404, render
from django.http import JsonResponse
from .models import Video, Type


# output = ', '.join([v.title for v in latest_videos_list])
def index(request):
    videos = Video.objects.order_by('-date_created')[:3]
    context = {'videos': videos}
    return render(request, 'video/index.html', context)


def video(request, video_id):
    video = get_object_or_404(Video, pk=video_id)
    return render(request, 'video/video.html', {'video': video})


def videoSubmit(request):
    return render(request, 'video/videoSubmit.html')


def videoCheck(request):
    videoURL = request.GET.get('url')

    matches = re.search('^https:\/\/video.nest.com\/clip\/([a-f0-9]{32})', videoURL)
    if not matches:
        return JsonResponse({'error': "That doesn't appear to be a valid URL", 'matches': matches, 'url': videoURL})

    # See if we already have it
    video = Video.objects.filter(pk=matches.group(1)).first()

    if video:
        return JsonResponse({'error': "We already have this video."})

    # See if it exists at Nest
    response = requests.head(videoURL)
    if response.status_code == requests.codes.ok:
        # We got one!
        type = Type.objects.get(pk=1)
        video = Video(id=matches.group(1), title='TBD', type=type, date_created=datetime.datetime.now())

        # Get the page proper to get the title
        page = requests.get(videoURL)
        if page.status_code == requests.codes.ok:
            rawTitle = re.search('\<title\>(.*)\<\/title\>', page.text)
            title = rawTitle.group(1)
            title = title.replace(' | Nest', '')
            video.title = title

        video.save()

        return JsonResponse({
            'success': 'It worked!',
            'id': matches.group(1)
        })

    return JsonResponse({'error': "Url didn't check out. Double check your copy & paste skills."})