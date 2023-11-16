import pandas as pd


def read_log_file(file_name):
    """
    Generator function to read a log file line by line
    """
    with open(file_name, "r") as file:
        for line in file:
            yield line


def parse_log_line(line):
    """
    Parse a single line of log file
    """
    timestamp, _, rest = line.partition(" - ")
    log_level, _, log_info = rest.partition("  ")

    return pd.Series(
        {
            "Timestamp": timestamp.strip(),
            "LogLevel": log_level.strip(),
            "LogInfo": log_info.strip(),
        }
    )


def parse_logs(log_file):
    """
    Parse the log file and return a dataframe
    """
    df = pd.DataFrame(columns=["Timestamp", "LogLevel", "LogInfo"])

    df = pd.concat(
        [parse_log_line(line) for line in read_log_file(log_file)],
        ignore_index=True,
        axis=1,
    ).T

    return df


if __name__ == "__main__":
    df = parse_logs("Zookeeper_2k.log")

    df.to_csv("parsed_logs.csv", index=False)
