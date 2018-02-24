"""An abstract representation of a basic camera."""

from abc import ABC, abstractmethod


class AbstractCamera(ABC):
    """An abstract class representing a basic camera."""

    @abstractmethod
    def capture_image(self, image_path, filename, overwrite=False):
        """Capture an image and store it in a specified location.

        Args:
            image_path: The full path that the image will be stored to.
            filename: The file name that the image will be stored as
                (including extension).
            overwrite: Specifies whether or not to overwrite a file if it
                already exists in the specified image_path with the specified
                filename.
        """
        pass
