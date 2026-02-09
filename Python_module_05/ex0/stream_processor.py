from abc import ABC, abstractmethod
from typing import Any

class DataProcessor(ABC):
    #Process the data and return result string
    @abstractmethod
    def process(self, data: Any) -> str:
        pass

    #Validate if data is appropriate for this processor
    @abstractmethod
    def validate(self, data: Any) -> bool:
        pass
    
    #Format the output string
    def format_output(self, result: str) -> str:
        return f"Output: {result}"

class NumericProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Data failed validation from NumericProcessor"
            
            if isinstance(data, (int, float)):
                data = [data]

            total = sum(data)
            len_data = len(data)
            if len_data == 0:
                average = 0.0
            else:
                average = total / len_data
            return f"Processed {len_data} numeric values, sum={total}, avg={average:.1f}"
        except Exception as e:
            return f"Error processing data: {str(e)}"
    
    def validate(self, data: Any) -> bool:
        if isinstance(data, (int, float)):
            return True
        
        if isinstance(data, list):
            for item in data:
                if not isinstance(item, (int, float)):
                    return False
            return True
        else:
            return False

class TextProcessor(DataProcessor):
    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Data failed validation from TextProcessor"
            len_data = len(data)
            words = len(data.split())
            return f"Processed text: {len_data} characters, {words} words"
        except Exception as e:
            return f"Error processing data: {str(e)}"


    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            return True
        else:
            return False

class LogProcessor(DataProcessor):

    def process(self, data: Any) -> str:
        try:
            if not self.validate(data):
                return "Error: Data failed validation from LogProcessor"
            
            splitted = data.split(":", 1)
            p1, p2 = splitted
            return f"{p1} level detected:{p2}"
        except Exception as e:
            return f"Error processing data: {str(e)}"


    def validate(self, data: Any) -> bool:
        if isinstance(data, str):
            if not (':' in data):
                return False
            return True
        return False
    
    def format_output(self, result: str) -> str:
        if "ERROR" in result:
            return f"Output: [ALERT] {result}"
        elif "INFO" in result:
            return f"Output: [INFO] {result}"
        else:
            return f"Output: [LOG] {result}"

def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_p = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    print(f"Validation: {"Numeric data verified" if num_p.validate(data) == True else "Failed"}")
    processed_data = num_p.process(data)
    print(num_p.format_output(processed_data))

    print("\nInitializing Text Processor...")
    str1 = "Hello Nexus World"
    print(f'Processing data: "{str1}"')
    text_p = TextProcessor()
    print(f"Validation: {"Text data verified" if text_p.validate(str1) == True else "Failed"}")
    processed_text = text_p.process(str1)
    print(text_p.format_output(processed_text))

    print("\nInitializing Log Processor...")
    data1 = "ERROR: Connection timeout"
    print(f'Processing data: "{data1}"')
    print(f"Validation: {"Log entry verified" if num_p.validate(data1) == True else "Failed"}")
    log_p = LogProcessor()
    processed_log = log_p.process(data1)
    print(log_p.format_output(processed_log))

    print("\n=== Polymorphic Processing Demo ===")
    print("Processing multiple data types through same interface...")
    processors = [
        NumericProcessor(),
        TextProcessor(),
        LogProcessor()
    ]
    data_streams = [
        [1, 2, 3],
        "Hello World!",
        "INFO: System ready"
    ]
    for i in range(len(processors)):
        curr_proc = processors[i]
        curr_data = data_streams[i]

        processed = curr_proc.process(curr_data)
        output = curr_proc.format_output(processed)
        print(f"Result {i + 1}: {processed}")
    
    print("\nFoundation systems online. Nexus ready for advanced streams.")


if __name__ == "__main__":
    main()