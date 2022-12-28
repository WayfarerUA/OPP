class Element:
    def __init__(self, tmelt, tboil):
        self.tmelt = tmelt
        self.tboil = tboil

    def agg_state(self, temp, scale):
        temp = self.temp_convert(temp, scale)
        if temp < self.tmelt:
            return "Solid"
        if temp > self.tboil:
            return "gas"
        else:
            return "liquid"


    def temp_convert(self,temp, scale: str = 'C'):
        if scale == "F":
            return (temp-32)*5/9
        if scale == "K":
            return temp - 273.15
        return temp

if __name__ == "__main__":
    iron = Element(1000, 2862)
    neiron = Element(15, 290)
    print(iron)
    print(neiron.agg_state(300, "K"))