with open(fr'01a-input.txt') as file:
    lines = file.readlines()
    previous_measurement = int(lines[0])
    times_increased = 0
    for line in lines:
        if int(line) > previous_measurement:
            times_increased += 1
        previous_measurement = int(line)

    print(f"Number of times measurement increased: {times_increased}")
