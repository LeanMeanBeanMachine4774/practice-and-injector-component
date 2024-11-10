import magicbot
import wpilib
from components.injector import InjectorComponent


class MyRobot(magicbot.MagicRobot):
    injector: InjectorComponent
    
    def createObjects(self) -> None:
        self.controller = wpilib.XboxController(0)

    def teleopInit(self) -> None:
        pass

    def teleopPeriodic(self) -> None:
        if self.controller.getAButton():
            self.injector.intaking()
            
            


if __name__ == "__main__":
    wpilib.run(MyRobot)
