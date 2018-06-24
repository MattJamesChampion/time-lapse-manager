"""A library for managing time-lapse sequences."""


class TimeLapseManager:
    """A basic time-lapse manager."""

    def __init__(self, cameras=None, capture_interval=10, capture_limit=None):
        """Initialise the time-lapse manager with the camera that will be used.

        Args:
            cameras: A collection of cameras that will be used when capturing
                images using this time-lapse manager.
            capture_interval: The interval (in seconds) to wait between
                capturing images.
            capture_limit: The maximum number of images to capture (or None for
                infinite).

        Raises:
            ValueError: If capture_interval is not greater than 0 or if
                capture_limit is not greater than 0 or None.
            TypeError: If capture_interval is not a numeric type or if
                capture_limit is not a numeric type or None.
        """
        if cameras is not None:
            self.set_cameras(cameras[:])
        else:
            self.set_cameras([])

        self.capture_interval = capture_interval
        self.capture_limit = capture_limit
        self._captured_frames = 0

    def add_camera(self, camera):
        """Add a camera to the collection on this time-lapse manager.

        Args:
            camera: The camera to add
        """
        if camera not in self._cameras:
            self._cameras.append(camera)

    def remove_camera(self, camera):
        """Remove a camera from the collection on this time-lapse manager.

        Raises:
            ValueError: If the camera does not exist.
        """
        self._cameras.remove(camera)

    def set_cameras(self, cameras):
        """Set the cameras that will be used with this time-lapse manager.

        Args:
            cameras: The cameras that will be used when capturing images using
                this time-lapse manager.
        """
        self._cameras = cameras[:]

    def get_cameras(self):
        """Get the cameras currently set on this time-lapse manager.

        Returns: A collection of cameras.
        """
        return self._cameras[:]

    def has_camera(self, camera):
        """Return whether the camera exists on this time-lapse manager.

        Returns: A boolean specifying whether the camera exists on this
            time-lapse manager.
        """
        if camera in self._cameras:
            return True
        else:
            return False

    @property
    def capture_interval(self):
        """Get the interval (in seconds) to wait between capturing images.

        Returns: The interval (in seconds) to wait between capturing images.
        """
        return self._capture_interval

    @capture_interval.setter
    def capture_interval(self, capture_interval):
        """Set the interval (in seconds) to wait between capturing images.

        Args:
            capture_interval: The interval (in seconds) to wait between
                capturing images.

        Raises:
            ValueError: If capture_interval is not greater than 0.
            TypeError: If capture_interval is not a numeric type.
        """
        try:
            if capture_interval > 0:
                self._capture_interval = capture_interval
            else:
                raise ValueError("capture_interval must be greater than 0.")
        except TypeError as error:
            exception_message = "capture_interval must be a numeric type."
            raise TypeError(exception_message) from error

    @property
    def capture_limit(self):
        """Get the maximum number of images to capture (or None for infinite).
        
        Returns: The maximum number of images to capture (or None for
            infinite).
        """
        return self._capture_limit

    @capture_limit.setter
    def capture_limit(self, capture_limit):
        """Set the maximum number of images to capture (or None for infinite).
        
        Args:
            capture_limit: The maximum number of images to capture (or None for
                infinite).

        Raises:
            ValueError: If capture_interval is not greater than 0.
            TypeError: If capture_interval is not a numeric type or None.
        """
        try:
            if capture_limit is None or capture_limit > 0:
                self._capture_limit = capture_limit
            else:
                raise ValueError("capture_limit must be greater than 0.")
        except TypeError as error:
            exception_message = "capture_limit must be a numeric type."
            raise TypeError(exception_message) from error

    @property
    def captured_frames(self):
        """Return the number of frames that have been captured.

        Returns: The number of frames that have been captured.
        """
        return self._captured_frames
