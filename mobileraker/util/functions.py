

import logging
import os
import subprocess
import uuid

# Based on the implementation of Klipperscreen https://github.com/jordanruthe/KlipperScreen/blob/e9df355b3b8c33b63d5cbb9f7f2c75bd879597c5/ks_includes/functions.py#L83


def get_software_version():
    prog = ('git', '-C', os.path.dirname(__file__), 'describe', '--always',
            '--tags', '--long', '--dirty')
    try:
        process = subprocess.Popen(prog, stdout=subprocess.PIPE,
                                   stderr=subprocess.PIPE)
        ver, err = process.communicate()
        retcode = process.wait()
        if retcode == 0:
            version = ver.strip()
            if isinstance(version, bytes):
                version = version.decode()
            return version
        else:
            logging.debug(f"Error getting git version: {err}")
    except OSError:
        logging.exception("Error runing git describe")
    return "?"


def is_valid_uuid(value):
    try:
        uuid.UUID(str(value))

        return True
    except ValueError:
        return False


def normalized_progress_interval_reached(last: int, current: int, interval: int) -> bool:
    """
    Check if the current progress has exceeded the normalized threshold based on increments.

    Parameters:
        last_progress (int): The previous progress value.
        current_progress (int): The current progress value.
        increment (int): The predefined increment to consider.

    Returns:
        bool: True if the current progress exceeds the normalized threshold, False otherwise.
    """
    noramlized = last - (last % interval)
    return abs(current - noramlized) >= interval
