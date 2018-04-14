from unittest import TestCase

from tests.mocks.mock_camera import MockCamera
from time_lapse_manager import TimeLapseManager


class TestTimeLapseManager(TestCase):
    def setUp(self):
        self.first_mock_camera = MockCamera("First")
        self.second_mock_camera = MockCamera("Second")
        self.third_mock_camera = MockCamera("Third")

        self.capture_interval = 5
        self.capture_limit = 10

        self.mock_camera_collection = [self.first_mock_camera,
                                       self.second_mock_camera]

        self.basic_time_lapse_manager = TimeLapseManager(
            self.mock_camera_collection,
            self.capture_interval,
            self.capture_limit)

    def test_init_works_with_default_arguments(self):
        try:
            TimeLapseManager()
        except Exception:
            self.fail("TimeLapseManager threw an exception during "
                      "initialisation.")

    def test_init_sets_capture_interval_correctly(self):
        self.assertEqual(self.capture_interval,
                         self.basic_time_lapse_manager.capture_interval)

    def test_get_cameras_returns_cameras(self):
        self.assertEqual(self.mock_camera_collection,
                         self.basic_time_lapse_manager.get_cameras())

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

    def test_remove_camera_removes_existing_camera_correctly(self):
        existing_camera = self.second_mock_camera

        self.basic_time_lapse_manager.remove_camera(existing_camera)

        self.assertFalse(
            self.basic_time_lapse_manager.has_camera(existing_camera))

    def test_remove_camera_throws_value_error_when_camera_does_not_exist(self):
        nonexistant_camera = self.third_mock_camera

        with self.assertRaises(ValueError):
            self.basic_time_lapse_manager.remove_camera(nonexistant_camera)

    def test_has_camera_returns_true_when_camera_exists(self):
        existing_camera = self.first_mock_camera

        self.assertTrue(
            self.basic_time_lapse_manager.has_camera(existing_camera))

    def test_has_camera_returns_false_when_camera_does_not_exist(self):
        nonexistant_camera = self.third_mock_camera

        self.assertFalse(
            self.basic_time_lapse_manager.has_camera(nonexistant_camera))

    def test_set_cameras_updates_cameras_correctly(self):
        new_cameras_collection = [self.second_mock_camera,
                                  self.third_mock_camera]

        self.basic_time_lapse_manager.set_cameras(new_cameras_collection)

        self.assertEqual(new_cameras_collection,
                         self.basic_time_lapse_manager.get_cameras())

    def test_set_capture_interval_updates_capture_interval_correctly(self):
        new_capture_interval = 60

        self.basic_time_lapse_manager.capture_interval = new_capture_interval

        self.assertEqual(new_capture_interval,
                         self.basic_time_lapse_manager.capture_interval)

    def test_set_capture_interval_raises_value_error_when_capture_interval_is_not_greater_than_zero(self):
        new_capture_interval = 0

        with self.assertRaises(ValueError):
            self.basic_time_lapse_manager.capture_interval = new_capture_interval

    def test_set_capture_interval_raises_type_error_when_capture_interval_is_not_numeric(self):
        new_capture_interval = "Test"

        with self.assertRaises(TypeError):
            self.basic_time_lapse_manager.capture_interval = new_capture_interval

    def test_get_capture_interval_returns_correct_result(self):
        self.assertEqual(self.capture_interval,
                         self.basic_time_lapse_manager.capture_interval)

    def test_set_capture_limit_updates_capture_limit_correctly(self):
        new_capture_limit = 100

        self.basic_time_lapse_manager.capture_limit = new_capture_limit

        self.assertEqual(new_capture_limit,
                         self.basic_time_lapse_manager.capture_limit)

    def test_set_capture_limit_raises_value_error_when_capture_limit_is_not_greater_than_zero(self):
        new_capture_limit = 0

        with self.assertRaises(ValueError):
            self.basic_time_lapse_manager.capture_limit = new_capture_limit

    def test_set_capture_limit_raises_type_error_when_capture_limit_is_not_numeric(self):
        new_capture_limit = "Test"

        with self.assertRaises(TypeError):
            self.basic_time_lapse_manager.capture_limit = new_capture_limit

    def test_set_capture_limit_does_not_raise_type_error_when_capture_limit_is_none(self):
        new_capture_limit = None

        try:
            self.basic_time_lapse_manager.capture_limit = new_capture_limit
        except TypeError:
            self.fail("TimeLapseManager threw a TypeError exception when "
                      "setting capture_limit to None.")

    def test_get_capture_limit_returns_correct_result(self):
        self.assertEqual(self.capture_limit,
                         self.basic_time_lapse_manager.capture_limit)

