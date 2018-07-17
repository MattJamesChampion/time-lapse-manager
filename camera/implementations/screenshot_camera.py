"""An interface for capturing screenshots."""

from os.path import join

from camera.abstract_camera import AbstractCamera
import wx

class ScreenshotCamera(AbstractCamera):
    """A class representing a screenshot camera."""

    def __init__(self,
                 name="Screenshot Camera",
                 storage_directory=None,
                 file_extension=None):
        """Initialise the screenshot camera.

        Args:
            name: The name or reference of this camera.
            storage_directory: The directory that images will be stored to.
            file_extension: The file extension to be used on this camera.
        """
        super().__init__(name, storage_directory, file_extension)

        self._captured_image_paths = []

    def set_up(self):
        """Set up the camera so that it is ready to capture an image."""
        pass

    def tear_down(self):
        """Free any resources held by the camera."""
        pass

    def __str__(self):
        """Return a string representation of this camera.

        Returns: A string representation of this camera.
        """
        return self._name

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

        full_path = join(self.storage_directory,
                         new_image_filename)

        if self.file_extension.lower() in ("jpg", "jpeg"):
            file_type = wx.BITMAP_TYPE_JPEG
        elif self.file_extension.lower() == "png":
            file_type = wx.BITMAP_TYPE_PNG
        elif self.file_extension.lower() == "gif":
            file_type = wx.BITMAP_TYPE_GIF
        else:
            file_type == wx.BITMAP_TYPE_JPEG

        try:
            app = wx.App()
            screen = wx.ScreenDC()

            screen_width, screen_height = screen.GetSize()

            bitmap = wx.Bitmap(screen_width, screen_height)

            memory = wx.MemoryDC(bitmap)
            memory.Blit(0, 0, screen_width, screen_height, screen, 0, 0)
        except Exception as exc:
            self._captured_image_paths.append(None)
            raise CameraCaptureError from exc

        bitmap.SaveFile(full_path, file_type)
        self._captured_image_paths.append(full_path)

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
