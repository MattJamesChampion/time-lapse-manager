"""An abstract representation of a basic camera."""

from abc import ABC, abstractmethod


class AbstractCamera(ABC):
    """An abstract class representing a basic camera."""

    def __init__(self, name=""):
        """Initialise the camera.

        Args:
            name: The name or reference of this camera.
        """
        self._name = name
        self.storage_directory = None

    def __str__(self):
        """Return a string representation of this camera.
        
        Returns: A string representation of this camera.
        """
        return self._name

    @abstractmethod
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
        pass

    @abstractmethod
    def get_captured_images(self):
        """Return a list of filepaths of the images captured.

        Returns: A list of filepaths of the images captured.
        """
        pass
