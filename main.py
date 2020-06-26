from video_splice import VideoSplice
from object_tracker import ObjectTracker
import sys


class Main():
    def __init__(self):
        self.video_file = ""
        self.filename = ""
        self.object_list = []
    def run(self):
        obj_tracker = ObjectTracker()
        video_splice = VideoSplice()
        obj_tracker.track_video(self.video_file)
        object_frames = obj_tracker.objects
        video_splice.cut_video(self.video_file, self.object_list, self.filename, object_frames)

if __name__ == "__main__":
    main = Main()
    main.video_file = sys.argv[1]
    main.filename = sys.argv[2]
    main.object_list = sys.argv[3:]
    main.run()
