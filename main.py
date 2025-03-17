from SensorPairer import SensorPairer

if __name__ == "__main__":


    csv_file_path1 = 'SensorData1.csv'
    json_file_path = 'SensorData2.json'

    
   
    pairer = SensorPairer(csv_file_path1, json_file_path)
    pairer._pair_sensors(100)
    pairer._generate_paired_sensor_ids_json("solution_output.json")
    