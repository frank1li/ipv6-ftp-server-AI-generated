# FTP server configuration settings
import os

# Get current working directory
BASE_DIR = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

# Server address (IPv6)
SERVER_ADDRESS = "::"  # Listen on all available IPv6 addresses

# Server port
SERVER_PORT = 21

# User authentication details
USER = "user"
PASSWORD = "password"
HOME_DIRECTORY = os.path.join(BASE_DIR, "files")  # files directory in project root

# Maximum number of simultaneous connections
MAX_CONNECTIONS = 10

# Log file settings
LOG_FILE = os.path.join(BASE_DIR, "logs", "ftp.log")
