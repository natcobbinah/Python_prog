def car_make(manufacturer, model_name, **car_info):
    car_info['manufacturer'] = manufacturer
    car_info['model_name'] = model_name
    return car_info

car_data = car_make('subaru','outback', color='blue', tow_package=True)
print(car_data)

