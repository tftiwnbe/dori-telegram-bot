from logs.watcher import LogFileWatcher


def main():
    watcher = LogFileWatcher(
        redis_key="file_log_position",
        log_file_path="path/to/file",
        file_name="/file.log",
        target_words=["Start", "Dead"],
    )
    watcher.start_observer()


if __name__ == "__main__":
    main()
