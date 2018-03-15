"""A mock implementation of a basic camera."""

import os
import sys
from camera.abstract_camera import AbstractCamera


class MockCamera(AbstractCamera):
    """A class representing a mock camera."""

    def __init__(self, name="", storage_directory=None):
        """Initialise the mock camera.

        Args:
            name: The name or reference of this camera.
            storage_directory: The directory that images will be stored to.
        """
        super().__init__(name, storage_directory)

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
            CameraConnectionError: If there is an issue with contacting the
                camera.
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

    def get_next_filename(self):
        """Return the filename of the next image that will be captured.

        Returns: The filename of the next image that will be captured.
        """
        number_of_captured_images = len(self._captured_images)
        
        return f"{number_of_captured_images + 1:08}"
