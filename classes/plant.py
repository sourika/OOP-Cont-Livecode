class Plant:
    def __init__(self, name, water_level, sunlight_hours, is_blooming=False):
        self.name = name
        self.water_level = water_level
        self.sunlight_hours = sunlight_hours
        self.is_blooming = is_blooming
    
    def water(self, water_amount):
        self.water_level += water_amount

        return f"{self.name} has been watered: {self.water_level}"
    
    def check_growth_stage(self):
        growth_stage = None

        if self.water_level > 5 and self.sunlight_hours > 5:
            growth_stage = "Mature"
        else:
            growth_stage = "Sprout"
        
        return f"{self.name} is currently at the {growth_stage} stage."
    
    def give_sunglight(self, hours):
        self.sunlight_hours += hours

        return f"{self.name} has received a total of {hours}. New sunlight level: {self.sunlight_hours}"