# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    stream_processor.py                                :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/07 15:21:03 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/07 17:28:27 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

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
    def process(self, data: Any) -> Any:
        """Where it will transform"""
        pass
    @abstractmethod
    def format_output(self, result: Any) -> str:
        """convert result as a string"""
        pass

class NumericProcessor(DataProcessor):
    """
    Takes a list of numbers and calculates sum and average
    """

    def validate(self, data: Any) -> bool:
        """Makes sure its a list of ints/floats"""
    
        if type(data) is not list or len(data) == 0:
            print("Error: Validation failed for numeric data.")
            return False
        for items in data:
            if type(items) is not int and type(items) is not float:
                print("Error: Validation failed for numeric data.")
                return False
        print("Validation: Numeric data verified")
        return True

    def process(self, data: list) -> dict:
        """ extract the count, sum and average of the values"""
        sum = 0
        for num in data:
            sum += num
        count = len(data)
        average = sum / count
        return {
            "count": count,
            "sum": sum,
            "average": average
        }

    def format_output(self, result: dict) -> str:
        """output formating for the numbers"""
        return (f"Output: Processed {result['count']} numeric values, "
                f"sum={result['sum']}, avg={result['average']}")

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
    
    def process(self, data: str) -> dict:
        """ counts words and char"""
        char_count = len(data)
        word_count = len(data.split()) # list of words...
        return {
            "char_count": char_count,
            "word_count": word_count
        }
    
    def format_output(self, result: dict) ->str:
        return (f"Output: Processed text: {result['char_count']} characters, "
                f"{result['word_count']} words")

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

    def process(self, data: str) -> dict:
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
            
        return {
            "level": level,
            "category": category,
            "message": data
        }

    def format_output(self, result: dict) -> str:
            return (f"Output: [{result['category']}] {result['level']} "
                    f"level detected: {result['message']}")

        

if __name__ == "__main__":

    print("=== CODE NEXUS - DATA PROCESSOR FOUNDATION ===")
    
    def tester():
        """tester for the 3 subclasses"""
        test_data = [[1, 2, 3, 4, 5], "Hello Nexus World", "ERROR: Connection timeout"]
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
            res = proc.process(mix)
            print(f"Result {i + 1}: {proc.format_output(res)}")

    tester()
    print()
    polimorphic_tester()

    print("\nFoundation systems online. Nexus ready for advanced streams.")



    

    
# So the abstract method 
# defines “what must exist,” and each subclass defines “how it works.”
