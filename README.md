# OOP Plant Livecode
This repository is the livecode for the Intro to OOP, Con't roundtable. 

## Instructions
Design a class that models a Plant:

- `Plant` basic information: 
  - `name`: A string representing the name of a plant.
  - `water_level`: The amount of water a plant has received represented by an **integer**.
  - `sunlight_hours`: The total hours of sunlight a plant needs in a day (**integer**).
  - `is_blooming`: A boolean value representing if a plant is blooming, has a default value of **False**.

- Methods of `Plant`:
  - `water`: Takes an **integer** and adds it to `water_level` of a plant.
  - `give_sunlight`: Takes an **integer** and adds it to the `sunlight_hours` of a plant.
  - `check_growth`: Determines a plant's growth stage based on its water level and sunlight hours, categorizing the plant as either "Sprout" or "Mature" based on thresholds: 
    - If the a plant requires more than **5** hours of sunlight **and** has a `water_level` higher than **5** then it is **mature**. Otherwise, it is a **sprout**.

- Write accompanying tests to test the `Plant` class.
