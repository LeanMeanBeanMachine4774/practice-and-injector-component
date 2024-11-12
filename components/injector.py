from rev import CANSparkMax
from wpilib import DigitalInput


class InjectorComponent:
    def __init__(self) -> None:
        self.injectormotor = CANSparkMax(1, CANSparkMax.MotorType.kBrushless)
        CANSparkMax.setInverted(self.injectormotor, False)
        self.injectormotor.setIdleMode(CANSparkMax.IdleMode.kBrake)
        self.desired_injector_speed = 0.0
        self.breakbeam = DigitalInput(2)

    def has_note(self) -> bool:
        return not self.breakbeam.get()

    def intaking(self) -> None:
        if self.has_note:
            self.desired_injector_speed = 0.0
        else:
            self.desired_injector_speed = 0.5

    def injecting(self) -> None:
        if self.has_note:
            self.desired_injector_speed = 1.0
        else:
            self.desired_injector_speed = 0.0

    def execute(self) -> None:
        self.injectormotor.set(self.desired_injector_speed)
