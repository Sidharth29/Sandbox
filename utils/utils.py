import os
import pandas as pd


def get_file_size_stats(filepath: str):
    """
    Retrieve file size for a specific file
    Args:
    -----
    filepath: The corresponding file path
    """
    # Load the CSV file using pandas (adjust the path to your file)
    csv_file_path = filepath

    # Get the file size in bytes
    file_size_bytes = os.path.getsize(csv_file_path)

    # Convert the file size to KB, MB, or GB
    file_size_kb = file_size_bytes / 1024
    file_size_mb = file_size_kb / 1024
    file_size_gb = file_size_mb / 1024

    print(f"File size: {file_size_bytes} bytes")
    print(f"File size: {file_size_kb:.2f} KB")
    print(f"File size: {file_size_mb:.2f} MB")
    print(f"File size: {file_size_gb:.2f} GB")