"""A library for managing time-lapse sequences."""


class TimeLapseManager:
    """A basic time-lapse manager."""

    def __init__(self, camera):
        """Initialise the time-lapse manager with the camera that will be used.

        Args:
            camera: The camera that will be used when capturing images using
                this time-lapse manager.
        """
        self.set_camera(camera)

    def set_camera(self, camera):
        """Set the camera that will be used with this time-lapse manager.

        Args:
            camera: The camera that will be used when capturing images using
                this time-lapse manager.
        """
        self._camera = camera

