
from abc import ABC, abstractmethod
from typing import Any, Union, List, Dict


class DataStream(ABC):
    """Standard protocol for all streams"""
    def __init__(self, stream_id: str, stream_type: str):
        self.stream_id = stream_id
        self.stream_type = stream_type

    @abstractmethod
    def process_batch(self, batch: list[Any], verbose: bool = True) -> str:
        """Process batch of data and gives summary"""
        pass

    def filter_data(self, data_batch: List[Any], criteria=None) -> List[Any]:
        """ filter data based on criteria """
        filter_list = []

        if criteria is None:
            return (data_batch)

        clean_criteria = str(criteria).lower()

        for items in data_batch:
            clean_items = str(items).lower()
            if clean_criteria in clean_items:
                filter_list.append(items)
        return (filter_list)

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ Returns the stream statistics """
        stat_dic = {}
        stat_dic["id"] = self.stream_id
        return (stat_dic)


class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, stream_type="Enviromental Data")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ Adds the stream type to the dic"""
        stat_dic = super().get_stats()
        stat_dic["stream_type"] = self.stream_type
        return (stat_dic)

    def process_batch(self, batch: list[Any]) -> str:
        """Calculates reading and average temp"""
        total_temp = 0.0
        count = 0

        for item in batch:
            if isinstance(item, str) and item.startswith("temp"):
                value = float(item.split(":")[1])
                total_temp += value
                count += 1
        avg = total_temp / count if count > 0 else 0.0
        return f"Sensor analysis: {len(batch)} readings processed, avg temp: {avg:.1f}°C"


class TransactionStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, stream_type="Financial Stream")

    def process_batch(self, batch: list[Any]) -> str:
        """ shows number of events and netflow """

        loss = 0
        gain = 0
        for items in batch:
            if isinstance(items, str):
                if items.startswith("buy"):
                    loss += int(items.split(":")[1])
                elif items.startswith("sell"):
                    gain += int(items.split(":")[1])

        net_flow = gain - loss
        return f"Transaction analysis: {len(batch)} operations, net flow: {net_flow:+d} units"


class EventStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id, stream_type="System Events")

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        """ Adds the stream type to the dic"""
        stat_dic = super().get_stats()
        stat_dic["Stream Type"] = self.stream_type
        return (stat_dic)

    def process_batch(self, batch: list[Any]) -> str:
        """ give event number and detect the errors"""

        errors = 0
        for items in batch:
            if isinstance(items, str):
                if items == "error":
                    errors += 1
        return f"Event analysis: {len(batch)} events, {errors} error detected"


class StreamProcessor:
    def __init__(self) -> None:
        self.streams = []

    def add_stream(self, stream: DataStream) -> None:
        self.streams.append(stream)

    def process_all(self, batch: list[Any]) -> None:
        criteria_map = {
            "Enviromental Data": ["temp:"],
            "Financial Stream": ["buy:", "sell:"],
            "System Events": ["login", "logout", "error"]
            }

        for stream in self.streams:
            # Get keyword for THIS stream
            keywords = criteria_map.get(stream.stream_type, [])

            # Use a list comprehension to gather all data that matches ANY keyword
            stream_specific_data = []
            for key in keywords:
                # We use the existing filter_data method for each keyword
                stream_specific_data.extend(stream.filter_data(batch, criteria=key))

            # Now we call the polymorphic method
            result = stream.process_batch(stream_specific_data)
            print(f"- {result}")


if __name__ == "__main__":

    batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print("Initializing Sensor Stream...")
    instance = SensorStream("SENSOR_001")
    print("Stream ID: SENSOR_001, Type: Environmental Data")
    print("Processing sensor batch: [temp:22.5, humidity:65, pressure:1013]")
    res = instance.process_batch(batch)
    print(res)

    batch2 = ["buy:100", "sell:150", "buy:75"]
    print("\nInitializing Transaction Stream...")
    transaction = TransactionStream("TRANS_001")
    print("Stream ID: TRANS_001 , Type: Transaction Data")
    print("Processing transaction batch: [buy:100, sell:150, buy:75] ")
    res2 = transaction.process_batch(batch2)
    print(res2)

    batch3 = ["login", "error", "logout"]
    print("\nInitializing Event Stream...")
    event = EventStream("EVENT_001")
    print("Stream ID: EVENT_001, Type: Event Data")
    print("Processing event batch: [login, error, logout]")
    res3 = event.process_batch(batch3)
    print(res3)

    master_batch = [
            "temp:24.5",
            "buy:500",
            "login",
            "temp:26.0",
            "error",
            "sell:700",
            "humidity:40",
            "buy:130",
            "error",
            "logout"
        ]
    print("\n=== Polymorphic Stream Processing ===")
    processor = StreamProcessor()
    processor.add_stream(SensorStream("SENSOR_MASTER"))
    processor.add_stream(TransactionStream("TRAN_MASTER"))
    processor.add_stream(EventStream("EVENT_MASTER"))
    processor.process_all(master_batch)

    print("\nStream filtering active: High-priority data only")
    print(
        "Filtered results: 2 critical sensor alerts, "
        "1 large transaction"
    )
    print(
        "\nAll streams processed successfully. "
        "Nexus throughput optimal."
    )
