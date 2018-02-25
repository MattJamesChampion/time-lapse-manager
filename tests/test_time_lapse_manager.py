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
            
        self.basic_time_lapse_manager = TimeLapseManager(self.mock_camera_collection)

    def test_init_works_without_camera_argument(self):
        try:
            TimeLapseManager()
        except Exception:
            self.fail("TimeLapseManager threw an exception during "
                "initialisation.")

    def test_get_cameras_returns_cameras(self):
        self.assertEqual(self.basic_time_lapse_manager.get_cameras(),
            self.mock_camera_collection)

    def test_add_camera_adds_camera_correctly(self):
        self.basic_time_lapse_manager.add_camera(self.third_mock_camera)

        new_mock_camera_collection = self.mock_camera_collection +\
            [self.third_mock_camera]

        self.assertEqual(new_mock_camera_collection,
            self.basic_time_lapse_manager.get_cameras())

    def test_add_camera_ignores_duplicate_cameras(self):
        self.basic_time_lapse_manager.add_camera(self.third_mock_camera)
        self.basic_time_lapse_manager.add_camera(self.third_mock_camera)

        new_mock_camera_collection = self.mock_camera_collection +\
            [self.third_mock_camera]

        self.assertEqual(new_mock_camera_collection,
            self.basic_time_lapse_manager.get_cameras())

    def test_has_camera_returns_true_when_camera_exists(self):
        existing_camera = self.first_mock_camera
    
        self.assertTrue(
            self.basic_time_lapse_manager.has_camera(existing_camera))

    def test_has_camera_returns_false_when_camera_does_not_exist(self):
        nonexistant_camera = self.third_mock_camera
        
        self.assertFalse(
            self.basic_time_lapse_manager.has_camera(nonexistant_camera))
