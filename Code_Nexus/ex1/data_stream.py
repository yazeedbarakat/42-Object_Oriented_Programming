import typing
from abc import ABC, abstractmethod


class DataProcessor(ABC):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.total: int = 0
        self.name: str = ""

    @abstractmethod
    def validate(self, data: typing.Any) -> bool:
        pass

    @abstractmethod
    def ingest(self, data: typing.Any) -> None:
        pass

    def output(self) -> tuple[int, str]:
        i = self.queue.pop(0)
        n = self.total - len(self.queue) - 1
        return (n, i)


class NumericProcessor(DataProcessor):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.total: int = 0
        self.name: str = "Numeric Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        elif isinstance(data, list):
            return all(isinstance(i, (int, float)) for i in data)
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper numeric data")
        if isinstance(data, list):
            for i in data:
                self.queue.append(str(i))
                self.total += 1
        else:
            self.queue.append(str(data))
            self.total += 1


class TextProcessor(DataProcessor):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.total: int = 0
        self.name: str = "Text Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, str):
            return True
        elif isinstance(data, list):
            return all(isinstance(i, str) for i in data)
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper text data")
        if isinstance(data, list):
            for i in data:
                self.queue.append(i)
                self.total += 1
        else:
            self.queue.append(data)
            self.total += 1


class LogProcessor(DataProcessor):
    def __init__(self) -> None:
        self.queue: list[str] = []
        self.total: int = 0
        self.name: str = "Log Processor"

    def validate(self, data: typing.Any) -> bool:
        if isinstance(data, dict):
            return all(isinstance(k, str) and isinstance(v, str)
                       for k, v in data.items())
        elif isinstance(data, list):
            return all(isinstance(d, dict) and
                       all(isinstance(k, str) and isinstance(v, str) for k, v
                           in d.items()) for d in data)
        else:
            return False

    def ingest(self, data: typing.Any) -> None:
        if not self.validate(data):
            raise ValueError("Improper log data")
        if isinstance(data, list):
            for d in data:
                self.queue.append(f"{d['log_level']}: {d['log_message']}")
                self.total += 1
        else:
            self.queue.append(f"{data['log_level']}: {data['log_message']}")
            self.total += 1


class DataStream():
    def __init__(self) -> None:
        self.processors: list[DataProcessor] = []

    def register_processor(self, proc: DataProcessor) -> None:
        self.processors += [proc]

    def process_stream(self, stream: list[typing.Any]) -> None:
        for i in stream:
            h = False
            for j in self.processors:
                if j.validate(i):
                    j.ingest(i)
                    h = True
                    break
            if not h:
                print(f"DataStream error - Can't process element in stream: {i}")

    def print_processors_stats(self) -> None:
        if not self.processors:
            print("No processor found, no data")
            return
        for proc in self.processors:
            name = proc.name
            remaining = len(proc.queue)
            print(f"{name}: total {proc.total} items processed, "
                  f"remaining {remaining} on processor")

if __name__ == "__main__":
    print("=== Code Nexus - Data Stream ===\n")
    stream = DataStream()
    print("Initialize Data Stream...")
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nRegistering Numeric Processor")
    stream.register_processor(NumericProcessor())
    batch = ['Hello world', [3.14, -1, 2.71],
             [{'log_level': 'WARNING', 'log_message': 'Telnet access! Use ssh instead'},
              {'log_level': 'INFO', 'log_message': 'User wil is connected'}],
             42, ['Hi', 'five']]
    print(f"\nSend first batch of data on stream: {batch}")
    stream.process_stream(batch)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nRegistering other data processors")
    stream.register_processor(TextProcessor())
    stream.register_processor(LogProcessor())
    print("Send the same batch again")
    stream.process_stream(batch)
    print("== DataStream statistics ==")
    stream.print_processors_stats()
    print("\nConsume some elements from the data processors: Numeric 3, Text 2, Log 1")
    for i in range(3):
        stream.processors[0].output()
    for i in range(2):
        stream.processors[1].output()
    for i in range(1):
        stream.processors[2].output()
    print("== DataStream statistics ==")
    stream.print_processors_stats()
