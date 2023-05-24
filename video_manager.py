#!/bin/python3

import argparse
import mimetypes
import os

def __get_videos():
    videos = os.listdir()
    videos.sort()

    for v in videos:
        if os.path.isdir(v):
            videos.remove(v)
            continue
        try:
            if not mimetypes.guess_type(v)[0].startswith("video"):
                videos.remove(v)
        except AttributeError:
            videos.remove(v)

    print(videos)

    return videos 
    

def compression():
    videos = __get_videos()

    if not os.path.exists("output"):
	    os.mkdir("output")

    for v in videos:
        if not os.path.exists(f"output/{v}"):
            if os.system(f"ffmpeg -i '{v}' -vcodec libx265 -crf 30 'output/{v}'"):
                os.remove(f"output/{v}")
                return False
    
    return True


def conversion():
    videos = __get_videos()
    
    for v in videos:
        if not v.endswith("mp4"):
            e = os.system(f'ffmpeg -i """{v}""" -codec copy """{v[:v.rfind(".")]}.mp4"""')
            print(e)
            if e:
                os.remove(f"{v[:v.rfind('.')]}.mp4")
                return False
            
            os.remove(v)

    return True

parser = argparse.ArgumentParser()
parser.add_argument("-d", "--directory", help="Directory of videos", default="",action="store")
parser.add_argument("-x", "--compress", help="compress videos in the directory specified", action="store_true")
parser.add_argument("-c", "--convert", help="convert videos in the directory specified", action="store_true")

args = parser.parse_args()

if __name__ == "__main__":
    if not args.compress != args.convert:
        parser.print_help()
        exit(-1)

    if args.directory != "":
        try:
            os.chdir(args.directory)
        except FileNotFoundError:
            print("ERROR: Directory not found")
            exit(-1)

    else:
        os.chdir(args.directory)

    if args.compress:
        if not compression():
            print("ERROR: Compression Failed")
            exit(-1)
    
    if args.convert:
        if not conversion():
            print("ERROR: Conversion Failed")
            exit(-1)

    exit(0)