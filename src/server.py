import hashlib
import os
import threading

from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler
from pyftpdlib.servers import FTPServer

from src.config.settings import (
    HOME_DIRECTORY,
    PASSWORD,
    SERVER_ADDRESS,
    SERVER_PORT,
    USER,
)


class FTPServerHandler:
    def __init__(self):
        self.server = None
        self.server_thread = None

    def init_server(self):
        # Check and create working directory if not exists
        if not os.path.exists(HOME_DIRECTORY):
            os.makedirs(HOME_DIRECTORY)
            print(f"Created working directory: {HOME_DIRECTORY}")

        # Create an authorizer
        authorizer = DummyAuthorizer()

        # Add user with settings from config
        authorizer.add_user(USER, PASSWORD, HOME_DIRECTORY, perm="elradfmwMT")

        # Create FTP handler
        handler = FTPHandler
        handler.authorizer = authorizer

        # Set IPv6 address and port
        address = (SERVER_ADDRESS, SERVER_PORT)

        # Create FTP server
        self.server = FTPServer(address, handler)

    def start(self):
        """Start FTP server in a separate thread"""
        if self.server is None:
            self.init_server()

        self.server_thread = threading.Thread(
            target=self.server.serve_forever,
            daemon=True,  # Set as daemon thread so it will exit when main program exits
        )
        self.server_thread.start()
        print(f"FTP server is running at [{SERVER_ADDRESS}]:{SERVER_PORT}")

    def stop(self):
        """Stop the FTP server"""
        if self.server:
            self.server.close_all()
            print("FTP server stopped")

    def add_binary_file(self, filename: str, content: bytes) -> bool:
        """Add a binary file to the FTP server's home directory

        Args:
            filename: Name of the file to create
            content: Binary content to write

        Returns:
            bool: True if successful, False otherwise
        """
        try:
            filepath = os.path.join(HOME_DIRECTORY, filename)
            with open(filepath, "wb") as f:
                f.write(content)
            return True
        except Exception as e:
            print(f"Error adding file: {e}")
            return False

    def get_file_sha256(self, filename: str) -> str:
        """Get SHA256 hash of a file in the FTP server's home directory

        Args:
            filename: Name of the file to hash

        Returns:
            str: SHA256 hash of the file, or empty string if file not found
        """
        try:
            filepath = os.path.join(HOME_DIRECTORY, filename)
            sha256_hash = hashlib.sha256()
            with open(filepath, "rb") as f:
                for byte_block in iter(lambda: f.read(4096), b""):
                    sha256_hash.update(byte_block)
            return sha256_hash.hexdigest()
        except Exception as e:
            print(f"Error calculating hash: {e}")
            return ""


def main():
    # Usage example
    ftp_server = FTPServerHandler()
    try:
        ftp_server.start()
        # Keep main thread running
        while True:
            input("Press Enter to stop the server...")
            break
    except KeyboardInterrupt:
        print("\nReceived exit signal")
    finally:
        ftp_server.stop()


if __name__ == "__main__":
    main()
