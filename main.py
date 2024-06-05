import datetime
import json
import os
import shutil
import sys


def main() -> None:
    """
    Main function that moves or deletes files from the source directory based on the config.json file.
    """
    if len(sys.argv) < 2:
        print("Usage: script.py [-m|-d] [source_directory]")
        sys.exit(1)

    action: str = sys.argv[1]
    source: str = (
        os.path.expanduser(f"~/{sys.argv[2]}")
        if len(sys.argv) == 3
        else os.path.expanduser("~/Downloads")
    )

    files: list = scan_source_directory(source)
    json_config: dict = load_json()

    if action == "-m":
        move(source, json_config, files)
    elif action == "-d":
        delete_files(source, json_config, files)
    else:
        print("Invalid option. Use -m to move files or -d to delete files.")
        sys.exit(1)


def move(source: str, json_config: dict, files: list) -> None:
    """
    Moves files from the source directory to the destination directory based on the config.json file.
    """

    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    log: str = f"Start transaction {current_date} {current_time}\n"

    for key in json_config:
        log += f"Moving {key} files\n"
        destination: str = os.path.expanduser(f"~/{json_config[key]['destination']}")
        extensions: list = json_config[key]["extension"]
        os.makedirs(destination, exist_ok=True)

        for file in files:
            if any(file.lower().endswith(ext) for ext in extensions):
                source_file = os.path.join(source, file)
                relative_path = os.path.relpath(source_file, source)
                destination_file = os.path.join(destination, relative_path)

                os.makedirs(os.path.dirname(destination_file), exist_ok=True)
                shutil.move(source_file, destination_file)

                current_time = datetime.datetime.now().strftime("%H:%M:%S")
                log += f"{current_time} - Moved {file} to {destination_file}\n"

    write_log_file(log)


def delete_files(source: str, json_config: dict, files: list) -> None:
    """
    Deletes files from the source directory based on the config.json file.
    """
    current_date = datetime.datetime.now().strftime("%Y-%m-%d")
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    log: str = f"Start transaction {current_date} {current_time}\n"
    files_deleted: bool = False

    extensions = json_config["delete"]["extension"]
    log += "Deleting files\n"

    for file in files:
        if any(file.lower().endswith(ext) for ext in extensions):
            source_file = os.path.join(source, file)
            os.remove(source_file)

            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            log += f"{current_time} - Deleted {file}\n"
            files_deleted = True

    if files_deleted:
        write_log_file(log)
    else:
        log += "No files to delete\n"
        write_log_file(log)


def load_json() -> dict:
    """Loads the config.json and returns a dictionary"""
    with open("config.json") as f:
        d = json.load(f)
    return d


def scan_source_directory(source: str) -> list:
    """
    Scans the source directory and returns a list of all files with their relative paths.
    """
    files: list = []
    for item in os.listdir(source):
        item_path = os.path.join(source, item)
        if os.path.isfile(item_path):
            files.append(item)
    return files


def write_log_file(log: str) -> None:
    """
    Writes the log to a file.
    """
    with open("log.txt", "a") as f:
        f.write(log + "\n")
        f.write("-" * 40 + "\n")

    print(log)


if __name__ == "__main__":
    main()
