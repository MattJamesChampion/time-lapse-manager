"""A library for managing time-lapse sequences."""


class TimeLapseManager:
    """A basic time-lapse manager."""

    def __init__(self, cameras=None):
        """Initialise the time-lapse manager with the camera that will be used.

        Args:
            cameras: A collection of cameras that will be used when capturing
                images using this time-lapse manager.
        """
        if cameras is not None:
            self._cameras = cameras[:]
        else:
            self._cameras = []

    def add_camera(self, camera):
        """Add a camera to the collection that will be used with this time-lapse manager.

        Args:
            camera: The camera to add
        """
        self._cameras.append(camera)

    def set_cameras(self, cameras):
        """Set the cameras that will be used with this time-lapse manager.

        Args:
            cameras: The cameras that will be used when capturing images using
                this time-lapse manager.
        """
        self._cameras = cameras

    def get_cameras(self):
        """Get the cameras currently set on this time-lapse manager."""
        return self._cameras
