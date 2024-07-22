def add_farm(farm_list):
    name=input('Enter the name: ')
    location=input('Enter the location: ')
    acres=input('Enter the acres: ')
    farm = {
        'name': name,
        'location': location,
        'acres': acres
    }
    farm_list.append(farm)
    print(f"Farm '{name}' added successfully.")

def update_farm(farm_list, name, location=None, acres=None):
    for farm in farm_list:
        if farm['name'] == name:
            if location:
                farm['location'] = location
            if acres:
                farm['acres'] = acres
            print(f"Details of farm '{name}' updated successfully.")
            return
    print(f"Farm '{name}' not found.")

def list_farms(farm_list):
    if not farm_list:
        print("No farms in the list.")
    else:
        for farm in farm_list:
            print(f"Name: {farm['name']}, Location: {farm['location']}, Acres: {farm['acres']} acres")
