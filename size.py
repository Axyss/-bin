
from os import path


class Size:

    def __init__(self):

        self.sizeVar = "0.0 MB"
        self.totalSize = 0

    def obtain_size(self, filtered_video_list):

        for i in filtered_video_list:

            self.totalSize += path.getsize(i)  # Default unit: byte

            if self.totalSize < 1000000000:  # Check if MB

                self.sizeVar = str(round(self.totalSize / 1000000, 2)) + " MB"

            elif self.totalSize >= 1000000000:  # Check if GB
                self.sizeVar = str(round(self.totalSize / 1000000000, 2)) + " GB"

        return self.sizeVar

    def reset(self):

        self.sizeVar = "0.0 MB"
        self.totalSize = 0


if __name__ != "__main__":
    size_obj = Size()
