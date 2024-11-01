import magicbot
import wpilib


class MyRobot(magicbot.MagicRobot):
    def createObjects(self) -> None:
        self.controller = wpilib.XboxController(0)

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        pass


if __name__ == "__main__":
    wpilib.run(MyRobot)
