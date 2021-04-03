from math import radians, sin, cos, asin, sqrt


class Points:
    """

    A class used to store latitude and longitude of a place as an object.

    ...

    Parameters
    ----------

    @:param: latitude - str
        A string which consists of latitude.
    @:param: longitude - str
        A string which consists of longitude.

    Methods
    -------

    split_string(str)
        Extracts and Returns the point in the input string.

    to_float(point)
        Casts the input to float and returns

    to_radians(point)
        Casts the input to radians and returns
    """

    def __init__(self, latitude, longitude):
        str_latitude = self.split_string(latitude)
        str_longitude = self.split_string(longitude)

        float_latitude = self.to_float(str_latitude)
        float_longitude = self.to_float(str_longitude)

        self.latitude = radians(float_latitude)
        self.longitude = radians(float_longitude)

    def split_string(self, str_point):
        str_point = str_point.split()

        if str_point[1] in {'W', 'S'}:
            str_point[0] = "-" + str_point[0]

        return str_point[0]

    def to_float(self, point):
        return float(point)

    def to_radians(self, point):
        return radians(point)


class Distance:
    """

    A class used to calculate distance between two points.

    ...

    Parameters
    ----------

    @:param: source - Point
        A Point instance which consists of latitude and longitude of source.
    @:param: destination - Point
        A Point instance which consists of latitude and longitude of destination.

    Methods
    -------

    calculate_distance()
        Calculates and prints the distance between two points.

    haversine(theta)
        Calculates and returns the squared sine(theta).

    """

    def __init__(self, source, destination):
        self.source = source
        self.destination = destination

    def calculate_distance(self, ):
        # Haversine formula
        # h = hav(lat of point 2 - lat of point 1) +
        # cos(lat of point 1)*cos(lat of point 2)*hav(lon of point 2 - lon of point 1)

        # distance = 2 * r * inverse_sine(sqrt(h))

        diff_lon = self.destination.longitude - self.source.longitude
        diff_lat = self.destination.latitude - self.source.latitude

        h = (self.haversine(diff_lat)) + (
                cos(self.source.latitude) * cos(self.destination.latitude) * self.haversine(diff_lon))

        # Radius of earth in kilometers. Use 3956 for miles
        r = 6371.00

        distance = 2 * r * (asin(sqrt(h)))

        print("City 1 and City 2 are  is %.2f km apart" % distance)

    def haversine(self, theta):
        return sin(theta / 2) ** 2


if __name__ == "__main__":
    source_latitude, source_longitude = input("City 1: ").split(",")
    dest_latitude, dest_longitude = input("City 2: ").split(",")

    source = Points(source_latitude, source_longitude)
    destination = Points(dest_latitude, dest_longitude)

    dist = Distance(source, destination)
    dist.calculate_distance()
