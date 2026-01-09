# **************************************************************************** #
#                                                                              #
#                                                         :::      ::::::::    #
#    data_stream.py                                     :+:      :+:    :+:    #
#                                                     +:+ +:+         +:+      #
#    By: anaiscaire <anaiscaire@student.42.fr>      +#+  +:+       +#+         #
#                                                 +#+#+#+#+#+   +#+            #
#    Created: 2026/01/07 17:29:05 by anaiscaire        #+#    #+#              #
#    Updated: 2026/01/08 22:05:42 by anaiscaire       ###   ########.fr        #
#                                                                              #
# **************************************************************************** #

from abc import ABC, abstractmethod
from typing import Any

class DataStream(ABC):
    """Standard protocol for all streams"""
    def __init__(self, stream_id: str):
        self.stream_id = stream_id

    @abstractmethod
    def process_batch(self, batch: list[Any], verbose: bool = True) -> str:
        """Process batch of data and gives summary"""
        pass

  #  @abstractmethod
   # def get_info(self) -> str:
    #    """way to identify all streams"""
     #   return f"Stream id: {self.stream_id}"

class SensorStream(DataStream):
    def __init__(self, stream_id: str):
        super().__init__(stream_id)
        self.stream_type = "Enviromental Data"

    def process_batch(self, batch: list[Any], verbose: bool) -> str:
        """Calculates reading and average temp"""
        if verbose:
            print(f"Initializing Sensor Stream...")
            print(f"Stream ID: {self.stream_id}, Type: {self.stream_type}")
            print(f"Processing sensor batch: {batch}")    
        total_temp = 0.0
        count = 0
        
        for item in batch:
            if isinstance(item, str) and item.startswith("temp"):
                value = float(item.split(":")[1])
                total_temp += value
                count += 1
        avg = total_temp / count if count > 0 else 0.0
        return f"Sensor analysis: {len(batch)} readings processed, avg temp: {avg:.1f}°C"

if __name__ == "__main__":
    batch = ["temp:22.5", "humidity:65", "pressure:1013"]
    print(f"Initializing Sensor Stream...")
    instance = SensorStream("SENSOR_001")
    res = instance.process_batch(batch, False)
    print(res)
