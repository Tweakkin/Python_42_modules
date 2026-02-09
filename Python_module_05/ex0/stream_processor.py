from abc import ABC, abstractmethod

class DataProcessor(ABC):
    #Process the data and return result string
    @abstractmethod
    def process(self, data: any) -> str:
        pass

    #Validate if data is appropriate for this processor
    @abstractmethod
    def validate(self, data: any) -> bool:
        pass
    
    #Format the output string
    def format_output(self, result: str) -> str:
        return f"Output: {str}"

class NumericProcessor(DataProcessor):
    def process(self, data: any) -> str:
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
    
    def validate(self, data: any) -> bool:
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
    def process(self, data: any) -> str:
        return ("Hello earth!")

    def validate(self, data: any) -> bool:
        return False

class LogProcessor(DataProcessor):

    def process(self, data: any) -> str:
        return ("Hello earth!")

    def validate(self, data: any) -> bool:
        return True

def main() -> None:
    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===\n")

    print("Initializing Numeric Processor...")
    num_p = NumericProcessor()
    data = [1, 2, 3, 4, 5]
    print(f"Processing data: {data}")
    print(f"Validation {"Numeric data verified" if num_p.validate(data) == True else "Failed"}")
    print(f"Output: {num_p.process(data)}")


main()