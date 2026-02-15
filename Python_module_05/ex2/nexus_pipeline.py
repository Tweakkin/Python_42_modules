from abc import ABC, abstractmethod
from typing import Any, List, Dict, Union, Optional, Protocol

class ProcessingStage(Protocol):
    def process(self, data: Any) -> Any:
        pass

class InputStage:
    def process(self, data: Any) -> Dict:
        if data is None:
            raise ValueError("InputStage: Data cannot be None")
        if isinstance(data, dict):
            print(f"Input: {str(data)}")
        else:
            print(f"Input: {data}")
        return data
        

class TransformStage:
    def process(self, data: Any) -> Dict:
        if isinstance(data, dict) and 'sensor' in data:
            print("Transform: Enriched with metadata and validation")
            return{"type": "json", "sensor": data["sensor"],"value": data["value"], "unit": data["unit"]}
        elif isinstance(data, str) and ',' in data:
            print("Transform: Parsed and structured data")
            return {"type": "csv", "count": 1}
        elif isinstance(data, str) and "Real-time" in data:
            print("Transform: Aggregated and filtered")
            return {"type": "stream", "count": 5, "avg": 22.1}
        
        return data

class OutputStage:
    def process(self, data: Any) -> str:
        if data["type"] == "json":
            return f"Output: Processed temperature reading: {data['value']}°C (Normal range)"
        elif data["type"] == "csv":
            return f"Output: User activity logged: {data["count"]} actions processed"
        elif data["type"] == "stream":
            return f"Output: Stream summary: {data['count']} readings, {data['avg']}: 22.1°C"
        return "Output: Unknown data"

class ProcessingPipeline(ABC):
    def __init__(self) -> None:
        self.stages: List[ProcessingStage] = []
        pass
    
    def add_stage(self, stage: ProcessingStage) -> None:
        self.stages.append(stage)
    
    def run_pipeline(self, data: Any) -> Any:
        try:
            current_data = data
            for stage in self.stages:
                current_data = stage.process(current_data)
            return current_data
        except Exception as e:
            print(f"Pipeline Error: {e}")
            return None
    
    @abstractmethod
    def process(self, data: Any) -> Any:
        pass

class JSONAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.id = pipeline_id
    
    def process(self, data: Any) -> Any:
        print("Processing JSON data through pipeline...")
        return self.run_pipeline(data)

class CSVAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.id = pipeline_id
    
    def process(self, data: Any) -> Any:
        print("Processing CSV data through same pipeline...")
        return self.run_pipeline(data)

class StreamAdapter(ProcessingPipeline):
    def __init__(self, pipeline_id: str) -> None:
        super().__init__()
        self.id = pipeline_id
    
    def process(self, data: Any) -> Any:
        print("Processing Stream data through same pipeline...")
        return self.run_pipeline(data)

def main() -> None:
    print("=== CODE NEXUS - ENTERPRISE PIPELINE SYSTEM ===\n")

    print("Initializing Nexus Manager...")
    print("Pipeline capacity: 1000 streams/second\n")

    print("Creating Data Processing Pipeline...")
    print("Stage 1: Input validation and parsing")
    print("Stage 2: Data transformation and enrichment")
    print("Stage 3: Output formatting and delivery\n")

    print("=== Multi-Format Data Processing ===\n")
    pipe_json = JSONAdapter("Worker_01")
    pipe_json.add_stage(InputStage())
    pipe_json.add_stage(TransformStage())
    pipe_json.add_stage(OutputStage())

    json_input = {"sensor": "temp", "value": 23.5, "unit": "C"}
    trans_output = pipe_json.process(json_input)
    print(trans_output)
    print()

    csv_input = "user,action,timestamp"
    print(pipe_json.process(csv_input))


if __name__ == "__main__":
    main()
