[![GitHub release (latest by date)](https://img.shields.io/github/v/release/Geospatial-AI-DE/geopedestrian-py)](https://pypi.org/project/geopedestrian)
![GitHub License](https://img.shields.io/github/license/Geospatial-AI-DE/geopedestrian-py)
[![Read the Docs](https://img.shields.io/readthedocs/geopedestrian)](https://geopedestrian.readthedocs.io/en/latest)
[![Tweet Me](https://img.shields.io/twitter/url?style=social&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%2Fgeopedestrian-py)](https://twitter.com/intent/tweet?text=Outstanding:&url=https%3A%2F%2Fgithub.com%2FGeospatial-AI-DE%2Fgeopedestrian-py)

# Introduction
Determines which locations are reachable by a pedestrian.

![](https://geospatial-ai.de/wp-content/uploads/2024/07/Walking-Areas-Berlin-Olympiastadium.png)

*Walking areas 5, 10, and 15 minutes for a pedestrian starting at the Olympiastadium in Berlin, Germany.*

## Why is it important?
Solving walking scenarios and determining accessible places and areas for pedestrians is important for several reasons:

1. **Accessibility**:
   It helps identify areas that are easily accessible by foot, which is crucial for people who rely on walking as their primary mode of transportation. This includes people without access to personal vehicles, the elderly, and those with certain disabilities.

2. **Urban Planning**:
   It aids in urban planning and development. Understanding pedestrian accessibility can guide the placement of public facilities, parks, and businesses to ensure they are reachable for as many people as possible.

3. **Health and Environment**:
   Promoting walkability can lead to healthier lifestyles by encouraging physical activity. It also contributes to environmental sustainability by reducing reliance on motor vehicles, thereby decreasing carbon emissions.

4. **Safety**:
   By identifying and improving pedestrian routes, cities can enhance safety for pedestrians, reducing accidents and making the city safer for everyone.

5. **Tourism**:
   For tourists, understanding walkable areas can enhance their experience, allowing them to explore local attractions on foot.
   Location services contribute to making urban regions more livable, sustainable, and enjoyable. They are a vital tool in modern urban planning and development.

## Next steps
Please, check out the [RapidAPI Account Creation and Management Guide](https://docs.rapidapi.com/docs/account-creation-and-settings).

Start with the [Usage](https://geopedestrian.readthedocs.io/en/latest/usage.html) section for further information, including
how to install the Python module.

## 15 Minutes Walking Scenario
To create a 15-minute city, urban planners need to address a variety of place categories to ensure that all essential services and amenities are within easy reach.

![](assets/images/Fifteen%20Minutes%20Walking%20Areas%20-%20Paris.png)

*Walking areas of 5, 10, and 15 minutes for a pedestrian starting at the center in Paris, France.*

We want to analyze walking to nearby museums within about 15 minutes. 
Every museum within the 15-minute walking area is a potential candidate. 
The analysis result is a 150-meter spatial grid where each cell contains at least one museum.

![](assets/images/Fifteen%20Minutes%20Walking%20Grid%20-%20Paris.png)

*Spatial grid showing areas containing museums that are accessible within about 15 minutes starting at the center in Paris, France.*

A more realistic scenario involves treating the museums as facilities and calculating every possible route. 
The result narrows down the museums being accessible by following the solved routes.

![](assets/images/Fifteen%20Minutes%20Walking%20Places%20-%20Paris.png)

*Museums being accesible within about 15 minutes starting at the center in Paris, France.*

![](assets/images/Fifteen%20Minutes%20Walking%20Routes%20-%20Paris.png)

*Walking routes to museums for a pedestrian starting at the center in Paris, France.*

| name | total_minutes | total_kilometers |
-------|---------------|------------------|
| Fondation Henri Cartier-Bresson | 2 | 0.1 |
| Passage de Retz | 4 | 0.4 |
| Musée de la Chasse et de la Nature  | 5 | 0.4 |
| Musée Picasso | 7 | 0.5 |
| Musée de l'Histoire de France | 7 | 0.6 |

