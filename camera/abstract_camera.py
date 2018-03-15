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
