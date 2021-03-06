"""An interface for using the camera module on a Raspberry Pi."""

from os.path import join

from camera.abstract_camera import AbstractCamera
from camera.exceptions import CameraCaptureError
from picamera import PiCamera, PiCameraError


class RaspberryPiCamera(AbstractCamera):
    """A class representing the Raspberry Pi camera module."""

    def __init__(self,
                 name="Raspberry Pi Camera",
                 storage_directory=None,
                 file_extension="jpeg",
                 images_stored_locally=True):
        """Initialise the Raspberry Pi camera module.

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
        
        self._camera_handle = PiCamera()

    def set_up(self):
        """Set up the camera so that it is ready to capture an image."""
        pass

    def tear_down(self):
        """Free any resources held by the camera."""
        self._camera_handle.close()

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
        try:
            new_image_filename = (self.get_next_filename() +
                                  "." +
                                  self.file_extension)

            full_path = join(self.storage_directory,
                             new_image_filename)

            self._camera_handle.capture(full_path, format=self.file_extension)
            self._captured_image_paths.append(full_path)
        except PiCameraError as exc:
            self.tear_down()
            self._captured_image_paths.append(None)
            raise CameraCaptureError from exc

    def get_captured_image_paths(self):
        """Return a list of filepaths of the images captured.

        Returns: A list of filepaths of the images captured.
        """
        return self._captured_image_paths[:]

    def get_next_filename(self):
        """Return the filename of the next image that will be captured.

        Returns: The filename of the next image that will be captured.
        """
        return str(len(self.get_captured_image_paths()) + 1).rjust(8, "0")
