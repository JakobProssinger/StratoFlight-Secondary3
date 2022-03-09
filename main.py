"""
@File:          main.py
@Descrption:    runnable file for secodary 3              
@Author:        Prossinger Jakob
@Date:          9 March 2022
@Todo:          
"""
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
    ina_solar_secondary = INA260(
        name="INA260-solar-secondary", address=INA260_SECONDARY_ADDRESS)

    strato_csv_handler = CSV_HANDLER(
        "/home/pi/Documents/StratoFlight-Secondary3/sensor_data/data.csv")

    strato_controller = Controller("seconday3_controller", strato_csv_handler)
    strato_controller.addSensor(ina_solar_primary)
    strato_controller.addSensor(ina_solar_secondary)

    strato_controller.write_csv_header()
    while True:
        strato_controller.reload()
        strato_controller.write_csv_data()
        time.sleep(3)


if __name__ == '__main__':
    main()
