class bil():

    def __init__(self, motor, seter, farge, speed, max_speed, størrelse, drivstoff, dimensjon_bil, konsum, distance_vision):
        self.motor = motor
        self.seter = seter
        self.farge = farge
        self.speed = speed
        self.max_speed = max_speed
        self.realmaxspeed = self.max_speed
        self.størrelse = størrelse
        self.drivstoff = drivstoff
        self.dimensjon_bil = dimensjon_bil
        self.konsum = konsum
        self.distance_vision = distance_vision
        self.realvision = self.distance_vision
        self.realwvision = self.realvision
        self.weather = "clear"
        self.light = 100
        self.valid_conditions = ("clear", "rain", "iceandsnow", "fog", "fogsnowandice")

    def detaljer(self):
        return "Motor: " + str(self.motor) + ", Seter: " + str(self.seter) + ", Farge: " + str(self.seter) + ", Hastighet: " + str(self.speed) + ", Maks hastighet: " + str(self.max_speed) + ", Størrelse: " + str(self.størrelse) + ", Drivstoff: " + str(self.drivstoff) + ", Dimensjon: " + str(self.dimensjon_bil) + ", Konsum: " + str(self.konsum) + ", Visjon (m): " + str(self.distance_vision)

    def weather_condition(self, weather):
        if weather in self.valid_conditions:
            if weather == "clear" and self.weather != "clear":
                self.max_speed = self.realmaxspeed
                self.distance_vision = self.realvision
            if weather == "rain" and self.weather != "rain":
                self.max_speed = self.realmaxspeed * 0.90
                self.distance_vision = self.realvision
            if weather == "iceandsnow" and self.weather != "iceandsnow":
                self.max_speed = self.realmaxspeed * 0.5
                self.distance_vision = self.realvision * 0.8
            if weather == "fog" and self.weather != "fog":
                self.max_speed = self.realmaxspeed * 0.75
                self.distance_vision = self.realvision * 0.6
            if weather == "fogsnowandice" and self.weather != "fogsnowandice":
                self.max_speed = self.realmaxspeed * 0.2
                self.distance_vision = self.realvision * 0.15
            self.realwvision = self.distance_vision
            self.distance_vision = self.distance_vision * (self.light / 100)

    def daylight(self, light):
        self.light = light
        if light > 100:
            self.light = 100
        if light < 1:
            self.light = 1
        self.distance_vision = self.realwvision * (self.light / 100)
            
