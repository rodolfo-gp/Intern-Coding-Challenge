# CUAVs-Coding-Challenge

Challenge Overview:

At Canadian UAVs, we handle large amounts of geospatial data, which is the focus of this challenge. The task involves correlating data from two sensors that detect anomalies. However, the sensors are not highly accurate, resulting in false positives and variations in their location readings. Your challenge is to associate the sensor readings based on their coordinates to identify common signals that may have been detected by both sensors. This correlation increases the likelihood that the signal is a genuine detection rather than a false positive.

Input Data:

The two sensors provide different output formats: one sensor outputs data in CSV format, and the other outputs data in JSON format. Please refer to the sample data for the exact format of each sensor's output. Both sensors assign a unique ID to each reading, but note that different sensors may use the same IDs. The sensor readings include location coordinates in decimal degrees, using the WGS 84 format, representing where the anomaly was detected. The sensors have an accuracy of 100 meters, meaning that the reported location is within 100 meters of the actual anomaly location.

Output:

The output should consist of pairs of IDs, where one ID is from the first sensor, and the second ID is from the second sensor.

# CUAVs-Coding-Solution

## Solution Overview

The solution takes in two input files processes the data, calculates the distance between points using the Haversine formula, and outputs pairs of sensor readings that are within the specified threshold (100 meters).

## Class Explanation: `SensorPairer`

The core of the solution is the `SensorPairer` class, which performs the task of correlating the sensor data.

### `__init__(self, sensor1_csv_file, sensor2_json_file)`

The constructor accepts two file paths:
- `sensor1_csv_file`: The path to the CSV file containing sensor data from the first sensor.
- `sensor2_json_file`: The path to the JSON file containing sensor data from the second sensor.

It processes both files into Python data structures (dictionaries) using helper methods and initializes an empty dictionary `paired_sensor_ids` to store the paired IDs.

### `_generate_paired_sensor_ids_json(self, file_name)`

This method generates a JSON file containing the paired sensor IDs. It writes the dictionary `paired_sensor_ids` to a file with the specified `file_name`.

### `_pair_sensors(self, threshold)`

This method performs the core functionality:
- It pairs readings from the two sensors if the distance between their coordinates is less than or equal to the given `threshold` (100 meters).
- It checks if the latitude and longitude keys are present in the sensor data and handles errors accordingly.
- It uses the Haversine formula to calculate the distance between two points on the Earth's surface.

### `_distance_between_points_in_meters(self, latitude1, longitude1, latitude2, longitude2)`

This method calculates the distance between two geographic points using the Haversine formula. It takes the latitude and longitude of two points and returns the distance in meters.

### Helper Methods:

- `__csv_to_dict(self, csv_file)`: Converts a CSV file to a list of dictionaries, where each row is a dictionary with the column headers as keys.
- `__import_json_to_dict_list(self, json_file)`: Converts a JSON file to a list of dictionaries.

## Solution Output

After processing the sensor data, the solution generates a `solution_output.json` file containing pairs of sensor IDs that correspond to the same anomaly detection based on proximity. The output is in the following format:

```json
{
    "sensor1_id_1": "sensor2_id_1",
    "sensor1_id_2": "sensor2_id_2",
}

```