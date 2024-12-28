import os.path
from pathlib import Path
from unittest import TestCase
from unittest.mock import patch, MagicMock

from app.core.utils import get_default_output_dir, get_mp3_file


class TestUtils(TestCase):
    @patch('platform.system')
    @patch('os.environ', {'USERPROFILE': 'C:\\Users\\testuser'})
    def test_windows_path(self, mock_platform):
        mock_platform.return_value = 'Windows'

        result = get_default_output_dir()

        expected = os.path.join('C:\\Users\\testuser', 'Downloads')
        self.assertEqual(result, expected)
        mock_platform.assert_called_once()

    @patch('platform.system')
    @patch.dict('os.environ', {'HOME': '/home/testuser'})
    def test_linux_path(self, mock_platform):
        mock_platform.return_value = 'Linux'

        result = get_default_output_dir()

        expected = os.path.join('/home/testuser', 'Downloads')
        self.assertEqual(result, expected)
        mock_platform.assert_called_once()

    @patch('platform.system')
    @patch.dict('os.environ', {'HOME': '/Users/testuser'})
    def test_mac_path(self, mock_platform):
        mock_platform.return_value = 'Darwin'  # macOS is reported as 'Darwin'

        result = get_default_output_dir()

        expected = os.path.join('/Users/testuser', 'Downloads')
        self.assertEqual(result, expected)
        mock_platform.assert_called_once()

    @patch('platform.system')
    @patch.dict('os.environ', {}, clear=True)  # Ensure no env vars are present
    def test_missing_env_variables(self, mock_platform):
        mock_platform.return_value = 'Linux'  # Or any other platform

        with self.assertRaises(KeyError):  # Expecting a KeyError or specific behavior
            get_default_output_dir()

        mock_platform.assert_called_once()

    @patch("pathlib.Path.glob")
    def test_newest_mp3_file_found(self, mock_glob):
        """
        Test that the function correctly identifies the most recently modified MP3 file.
        """
        # Create mock MP3 files with different modification times
        mock_file1 = MagicMock()
        mock_file1.stat.return_value.st_mtime = 100
        mock_file1.name = "song1.mp3"

        mock_file2 = MagicMock()
        mock_file2.stat.return_value.st_mtime = 200
        mock_file2.name = "song2.mp3"

        mock_file3 = MagicMock()
        mock_file3.stat.return_value.st_mtime = 150
        mock_file3.name = "song3.mp3"

        # Mock the list of files returned by glob
        mock_glob.return_value = [mock_file1, mock_file2, mock_file3]

        output_folder = Path("/mock/output")
        result = get_mp3_file(output_folder)

        # Assert that the newest file is returned (song2.mp3 with mtime=200)
        self.assertEqual(result, mock_file2)

    @patch("pathlib.Path.glob")
    def test_no_mp3_files(self, mock_glob):
        """
        Test that the function returns None if no MP3 files are found in the directory.
        """
        # Mock an empty list (no MP3 files)
        mock_glob.return_value = []

        output_folder = Path("/mock/output")
        result = get_mp3_file(output_folder)

        # Assert that no file is found
        self.assertIsNone(result)

    @patch("pathlib.Path.glob")
    def test_only_one_mp3_file(self, mock_glob):
        """
        Test that the function correctly returns the single MP3 file in the directory.
        """
        # Create a single mock MP3 file
        mock_file = MagicMock()
        mock_file.stat.return_value.st_mtime = 100
        mock_file.name = "song.mp3"

        # Mock the list of files returned by glob
        mock_glob.return_value = [mock_file]

        output_folder = Path("/mock/output")
        result = get_mp3_file(output_folder)

        # Assert the single file is returned
        self.assertEqual(result, mock_file)

    @patch("pathlib.Path.glob")
    def test_folder_with_mixed_mp3_and_non_mp3_files(self, mock_glob):
        """
        Test that the function correctly identifies the most recently modified MP3 file,
        ignoring non-MP3 files.
        """
        # Create mock files with different extensions and modification times
        mock_file1 = MagicMock()
        mock_file1.stat.return_value.st_mtime = 100
        mock_file1.name = "song.mp3"

        mock_file2 = MagicMock()
        mock_file2.stat.return_value.st_mtime = 50
        mock_file2.name = "document.txt"

        mock_file3 = MagicMock()
        mock_file3.stat.return_value.st_mtime = 200
        mock_file3.name = "new_song.mp3"

        # Mock the list of files returned by glob
        mock_glob.return_value = [mock_file1, mock_file2, mock_file3]

        output_folder = Path("/mock/output")
        result = get_mp3_file(output_folder)

        # Assert that the most recent MP3 file is returned (new_song.mp3 with mtime=200)
        self.assertEqual(result, mock_file3)

