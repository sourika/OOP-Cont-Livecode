from classes.plant import Plant

def test_plant_class_instantiation():
    # Arrange
    name = "Fern"
    water_level = 4
    sunlight_hours = 5
    is_blooming = False

    # Act
    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == False

def test_plant_class_instantiation_default_is_blooming():
    # Arrange
    name = "Orchid"
    water_level = 4
    sunlight_hours = 5

    # Act
    plant = Plant(
       name,
       water_level,
       sunlight_hours,
    )

    # Assert
    assert plant.name == name
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert plant.is_blooming == False

def test_change_water_increases_water_level():
    # Arrange
    name = "Oxalis"
    water_level = 2
    sunlight_hours = 7
    is_blooming = True

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Act
    result = plant.change_water(3)

    # Assert
    assert result == 5
    assert plant.water_level == 5

def test_change_water_decreases_water_level():
    # Arrange
    name = "Oxalis"
    water_level = 2
    sunlight_hours = 7
    is_blooming = True

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Act
    result = plant.change_water(-1)

    # Assert
    assert result == 1
    assert plant.water_level == 1

def test_change_sunlight_increases_decreases_sunlight_hours():
    # Arrange
    name = "Air Plant"
    water_level = 2
    sunlight_hours = 6

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
    )

    # Act
    plant.change_sunlight(2)
    result = plant.change_sunlight(-3)

    # Assert
    assert result == 5
    assert plant.sunlight_hours == 5

def test_check_growth_water_sunlight_under_five():
    # Arrange
    name = "Money Tree"
    water_level = 2
    sunlight_hours = 3
    is_blooming = False

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Act
    result = plant.check_growth()

    # Assert
    assert result == "Money Tree's growth stage: Sprout"
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours 

def test_check_growth_water_sunlight_over_five():
    # Arrange
    name = "Purple Trumpet"
    water_level = 8
    sunlight_hours = 6
    is_blooming = False

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Act
    result = plant.check_growth()

    # Assert
    assert result == "Purple Trumpet's growth stage: Mature"
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
    assert not plant.is_blooming  

def test_check_growth_plant_is_blooming():
    # Arrange
    name = "Money Tree"
    water_level = 2
    sunlight_hours = 6
    is_blooming = True

    plant = Plant(
       name,
       water_level,
       sunlight_hours,
       is_blooming
    )

    # Act
    result = plant.check_growth()

    # Assert
    assert result == "Money Tree's growth stage: Mature"
    assert plant.water_level == water_level
    assert plant.sunlight_hours == sunlight_hours
