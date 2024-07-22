def add_crop(listname):
    name=input('Enter the plant name: ')
    sci_name=input('Enter the sci_name: ')
    planting_date=input('Enter the planting_date: ')
    expected_harvest_date=input('Enter the expected_harvest_date: ')
    
    crop = {
        'name': name,
        'sci_name': sci_name,
        'planting_date': planting_date,
        'expected_harvest_date': expected_harvest_date
    }
    
    listname.append(crop)
    print(f"Crop '{name}' added successfully.")
    

def update_crop(listname):
    name=input('Enter the plant name: ')
    harvest_status=input('Enter the harvest_status: ')
    actual_harvest_date=input('Enter the actual_harvest_date: ')
    yield_amount=input('Enter the yield_amount: ')
    crop_up={
             'name':name,
             'harvest_status':harvest_status,
             'actual_harvest_date':actual_harvest_date,
             'yield_amount':yield_amount 
            }
    listname.append(crop_up)
    print(f"Details of crop '{name}' updated successfully.")
    
def remove_crop(listname, name):
        for crop in listname:
            if crop['name'] == name:
                listname.remove(crop)
                print(f"Crop '{name}' removed successfully.")
            print(f"Crop '{name}' not found.")