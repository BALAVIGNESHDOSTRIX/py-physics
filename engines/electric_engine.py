from .exceptions import ElecticEngineException
from typing import *


class ElectricEngine(object):

    @staticmethod
    def get_battery_life(capacity_in_ah: float | int = 1, load_in_a: float | int = 1) -> int | float:
        return capacity_in_ah / load_in_a

    @staticmethod
    def calculate_watts(voltage: float | int = 1, amp_in_hr: float | int = 1) -> int | float:
        return voltage * amp_in_hr

    @staticmethod
    def calculate_amp(watts: float | int = 1, voltage: float | int = 1) -> int | float:
        return watts / voltage

    @staticmethod
    def calculate_voltage(watts: float | int = 1, amp: float | int = 1) -> float | int:
        return watts / amp

    @staticmethod
    def calculate_mah_to_ah(mah: int = 1000) -> int:
        return mah // 1000

    @staticmethod
    def get_battery_out_report(cell_count: int = 1, voltage: float | int = 1, mah: int = 1000,
                               con_type: str = 'serial') -> Tuple[float, int]:
        if con_type not in ('serial', 'parallel'):
            raise ElecticEngineException('Please give the connection type as serial or parallel')

        amp = ElectricEngine.calculate_mah_to_ah(mah)

        if con_type == 'serial':
            voltage = voltage * cell_count
        else:
            amp = amp * cell_count

        return voltage, amp
