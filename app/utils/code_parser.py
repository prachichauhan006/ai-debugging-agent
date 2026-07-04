import re

def parse_traceback(traceback: str) -> dict:
    result = {
        "error_type": None,
        "error_message": None,
        "line_number": None,
        "file_name": None
    }

    # Extract error type and message
    error_match = re.search(r'(\w+Error|\w+Exception): (.+)', traceback)
    if error_match:
        result["error_type"] = error_match.group(1)
        result["error_message"] = error_match.group(2)

    # Extract file and line number
    location_match = re.search(r"File ['\"](.+)['\"], line (\d+)", traceback)
    if location_match:
        result["file_name"] = location_match.group(1)
        result["line_number"] = int(location_match.group(2))

    return result