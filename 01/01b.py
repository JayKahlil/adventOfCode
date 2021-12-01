with open(fr'01a-input.txt') as file:
    lines = file.readlines()
    previous_measurement = int(lines[0]) + int(lines[1]) + int(lines[2])
    times_increased = 0
    for index, value in enumerate(lines):
        if len(lines) > index + 2:
            current_measurement = int(lines[index]) + int(lines[index + 1]) + int(lines[index + 2])

            if current_measurement > previous_measurement:
                times_increased += 1
            previous_measurement = current_measurement

    print(f"Number of times measurement increased: {times_increased}")
