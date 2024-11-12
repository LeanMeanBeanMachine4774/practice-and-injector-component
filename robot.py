import magicbot
import wpilib
from controllers.injector import Injector
from controllers.shooter import Shooter


class MyRobot(magicbot.MagicRobot):
    injector: Injector
    shooter: Shooter

    def createObjects(self) -> None:
        self.controller = wpilib.XboxController(0)

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        if self.controller.getAButton():
            self.injector.try_intake()
        if self.controller.getRightBumper():
            self.shooter.try_outtake()


if __name__ == "__main__":
    wpilib.run(MyRobot)
