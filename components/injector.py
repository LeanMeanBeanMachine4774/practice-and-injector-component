from rev import CANSparkMax
from wpilib import DigitalInput


class InjectorComponent:
    def __init__(self) -> None:
        self.injectormotor = CANSparkMax(1, CANSparkMax.MotorType.kBrushless)
        self.desired_injector_speed = 0.0
        CANSparkMax.setInverted(self.injectormotor, False)
        self.breakbeam = DigitalInput(2)

    def intaking(self) -> None:
        self.desired_injector_speed = 0.5

    def execute(self) -> None:
        self.injectormotor.set(self.desired_injector_speed)
        if not self.breakbeam.get():
            self.desired_injector_speed = 0.0
