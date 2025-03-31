# OOP Plant Livecode
This repository is the livecode for the Intro to OOP, Con't roundtable. 

## Instructions
A class that models a Plant:

- `Plant` attributes: 
  - `name`: A string representing the name of a plant.
  - `water_level`: The amount of water a plant has received represented by an **integer**.
  - `sunlight_hours`: The total hours of sunlight a plant needs in a day (**integer**).
  - `is_blooming`: A boolean value representing if a plant is blooming, has a default value of **False**.

- Methods of `Plant`:
  - `change_water`: Takes an **integer** and adds it to `water_level` of a plant. Finally, returning the new water level.
  - `change_sunlight`: Takes an **integer** and adds it to the `sunlight_hours` of a plant. Finally, returning the new total amount of sunlight hours.
  - `check_growth`: Determines a plant's growth stage, categorizing the plant as either "Sprout" or "Mature" based on: 
    - If the a plant requires more than **5** hours of sunlight **and** has a water level higher than **5** then it is **mature**.
    - If the plant is blooming, regardless of the water and sunlight levels, it is **mature**
    - Otherwise, it is a **sprout**. 

- Write accompanying tests to test the `Plant` class.
