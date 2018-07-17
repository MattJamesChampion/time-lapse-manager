"""An abstract representation of a basic camera."""

from abc import ABC, abstractmethod


class AbstractCamera(ABC):
    """An abstract class representing a basic camera."""

    def __init__(self, name="", storage_directory=None, file_extension=None):
        """Initialise the camera.

        Args:
            name: The name or reference of this camera.
            storage_directory: The directory that images will be stored to.
            file_extension: The file extension to be used on this camera.
        """
        self._name = name
        self.storage_directory = storage_directory
        self.file_extension = file_extension

    @abstractmethod
    def set_up(self):
        """Set up the camera so that it is ready to capture an image."""
        pass

    @abstractmethod
    def tear_down(self):
        """Free any resources held by the camera."""
        pass

    def __str__(self):
        """Return a string representation of this camera.
        
        Returns: A string representation of this camera.
        """
        return self._name

    @abstractmethod
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
        pass

    @abstractmethod
    def get_captured_image_paths(self):
        """Return a list of filepaths of the images captured.

        Returns: A list of filepaths of the images captured.
        """
        pass

    @abstractmethod
    def get_next_filename(self):
        """Return the filename of the next image that will be captured.

        Returns: The filename of the next image that will be captured.
        """
        pass

    @property
    def file_extension(self):
        """Return the file extension used on this camera.
        
        Returns: The file extension used on this camera.
        """
        return self._file_extension

    @file_extension.setter
    def file_extension(self, file_extension):
        """Set the file extension to be used on this camera.
        
        Args:
            file_extension: The file extension to be used on this camera.
        """
        self._file_extension = file_extension
