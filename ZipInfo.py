class ZipInfo:
    def __init__(self, zip, city, state, lat, lon):
        self._zip = int(zip)
        self._city = city
        self._state = state
        self._lat = float(lat)
        self._lon = float(lon)

    def get_zip_code(self):
            return self._zip
    def get_city(self):
            return self._city
    def get_state(self):
            return self._state
    def get_lat(self):
        return self._lat
    def get_lon(self):
        return self._lon

    def set_zip_code(self, new_zip):
        self._zip = new_zip
    def set_city(self, new_city):
        self._city = new_city
    def set_state(self, new_state):
        self._state = new_state
    def set_lat(self, new_lat):
        self._lat = new_lat
    def set_lon(self, new_lon):
        self._lon = new_lon

    def __str__(self):
        return (f"{self._city}, {self._state} {self._zip}")


if __name__ == "__main__":
    allendale = ZipInfo(49401, 'Allendale', 'MI', 42.9711, -85.9249)
    print(allendale.get_city())
    #allendale.set_state('MO')
    #allendale.set_zip_code(64420)
    print(allendale)


