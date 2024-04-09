from data.sensor import create_sensor


def create_sensor_handler(session, payload):
    # do sensor validdation
    # if not validate_project(payload.project_id):
    #     raise Exception("Invalid sensor id")

    return create_sensor(session, payload)


# def validate_project(sensor_id: int) -> bool:
#     # verify sensor_id
#     return True
