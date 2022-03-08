import smbus
import time
from csv_handler.csv_handler import CSV_HANDLER
from sensor.ina260 import INA260
from controller.controller import Controller

DEVICE_BUS = 1
INA260_PRIMARY_ADDRESS = 0x40
INA260_SECONDARY_ADDRESS = 0x41


def main():
    ina_solar_primary = INA260(
        name="INA260-solar-primary", address=INA260_PRIMARY_ADDRESS)
    ina_solar_primary.activate_average()
    ina_solar_secondary = INA260(
        name="INA260-solar-secondary", address=INA260_SECONDARY_ADDRESS)
    ina_solar_secondary.activate_average()

    strato_csv_handler = csv_handler.csv_handler(
        "C:\Programming\StratoFlight-INA260\data\sensor_data.csv")

    strato_controller = Controller("seconday3_controller", strato_csv_handler)
    strato_controller.addSensor(ina_solar_primary)
    strato_controller.addSensor(ina_solar_secondary)
    while True:

        time.sleep(30)


if __name__ == '__main__':
    main()
