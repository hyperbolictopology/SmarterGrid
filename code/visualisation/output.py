from code.classes import district
import json


def generate_json(district):
    data = []
    data.append({"district": district.district_number, "costs-shared": district.shared_cost})

    for battery in district.batteries:
        data.append({"location": battery.location, "capacity": battery.max_capacity, "houses": []})

        for house in district.houses:

            # Only adding houses to the list if they lead to that battery.
            # The last coordinate of the cable should equal the battery position
            if house.cables.cable_segments[-1][-1] == (battery.pos_x, battery.pos_y):
                data[-1]["houses"].append({"location": house.location, "output": house.output, "cables": house.cables.get_route_list_string()})

    json_output = json.dumps(data, indent = 2)
    with open("output.json", "w") as file:
        file.write(json_output)

    return json_output
