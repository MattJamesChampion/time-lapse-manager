from unittest import TestCase

from tests.mocks.mock_camera import MockCamera
from time_lapse_manager import TimeLapseManager

class TestTimeLapseManager(TestCase):
    def setUp(self):
        self.mock_camera = MockCamera()

    def test_camera_is_set_on_creation(self):
        time_lapse_manager = TimeLapseManager(self.mock_camera)

        self.assertEqual(time_lapse_manager.get_camera(), self.mock_camera)
