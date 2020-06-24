def car_info(model,company,*color):
    """display the car information"""
    info = {"model":model,"company":company,"color":color}
    print(f"\n info: {info}")
    return info
car = car_info("BMW X6","BMW","Black","feature= Max Speed")
car = car_info("ecosport","ford","white","feature= best sensors")
