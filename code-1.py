from pytube import YouTube
import os
import yaml
import ssl
ssl._create_default_https_context = ssl._create_stdlib_context

""" pip3 install pytube
    pip3 install pytube3
    참고 : https://python-pytube.readthedocs.io/en/latest/user/quickstart.html
    group-study d-1 : 3/3번문제
    __author__ : KimJunHyeon
"""

class YouTubeGet():

    utube_path = "./config/utube_url_list.yml"

    def __init__(self):
        self.utube_list = YouTubeGet.get_utube_list()
        self.utube_video_download_path = "./video"

    def download_utube_video(self):
        for u in self.utube_list["url_list"]:
            yt = YouTube(u)
            self.video_information(yt)

            yt.streams \
                    .filter(progressive=True, file_extension='mp4')\
                    .order_by('resolution')\
                    .desc()\
                    .first()\
                    .download(self.utube_video_download_path)

    def video_information(self, yt):
        print("===================================")
        print("1.영상 제목 : ", yt.title)
        print("2.영상 길이 : ", yt.length)
        print("3.영상 평점 : ", yt.rating)
        print("4.영상 썸네일 링크 : ", yt.thumbnail_url)
        print("5.영상 조회수 : ", yt.views)
        print("6.영상 설명 : ", yt.description)
        print("===================================")

    @classmethod
    def get_utube_list(cls):
        result = os.path.isfile(YouTubeGet.utube_path)
        if result:
            with open(YouTubeGet.utube_path, "r", encoding="utf-8") as fr:
                info_ = yaml.safe_load(fr)
                fr.close()
                return info_
        else:
            exit(1)

if __name__ == "__main__":
    o_instance = YouTubeGet()
    o_instance.download_utube_video()