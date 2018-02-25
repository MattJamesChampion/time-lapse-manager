from unittest import TestCase

from tests.mocks.mock_camera import MockCamera
from time_lapse_manager import TimeLapseManager

class TestTimeLapseManager(TestCase):
    def setUp(self):
        self.first_mock_camera = MockCamera("First")
        self.second_mock_camera = MockCamera("Second")
        
        self.mock_camera_collection = [self.first_mock_camera,
            self.second_mock_camera]

    def test_get_cameras_returns_cameras(self):
        time_lapse_manager = TimeLapseManager(self.mock_camera_collection)

        self.assertEqual(time_lapse_manager.get_cameras(),
            self.mock_camera_collection)
