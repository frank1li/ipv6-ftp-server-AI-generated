import hashlib
import os

import pytest

from src.config.settings import HOME_DIRECTORY
from src.server import FTPServerHandler


class TestFTPServer:
    @pytest.fixture(autouse=True)
    def setup_teardown(self):
        # Setup
        self.server = FTPServerHandler()
        self.test_content = b"Hello, this is a test file content!"
        self.test_filename = "test.bin"

        yield  # Run tests here

        # Teardown
        if self.server.server:
            self.server.stop()

        test_filepath = os.path.join(HOME_DIRECTORY, self.test_filename)
        if os.path.exists(test_filepath):
            os.remove(test_filepath)

    def test_add_binary_file(self):
        # Start server
        self.server.start()

        # Add test file
        result = self.server.add_binary_file(self.test_filename, self.test_content)
        assert result is True

        # Verify file exists
        test_filepath = os.path.join(HOME_DIRECTORY, self.test_filename)
        assert os.path.exists(test_filepath)

        # Read file and verify content
        with open(test_filepath, "rb") as f:
            content = f.read()
        assert content == self.test_content

    def test_file_sha256(self):
        # Start server
        self.server.start()

        # Add test file
        self.server.add_binary_file(self.test_filename, self.test_content)

        # Calculate expected hash
        expected_hash = hashlib.sha256(self.test_content).hexdigest()

        # Get file hash from server
        actual_hash = self.server.get_file_sha256(self.test_filename)

        # Verify hashes match
        assert actual_hash == expected_hash

    def test_file_upload_download(self):
        """Test complete file upload and download cycle"""
        # Start server
        self.server.start()

        # Upload test file
        upload_result = self.server.add_binary_file(
            self.test_filename, self.test_content
        )
        assert upload_result is True

        # Download the file
        download_filepath = os.path.join(HOME_DIRECTORY, self.test_filename)
        with open(download_filepath, "rb") as f:
            downloaded_content = f.read()

        # Compare original and downloaded content
        assert downloaded_content == self.test_content

        # Optional: Also verify file size
        assert len(downloaded_content) == len(self.test_content)
