from classes.plant import Plant

def test_plant_initialization():

    name = "Orchid"
    water_level = 3
    sunlight_hours = 1
    is_blooming = True

    plant = Plant(
        name,
        water_level,
        sunlight_hours,
        is_blooming
    )
     
    assert plant.name == name 
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming is True


def test_plant_initialization_default_is_blooming():

    name = "Lily"
    water_level = 4
    sunlight_hours = 5

    plant = Plant(
        name,
        water_level,
        sunlight_hours
    )
     
    assert plant.name == name 
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming is False    


def test_change_water_level_increses_water_level():
    plant = Plant("Jasmine", 3, 4)

    result = plant.change_water(3)

    assert result == 4
    assert plant.water_level == 8


def test_check_water_six():

    name = "Basil"
    water_level = 6
    sunlight_hours = 6
    

    plant = Plant(
        name,
        water_level,
        sunlight_hours
        )
    
    result = plant.check_growth()

    assert result == "Basil's growth stage: Mature"   