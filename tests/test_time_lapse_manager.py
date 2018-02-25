from unittest import TestCase

from tests.mocks.mock_camera import MockCamera
from time_lapse_manager import TimeLapseManager

class TestTimeLapseManager(TestCase):
    def setUp(self):
        self.first_mock_camera = MockCamera("First")
        self.second_mock_camera = MockCamera("Second")
        self.third_mock_camera = MockCamera("Third")
        
        self.mock_camera_collection = [self.first_mock_camera,
            self.second_mock_camera]

    def test_init_works_without_camera_argument(self):
        try:
            TimeLapseManager()
        except Exception:
            self.fail("TimeLapseManager threw an exception during "
                "initialisation.")

    def test_get_cameras_returns_cameras(self):
        time_lapse_manager = TimeLapseManager(self.mock_camera_collection)

        self.assertEqual(time_lapse_manager.get_cameras(),
            self.mock_camera_collection)

    def test_add_camera_adds_camera_correctly(self):
        time_lapse_manager = TimeLapseManager(self.mock_camera_collection)

        time_lapse_manager.add_camera(self.third_mock_camera)

        new_mock_camera_collection = self.mock_camera_collection +\
            [self.third_mock_camera]

        self.assertEqual(new_mock_camera_collection,
            time_lapse_manager.get_cameras())

    def test_add_camera_ignores_duplicate_cameras(self):
        time_lapse_manager = TimeLapseManager(self.mock_camera_collection)

        time_lapse_manager.add_camera(self.third_mock_camera)
        time_lapse_manager.add_camera(self.third_mock_camera)

        new_mock_camera_collection = self.mock_camera_collection +\
            [self.third_mock_camera]

        self.assertEqual(new_mock_camera_collection,
            time_lapse_manager.get_cameras())
