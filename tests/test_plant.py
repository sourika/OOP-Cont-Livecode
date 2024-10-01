from classes.plant import Plant

def test_plant_initialization():
    # Act
    plant_rose = Plant(name="Rose", water_level=5, sunlight_hours=6, is_blooming=True)
    plant_cactus = Plant(name="Cactus", water_level=1, sunlight_hours=12)

    # Assert
    assert plant_rose.name == "Rose"
    assert plant_rose.water_level == 5
    assert plant_rose.sunlight_hours == 6
    assert plant_rose.is_blooming == True

    assert plant_cactus.name == "Cactus"
    assert plant_cactus.water_level == 1
    assert plant_cactus.sunlight_hours == 12
    assert plant_cactus.is_blooming == False


def test_plant_watering():
    # Arrange
    plant_bamboo = Plant(name="Bamboo", water_level=4, sunlight_hours=6)

    # Act
    result_bamboo = plant_bamboo.water(3)

    # Assert
    assert plant_bamboo.water_level == 7
    assert result_bamboo == "Bamboo has been watered: 7"

def test_plant_sunlight():
    # Arrange
    plant_sunflower = Plant(name="Sunflower", water_level=5, sunlight_hours=8)

    # Act
    result_sunflower = plant_sunflower.give_sunglight(4)

    # Assert
    assert plant_sunflower.sunlight_hours == 12
    assert result_sunflower == "Sunflower has received a total of 4. New sunlight level: 12"

def test_plant_growth_stage():
    # Arrange
    plant_cactus = Plant(name="Cactus", water_level=12, sunlight_hours=15)

    # Act
    result_cactus = plant_cactus.check_growth_stage()

    # Assert
    assert result_cactus == "Cactus is currently at the Mature stage."
