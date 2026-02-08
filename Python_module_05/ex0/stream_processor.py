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
        return f"{result} yahya"

class NumericProcessor(DataProcessor):
    def process(self, data: any) -> str:
        return ("Hello world!")
    
    def validate(self, data: any) -> bool:
        return True

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

num = NumericProcessor()
print(f"{num.format_output("hello")}")
