class Solution:
    def convertTemperature(self, celsius: float) -> list[float]:
        result=[]
        kelvin=celsius+273.15
        f=celsius*1.80+32.00
        result.append(kelvin)
        result.append(f)
        return result