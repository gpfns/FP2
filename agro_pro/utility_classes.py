
class Current:

    def __init__(self, current_data):
        self.c = current_data

    def get_air_quality(self):
        s1 = ""
        s1 += 'CO : ' + self.aq['co']
        s1 += 'NO2 : ' + self.aq['no2']
        s1 += 'O3 : ' + self.aq['o3']
        s1 += 'SO2 : ' + self.aq['so2']

        return s1

    def get_temp(self):
        return self.c['temp_c']

    def get_last_updated(self):
        return self.c['last_updated']

    def get_condition(self):
        return self.c['condition']['text']

    def get_wind_kph(self):
        return self.c['wind_kph']

    def get_wind_dir(self):
        return self.c['wind_dir']

    def get_cloud(self):
        return self.c['cloud']

    def get_humid(self):
        return self.c['humidity']
