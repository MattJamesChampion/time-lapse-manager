"""A mock implementation of a basic camera."""

import os
import sys
from camera.abstract_camera import AbstractCamera


class MockCamera(AbstractCamera):
    """A class representing a mock camera."""

    def __init__(self,
                 name="",
                 storage_directory=None,
                 file_extension="jpg",
                 images_stored_locally=True):
        """Initialise the mock camera.

        Args:
            name: The name or reference of this camera.
            storage_directory: The directory that images will be stored to.
            file_extension: The file extension to be used on this camera.
            images_stored_locally: Whether the images are stored on a locally
                accessible device or not.
        """
        super().__init__(name,
                         storage_directory,
                         file_extension,
                         images_stored_locally)

        self._captured_image_paths = []

    def set_up(self):
        """Set up the camera so that it is ready to capture an image."""
        pass

    def tear_down(self):
        """Free any resources held by the camera."""
        pass

    def capture_image(self):
        """Capture an image to the default storage_directory.

        Raises:
            CameraConnectionError: If there is an issue with contacting the
                camera.
            CameraCaptureError: If there is an issue with capturing the image
                caused by the camera.
            ImageStorageError: If the image can be captured but cannot be
                stored successfully.
        """
        new_image_filename = (self.get_next_filename() +
                             "." +
                             self.file_extension)

        if self.storage_directory is not None:
            new_image_path = os.path.join(self.storage_directory,
                                          new_image_filename)
        else:
            new_image_path = new_image_filename

        self._captured_image_paths.append(new_image_path)

    def get_captured_image_paths(self):
        """Return a list of filepaths of the images captured.

        Returns: A list of filepaths of the images captured.
        """
        return self._captured_image_paths[:]

    def get_next_filename(self):
        """Return the filename of the next image that will be captured.

        Returns: The filename of the next image that will be captured.
        """
        number_of_captured_images = len(self.get_captured_image_paths())
        
        return str(number_of_captured_images + 1).rjust(8, "0")
