import typing
from data_processor import (
        DataProcessor,
        NumericProcessor,
        TextProcessor,
        LogProcessor,
    )


class DataStream:
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []
        self.processed: dict[DataProcessor, int] = {}

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors.append(proc)
        self.processed[proc] = 0

    def process_stream(self, stream: list[typing.Any]) -> None:
        for element in stream:
            found = False

            for proc in self.processors:
                if proc.validate(element):
                    before = len(proc.data)

                    try:
                        proc.ingest(element)
                    except (TypeError, ValueError) as error:
                        print(
                                f"DataStream error - "
                                f"Processor failed: {error}"
                            )
                    added = len(proc.data) - before
                    self.processed[proc] += added
                    found = True
                    break

            if not found:
                print(
                        f"DataStream error - Can't process "
                        f"element in stream: {element}"
                    )

    def print_processors_stats(self) -> None:
        print("== DataStream statistics ==")
        if not self.processors:
            print("No processor found, no data")
            return

        for proc in self.processors:
            name = type(proc).__name__.replace(
                    "Processor", "Processor"
                )
            total = self.processed[proc]
            remaining = len(proc.data)

            print(
                    f"{name}: total {total} items processed, "
                    f"remaining {remaining} on processor"
                )


if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    print("Initialize Data Stream...")

    stream = DataStream()
    stream.print_processors_stats()

    print("\nRegistering Numeric Processor\n")
    numeric = NumericProcessor()
    stream.register_processor(numeric)

    batch = [
        "Hello world",
        [3.14, -1, 2.71],
        [
            {
                "log_level": "WARNING",
                "log_message": "Telnet access! Use ssh instead",
            },
            {
                "log_level": "INFO",
                "log_message": "User wil is connected",
            },
        ],
        42,
        ["Hi", "five"],
    ]

    print(f"Send first batch of data on stream: {batch}")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print("\nRegistering other data processors")
    text = TextProcessor()
    logs = LogProcessor()
    stream.register_processor(text)
    stream.register_processor(logs)

    print("Send the same batch again")
    stream.process_stream(batch)
    stream.print_processors_stats()

    print(
        "\nConsume some elements from the data processors: "
        "Numeric 3, Text 2, Log 1"
    )

    for _ in range(3):
        numeric.output()

    for _ in range(2):
        text.output()

    logs.output()

    stream.print_processors_stats()
