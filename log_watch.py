from logs.watcher import LogFileWatcher


def main():
    watcher = LogFileWatcher(
        redis_key="factorio_log_position",
        log_file_path="/home/factorio",
        file_name="factorio.log",
        target_words=["JOIN", "LEAVE"],
    )
    watcher.start_observer()


if __name__ == "__main__":
    main()
