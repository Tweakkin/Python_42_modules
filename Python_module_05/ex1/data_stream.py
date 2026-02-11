from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional

class DataStream(ABC):

    def __init__(self, stream_id: str) -> None:
        self.stream_id = stream_id
    
    @abstractmethod
    def process_batch(self, data_batch: List[Any]) -> str:
        pass
    
    def filter_data(self, data_batch: List[Any], criteria: Optional[str] = None) -> List[Any]:
        if not isinstance(data_batch, list):
            return []
        if criteria is None:
            return data_batch
        else:
            new_data = [i for i in data_batch if criteria in str(i)]
            return new_data

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id" : self.stream_id,
            "type": "Generic DataStream"
            }

class SensorStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_val = []
        temp_val = []
        for item in data_batch:
            try:
                str_item = str(item)
                if ':' in str_item:
                    parts = str_item.split(":")
                    valid_val.append(float(parts[1]))
                    if "temp" in parts[0]:
                        temp_val.append(float(parts[1]))
                else:
                    continue
            except (ValueError, IndexError):
                continue
            
        if not temp_val:
             return f"Sensor analysis: {len(valid_val)} readings processed, but no temperature data found."
        
        if not valid_val:
            return f"Sensor analysis: 0 readings processed"
        
        avg = sum(temp_val) / len(temp_val)
        if avg < -20:
            return f"Sensor analysis: {len(valid_val)} readings processed, avg temp: {avg:.1f}°C, Warning temp is too low!"
        elif avg > 50:
            return f"Sensor analysis: {len(valid_val)} readings processed, avg temp: {avg:.1f}°C, Warning temp is too high!"
        return f"Sensor analysis: {len(valid_val)} readings processed, avg temp: {avg:.1f}°C"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Environmental Data"
        }

class TransactionStream(DataStream):

    def process_batch(self, data_batch: List[Any]) -> str:
        valid_val = []
        buy_val = []
        sell_val = []
        for item in data_batch:
            try:
                str_item = str(item)
                if ':' in str_item:
                    parts = str_item.split(":")
                    if "buy" in parts[0]:
                        valid_val.append(float(parts[1]))
                        buy_val.append(float(parts[1]))
                    elif "sell" in parts[0]:
                        valid_val.append(float(parts[1]))
                        sell_val.append(float(parts[1]))
                else:
                    continue
            except (ValueError, IndexError):
                continue
        if not valid_val:
            return f"Transaction analysis: 0 readings processed"
        
        net = int(sum(buy_val)-sum(sell_val))
        net_str = f"+{net}" if net > 0 else f"{net}"

        return f"Transaction analysis: {len(valid_val)} operations, net flow: {net_str} units"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "Financial Data"
        }

class EventStream(DataStream):
    def process_batch(self, data_batch: List[Any]) -> str:
        valid_val = []
        err = []
        for item in data_batch:
            try:
                if not item:
                    continue
                
                str_item = str(item).strip()
                if not str_item:
                    continue
                if "error" in str_item.lower():
                    err.append(str_item)
                valid_val.append(str_item)
            except (ValueError, IndexError):
                continue

        if not valid_val:
            return f"Event analysis: 0 readings processed"

        return f"Event analysis: {len(valid_val)} events, {len(err)} error detected"

    def get_stats(self) -> Dict[str, Union[str, int, float]]:
        return {
            "stream_id": self.stream_id,
            "type": "System Events"
        }

class StreamProcessor:
    def __init__(self) -> None:
        self.streams = {}
    
    def add_stream(self, stream: DataStream) -> None:
        if stream.stream_id in self.streams:
            print(f"Error: Stream {stream.stream_id} already exists.")
            return
        self.streams[stream.stream_id] = stream
    
    def process_stream_data(self, stream_id: str, data_batch: List[Any]) -> str:
        if stream_id not in self.streams:
            return f"Error: Stream {stream_id} not found."
        stream = self.streams[stream_id]
        return stream.process_batch(data_batch)
    

def main() -> None:
    print("=== CODE NEXUS - POLYMORPHIC STREAM SYSTEM ===\n")

    print("Initializing Sensor Stream...")
    proc = SensorStream("SENSOR_001")
    print(f"Stream Id: {proc.get_stats()['stream_id']}, Type: {proc.get_stats()['type']}")
    data = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Processing sensor batch: {data}")
    print(proc.process_batch(data))

    print("\nInitializing Transaction Stream...")
    proc_t = TransactionStream("TRANS_001")
    stat = proc_t.get_stats()
    print(f"Stream ID: {stat['stream_id']}, Type: {stat['type']}")
    data2 = ["buy:100", "sell:150", "buy:75"]
    print(f"Processing transaction batch: {data2}")
    print(proc_t.process_batch(data2))

    print("\nInitializing Event Stream...")
    proc_e = EventStream("EVENT_001")
    stat2 = proc_e.get_stats()
    print(f"Stream ID: {stat2['stream_id']}, Type: {stat2['type']}")
    data3 = ["login", "error", "logout"]
    print(f"Processing event batch: {data3}")
    print(proc_e.process_batch(data3))

    print("\n=== Polymorphic Stream Processing ===")
    print("Processing mixed stream types through unified interface...\n")
    main_proc = StreamProcessor()

    main_proc.add_stream(SensorStream("SENSOR_001"))
    main_proc.add_stream(TransactionStream("TRANS_001"))
    main_proc.add_stream(EventStream("EVENT_001"))

    stream_data = [
        ("SENSOR_001", data),
        ("TRANS_001",   data2),
        ("EVENT_001",  data3)
    ]

    print("Batch 1 Results:")
    for id, dat in stream_data:
        print(f"- {main_proc.process_stream_data(id, dat)}")
    

    print("\nStream filtering active: High-priority data only")
    mixed_data_s = [
        "temp:20", 
        "critical:overheat",
        "critical:power_loss",
        "temp:22"
    ]
    mixed_data_t = [
        "buy:10", 
        "buy:50000",
        "sell:20"
    ]
    obj_sens = SensorStream("SENSOR_002")
    obj_trans = TransactionStream("TRANS_001")
    filtered_s = obj_sens.filter_data(mixed_data_s, "critical")
    filtered_t = obj_trans.filter_data(mixed_data_t, "50000")

    print(f"Filtered results: {len(filtered_s)} critical sensor alerts, {len(filtered_t)} large transaction")

    print("All streams processed successfully. Nexus throughput optimal.")

if __name__ == "__main__":
    main()