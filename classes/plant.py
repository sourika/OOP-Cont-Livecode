class Plant:
    def __init__(self, name, water_level, origin, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_level
        self.origin = origin
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming
    
    def water(self, water_amount):
        self.water_level += water_amount

        return f"{self.name} has been watered: {self.water_level}"
    
    def check_growth_stage(self):
        growth_stage = None

        if self.water_level > 5 and self.sunlight_hours > 5:
            growth_stage = "Sprout"
        if self.water_level > 10 and self.sunlight_hours > 10:
            growth_stage = "Mature"
        
        return f"{self.name} is currently at the {growth_stage} stage."
    
    def give_sunglight(self, hours):
        self.sunlight_hours += hours

        return f"{self.name} has received a total of {hours}. New sunlight level: {self.sunlight_hours}"
    
    def __repr__(self):
        return f"Plant(name='{self.name}', origin='{self.origin}', water_level={self.water_level}, sunlight_hours={self.sunlight_hours}, is_blooming={self.is_blooming})"

    
