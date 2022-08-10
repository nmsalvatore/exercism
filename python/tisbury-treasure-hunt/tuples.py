"""Functions to help Azara and Rui locate pirate treasure."""


def get_coordinate(record):
    """Return coordinate value from a tuple containing the treasure name, and treasure coordinate."""
    return record[1]


def convert_coordinate(coordinate):
    """Split the given coordinate into tuple containing its individual components."""
    return (coordinate[0], coordinate[1])


def compare_records(azara_record, rui_record):
    """Compare two record types and determine if their coordinates match."""
    azara_coordinate = get_coordinate(azara_record)
    rui_coordinate = get_coordinate(rui_record)
    return convert_coordinate(azara_coordinate) == rui_coordinate


def create_record(azara_record, rui_record):
    """Combine the two record types (if possible) and create a combined record group."""
    if compare_records(azara_record, rui_record):
        return azara_record  + rui_record

    return 'not a match'


def clean_up(combined_record_group):
    """Clean up a combined record group into a multi-line string of single records."""
    combined_record_string = """"""

    for record in combined_record_group:
        record_list = list(record)
        del record_list[1]
        record = tuple(record_list)
        combined_record_string += str(record) + '\n'

    return combined_record_string
