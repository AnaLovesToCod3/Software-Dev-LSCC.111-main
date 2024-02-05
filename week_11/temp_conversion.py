unit_conversions = {
    "K": {"C": lambda x: x - 273.15, "F": lambda x: (x - 273.15) * 9/5 + 32},
    "C": {"K": lambda x: x + 273.15, "F": lambda x: x * 9/5 + 32},
    "F": {"K": lambda x: (x - 32) * 5/9 + 273.15, "C": lambda x: (x - 32) * 5/9}
}

while True:
    try:
        value = float(input("temperature value: "))
        from_unit = input("from unit (K, C, or F): ").upper()
        to_unit = input("to unit (K, C, or F): ").upper()


        if from_unit not in ("K", "C", "F") or to_unit not in ("K", "C", "F"):
            raise ValueError("invalid unit. Please use K, C, or F.")

        #i know im being extra but you gotta check if the units are the same

        if from_unit == to_unit:
            print(f"{value}{from_unit} is {value}{to_unit}... girl think")
            continue

        conversion_func = unit_conversions[from_unit][to_unit]
        converted_value = conversion_func(value)
        print(f"value of {value}{from_unit} is {converted_value:.2f}{to_unit}")
        break

    except ValueError as e:
        print(f"Error: {e}")
        print("please enter valid units (K, C, or F) and a numerical value.")

print("tadah!")

