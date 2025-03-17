import json
import csv
import math

class SensorPairer:
    
    def __init__(self, sensor1_info, sensor2_info):
        """
        Initialize with sensor info and parameter2 info.
        """
        self.sensor1_info = sensor1_info
        self.sensor2_info = sensor2_info
        self.paired_sensor_ids = {}

    def _generate_paired_sensor_ids_json(self, file_name):
        """
        Generate a JSON representation of paired sensor IDs and save it to a file.
        
        :param file_name: The name of the file to save the JSON data
        """
        # Open the file for writing
        with open(file_name, mode='w', encoding='utf-8') as file:
            # Use json.dump to write the paired_sensor_ids dictionary as JSON
            json.dump(self.paired_sensor_ids, file, indent=4)
        
    def _pair_sensors(self, threshold):
        """
        
        """
        id_key = "id"
        lat_key = "latitude"
        long_key = "longitude"
        
        #error checking
        if len(self.sensor1_info)<1 or len(self.sensor2_info) < 1:
            return -3
        elif lat_key not in self.sensor1_info[0] or long_key not in self.sensor1_info[0]:
            return -2
        elif lat_key not in self.sensor2_info[0] or long_key not in self.sensor2_info[0]:
            return -1
        
        #pairs the current sensor 1 reading id with the first sensor2 reading id where the distance between points is withing threshold
        for reading1 in self.sensor1_info:
            lat1 = float(reading1[lat_key])  # Convert latitude to float
            long1 = float(reading1[long_key])  # Convert longitude to float
            
            for reading2 in self.sensor2_info:
                

                lat2 = float(reading2[lat_key])  # Convert latitude to float
                long2 = float(reading2[long_key])  # Convert longitude to float
                
                #if distance is within threshold and the sensor 1 id isnt already paired then add new pair
                if self._distance_between_points_in_meters(lat1, long1, lat2, long2) <= threshold:
                    if reading1[id_key] not in self.paired_sensor_ids:
                        self.paired_sensor_ids[int(reading1[id_key])] = int(reading2[id_key])
                    
        return 1

    def _distance_between_points_in_meters(self, latitude1, longitude1, latitude2, longitude2):
        """
        Calculate the distance between two geographic points using the Haversine formula.
        :param latitude1: Latitude of the first point
        :param longitude1: Longitude of the first point
        :param latitude2: Latitude of the second point
        :param longitude2: Longitude of the second point
        :return: Distance in meters
        """
        
        # Haversine formula to calculate the distance between two points
        R = 6371000  # Radius of Earth in meters
        phi1 = math.radians(latitude1)
        phi2 = math.radians(latitude2)
        delta_phi = math.radians(latitude2 - latitude1)
        delta_lambda = math.radians(longitude2 - longitude1)

        a = math.sin(delta_phi / 2) ** 2 + math.cos(phi1) * math.cos(phi2) * math.sin(delta_lambda / 2) ** 2
        c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
        
        return R * c 

    def csv_to_dict(csv_file):
        """
        Convert a CSV file into a list of dictionaries.
        Each row in the CSV will be converted to a dictionary where the keys are the column headers.
        
        :param csv_file: Path to the CSV file
        :return: List of dictionaries representing the CSV data
        """

        with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
            csv_reader = csv.DictReader(file)
            data = [row for row in csv_reader]
            
        return data
    
    import json

    def import_json_to_dict_list(json_file):
        """
        Convert a JSON file into a list of dictionaries.
        
        :param json_file: Path to the JSON file
        :return: List of dictionaries representing the JSON data
        """
        with open(json_file, mode='r', encoding='utf-8') as file:
            data = json.load(file)
            
        return data


if __name__ == "__main__":


    csv_file_path1 = 'SensorData1.csv'
    sensor1Info = SensorPairer.csv_to_dict(csv_file_path1)
    
    json_file_path = 'SensorData2.json'
    sensor2Info = SensorPairer.import_json_to_dict_list(json_file_path)
    
    # Print the resulting list of dictionaries
    var = SensorPairer(sensor1Info, sensor2Info)
    res = var._pair_sensors(100)
    print(var.paired_sensor_ids)
    
    var._generate_paired_sensor_ids_json("test")
