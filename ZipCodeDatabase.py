'''
Braxton Wyman
This is a code that can take in things like zip codes, city names, and states and do list with them like
check how many zip codes are in a certain radius, check distances between places, an dfind the furthest place
from a zip code
I certify that this code is mine, and mine alone, in accordance with
GVSU academic honesty policy.
4/13/25
'''

from ZipInfo import ZipInfo
import math


class ZipCodeDatabase:
    """A class to store and manage zip code information."""

    def __init__(self):
        """Initialize an empty zip code dictionary."""
        self._ZipDict = {}

    def add_zip_info(self, zipInfoObject):
        """Add a ZipInfo object to the dictionary."""
        self._ZipDict[zipInfoObject._zip] = zipInfoObject

    def import_data(self, filename):
        """Read zip code data from a file and populate the dictionary."""
        with open(filename, 'r') as f:
            # Loop over each line in the file
            for line in f:
                line = line.strip()
                zip, city, state, lat, lon = line.split(',')
                zip_info = ZipInfo(zip, city, state, float(lat), float(lon))
                self.add_zip_info(zip_info)

    def get_count(self):
        """Return the number of zip codes in the dictionary."""
        return len(self._ZipDict)

    def find_zip_info(self, zipcode):
        """Return the ZipInfo object for a given zip code."""

        # Check if the zip code exists in the dictionary
        if zipcode in self._ZipDict:
            return self._ZipDict[zipcode]
        else:
            return None

    def distance_between(self, zipcode1, zipcode2):
        """Calculate and return the distance between two zip codes."""

        zip1_info = self.find_zip_info(zipcode1)
        zip2_info = self.find_zip_info(zipcode2)

        # Check if either zip code was not found
        if zip1_info is None or zip2_info is None:
            return -1

        radius = 3959.0  # Radius of the Earth in miles

        # Convert latitude and longitude to radians
        lat1 = math.radians(zip1_info._lat)
        lon1 = math.radians(zip1_info._lon)
        lat2 = math.radians(zip2_info._lat)
        lon2 = math.radians(zip2_info._lon)

        # Calculate components for the spherical law of cosines formula
        p1 = math.cos(lat1) * math.cos(lon1) * math.cos(lat2) * math.cos(lon2)
        p2 = math.cos(lat1) * math.sin(lon1) * math.cos(lat2) * math.sin(lon2)
        p3 = math.sin(lat1) * math.sin(lat2)

        # Calculate the distance
        distance = math.acos(p1 + p2 + p3) * radius
        return round(distance)

    def within_radius(self, zipcode, radius):
        """Find and return zip codes within a given radius."""

        center_zip = self.find_zip_info(zipcode)
        if center_zip is None:
            return []

        result = []

        # Loop over all zip codes in the dictionary
        for zip_code, zip_info in self._ZipDict.items():
            # Skip the starting zip code itself
            if zip_code != zipcode:
                distance = self.distance_between(zipcode, zip_code)

                # Check if the distance is within the specified radius
                if distance <= radius:
                    result.append(zip_info)
        return result

    def find_furthest_away(self, zipcode):
        """Find the furthest zip code from the given zip code."""

        start_zip = self.find_zip_info(zipcode)
        if start_zip is None:
            return None

        max_distance = -1
        furthest_zip = None

        # Loop over all zip codes in the dictionary
        for zip_code, zip_info in self._ZipDict.items():
            # Skip the starting zip code itself
            if zip_code != zipcode:
                distance = self.distance_between(zipcode, zip_code)

                # Update the furthest distance if this one is greater
                if distance > max_distance:
                    max_distance = distance
                    furthest_zip = zip_info
        return furthest_zip

    def search_city(self, substr):
        """Search for zip codes where the city name contains a substring."""

        substr = substr.upper()
        result = []

        # Loop over all zip codes in the dictionary
        for zip_info in self._ZipDict.values():
            # Check if the substring exists in the city name
            if substr in zip_info._city.upper():
                result.append(zip_info)
        return result

    def search_state(self, state):
        """Search for zip codes in a specific state."""

        state = state.upper()
        result = []

        # Loop over all zip codes in the dictionary
        for zip_info in self._ZipDict.values():
            # Check if the state matches the requested state
            if zip_info._state.upper() == state:
                result.append(zip_info)
        return result

    def find_extreme_location(self, direction):
        """Find the zip code in the extreme cardinal direction."""

        # Validate the direction input
        if direction.lower() not in ['n', 'north', 's', 'south', 'e', 'east', 'w', 'west']:
            return None

        extreme_zip = None

        # Loop over all zip codes in the dictionary
        for zip_info in self._ZipDict.values():
            if extreme_zip is None:
                extreme_zip = zip_info
            else:
                # Check for the northmost zip code
                if direction.lower() in ['n', 'north']:
                    if zip_info._lat > extreme_zip._lat:
                        extreme_zip = zip_info

                # Check for the southmost zip code
                elif direction.lower() in ['s', 'south']:
                    if zip_info._lat < extreme_zip._lat:
                        extreme_zip = zip_info

                # Check for the eastmost zip code
                elif direction.lower() in ['e', 'east']:
                    if zip_info._lon > extreme_zip._lon:
                        extreme_zip = zip_info

                # Check for the westmost zip code
                elif direction.lower() in ['w', 'west']:
                    if zip_info._lon < extreme_zip._lon:
                        extreme_zip = zip_info

        return extreme_zip