
from abc import ABC, abstractmethod
from typing import Any


class DataProcessor(ABC):
    """
    The base of all Nexus processors, Parent class
    """
    @abstractmethod
    def validate(self, data: Any) -> bool:
        """Verify if the data can be processed"""
        pass

    @abstractmethod
    def process(self, data: Any) -> str:
        """Where it will transform"""
        pass

    def format_output(self, result: str) -> str:
        """convert result as a string"""
        return "this will be overwritten"


class NumericProcessor(DataProcessor):
    """
    Takes a list of numbers and calculates sum and average
    """

    def validate(self, data: Any) -> bool:
        """Makes sure its a list of ints/floats"""
        if isinstance(data, (int, float)):
            print("Validation: Numeric data verified")
            return True

        if isinstance(data, list):
            if all(isinstance(item, (int, float)) for item in data):
                print("Validation: Numeric data verified")
                return True

        print("Error: Validation failed for numeric data.")
        return False

    def process(self, data: list) -> str:
        """ extract the count, sum and average of the values"""
        values = data if isinstance(data, list) else [data]
        total = 0
        for num in values:
            total += num
        count = len(values)
        average = total / count
        return f"{count}, {total:.2f}, {average:.2f}"

    def format_output(self, result: str) -> str:
        """output formating for the numbers"""
        unpack = result.split(", ")
        return (f"Output: Processed {unpack[0]} numeric values, "
                f"sum={unpack[1]}, avg={unpack[2]}")


class TextProcessor(DataProcessor):
    """
    processes a string and returns numb of caracters and words
    """
    def validate(self, data: Any) -> bool:
        """Data needs to be a string"""

        if type(data) is not str:
            print("Error: Validation failed for text data.")
            return False
        else:
            print("Validation: text data verified")
            return True

    def process(self, data: str) -> str:
        """ counts words and char"""
        char_count = len(data)
        word_count = len(data.split())
        return f"{char_count}, {word_count}"

    def format_output(self, result: str) -> str:
        unpack = result.split(", ")
        return (f"Output: Processed text: {unpack[0]} characters, "
                f"{unpack[1]} words")


class LogProcessor(DataProcessor):
    """
    Manages as a filter to categorie data with keywords
    """
    def validate(self, data: Any) -> bool:
        """Verify that the log entry is a string"""
        if type(data) is not str:
            print("Error: Validation failed for log data.")
            return False
        print("Validation: Log entry verified")
        return True

    def process(self, data: str) -> str:
        """Detect the severity level of the log"""

        if "ERROR" in data:
            level = "ERROR"
            category = "ALERT"
        elif "INFO" in data:
            level = "INFO"
            category = "INFO"
        else:
            level = "UNKNOWN"
            category = "DEBUG"

        return f"{level}, {category}, {data}"

    def format_output(self, result: str) -> str:
        unpack = result.split(", ")
        return (f"Output: [{unpack[0]}] {unpack[1]} "
                f"level detected: {unpack[2]}")


if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")

    def tester():
        """tester for the 3 subclasses"""
        test_data = [
            [1, 54, 88, 12, 4.4, 2.3],
            "Hello Nexus World",
            "ERROR: Connection timeout"]
        processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
        names = ['Numeric', 'Text', 'Log']
        for i in range(len(processors)):
            proc = processors[i]
            data = test_data[i]

            print(f"\nInitializing {names[i]} Processor...")
            print(f"Processing data: {data}")

            if proc.validate(data):
                result = proc.process(data)
                output = proc.format_output(result)
                print(output)

    def polimorphic_tester():
        """Testing with a polimorphic way"""

        print("=== Polymorphic Processing Demo ===")
        print("Processing multiple data types through same interface...")

        processors = [NumericProcessor(), TextProcessor(), LogProcessor()]
        mix_data = [[1, 2, 3], "42 Neo-Tokyo", "INFO: System ready"]

        for i in range(len(processors)):
            proc = processors[i]
            mix = mix_data[i]
            if proc.validate(mix):
                res = proc.process(mix)
                print(f"Result {i + 1}: {proc.format_output(res)}")

    tester()
    print()
    polimorphic_tester()

    print("\nFoundation systems online. Nexus ready for advanced streams.")
