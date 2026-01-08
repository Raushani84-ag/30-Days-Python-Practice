def classify_sensor_readings(sensor_data , max_irradiance ):
    valid =[]
    invalid = []
    suspicious = []
    missing = []
    
    def value_check(sensor_data):
        if not isinstance(sensor_data, list):
            raise TypeError("sensor data must be a list")
            
    def sensor_data_classification(sensor_data, max_irradiance):
        
        for data in sensor_data:
            if data is None:
                missing.append(data)
            elif data < 0:
                invalid.append(data)
            elif data > max_irradiance:
                suspicious.append(data)
            else:
                valid.append(data)
        
                
        sensor_data_classifications = {
        'valid':valid,
        'invalid' : invalid,
        'suspicious' : suspicious,
        'missing': missing }
        return sensor_data_classifications

    def summary(sensor_data):
        summary =  {'total data' :len(sensor_data),
                   'valid data':len(valid),
                    'invalid data' : len(invalid),
                   'suspicious data' : len(suspicious),
                   'missing data' : len(missing)}
        return summary 
        
    data = sensor_data_classification( sensor_data ,max_irradiance)
    get_summary = summary(sensor_data)

    output = {'data' : data,
             'summary': get_summary }

    return output 
      
solar_irradiance_readings = [800 , 670 , -780, -200,None,  0, 1800, 670, None, 900, 1000,-560, 5000, 1600, 230]
classify_sensor_readings(sensor_data =solar_irradiance_readings , max_irradiance = 1100)
           
