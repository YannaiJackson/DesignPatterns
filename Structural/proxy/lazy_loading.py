
class RealImage:
    def __init__(self, filename):
        print(f"Loading image {filename} from disk...")
        self.filename = filename

    def display(self):
        print(f"Displaying {self.filename}")


class ImageProxy:
    def __init__(self, filename):
        self.filename = filename
        self._real_image = None

    def display(self):
        if self._real_image is None:
            self._real_image = RealImage(self.filename)
        self._real_image.display()


# Usage
if __name__ == "__main__":
    image = ImageProxy("large_photo.png")
    image.display()
    image.display()
