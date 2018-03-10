"""A mock implementation of a basic camera."""

import os
import sys
from camera.abstract_camera import AbstractCamera


class MockCamera(AbstractCamera):
    """A class representing a mock camera."""

    def __init__(self, name=""):
        """Initialise the mock camera.

        Args:
            name: The name or reference of this camera.
        """
        super().__init__(name)
        self._captured_images = []

    def capture_image(self, image_path, filename, overwrite=False):
        """Capture an image and store it in the specified location.

        Args:
            image_path: The full path that the image will be stored to.
            filename: The file name that the image will be stored as
                (including extension).
            overwrite: Specifies whether or not to overwrite a file if it
                already exists in the specified image_path with the specified
                filename.
        Raises:
            CameraCaptureError: If there is an issue with capturing the image
                caused by the camera.
            ImageStorageError: If the image can be captured but cannot be
                stored successfully.
        """
        self._captured_images.append(os.path.join(image_path, filename))

    def get_captured_images(self):
        """Return a list of filepaths of the images captured.

        Returns: A list of filepaths of the images captured.
        """
        return self._captured_images
