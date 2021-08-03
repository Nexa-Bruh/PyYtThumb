# Copyright (c) 2021 Itz-fork
# Part of Py-Yt-Thumb Project

import logging
from urllib.parse import urlparse, parse_qs

logger = logging.getLogger(__name__)

class YtThumb:
    def getthumb(url=None):
        url = url
        if url is None:
            logging.error("Url Isn't Provided")
        # Getting Video Id from given Url
        logging.info("Getting Video ID From Url")
        Yt_Vid_Id = YtThumb.extract_video_id(url)
        if Yt_Vid_Id is None:
            logging.error("Given Url is not a Youtube Url")
    
    def extract_video_id(url):
        query = urlparse(url)
        if query.hostname == 'youtu.be': return query.path[1:]
        if query.hostname in {'www.youtube.com', 'youtube.com'}:
            if query.path == '/watch': return parse_qs(query.query)['v'][0]
            if query.path[:7] == '/watch/': return query.path.split('/')[1]
            if query.path[:7] == '/embed/': return query.path.split('/')[2]
            if query.path[:3] == '/v/': return query.path.split('/')[2]
        return None
