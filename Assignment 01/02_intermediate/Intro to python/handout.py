def main():
    # Prompt the user to enter their weight on Earth
    earth_weight = float(input("Enter a weight on Earth: "))
    
    # Prompt the user to enter the name of a planet
    planet = input("Enter a planet: ")

    # Dictionary of gravitational constants for each planet (as a multiplier)
    gravity_multipliers = {
        "Mercury": 0.376,
        "Venus": 0.889,
        "Mars": 0.378,
        "Jupiter": 2.36,
        "Saturn": 1.081,
        "Uranus": 0.815,
        "Neptune": 1.14
    }

    # Calculate the weight on the given planet
    if planet in gravity_multipliers:
        planet_weight = earth_weight * gravity_multipliers[planet]
        planet_weight = round(planet_weight, 2)
        print(f"The equivalent weight on {planet}: {planet_weight}")
    else:
        print("Invalid planet name.")

if __name__ == "__main__":
    main()
