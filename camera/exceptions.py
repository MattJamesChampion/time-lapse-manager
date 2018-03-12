"""A collection of custom Exceptions specifically pertaining to cameras."""


class CameraConnectionError(Exception):
    """Camera could not be contacted."""
    pass


class CameraCaptureError(Exception):
    """Camera could not capture the image."""
    pass


class ImageStorageError(Exception):
    """Image could not be stored."""
    pass
