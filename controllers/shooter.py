from magicbot import StateMachine, timed_state, state, default_state, will_reset_to
from components.shooter import ShooterComponent
from components.injector import InjectorComponent


class Shooter(StateMachine):
    shooter: ShooterComponent
    injector: InjectorComponent
    outtake_desire = will_reset_to(False)

    def try_outtake(self) -> None:
        self.outtake_desire = True

    @default_state()
    def flywheel_state(self) -> None:
        if self.injector.has_note:
            self.shooter.spin_up_flywheels()
        else:
            self.shooter.coast_flywheels()
        if self.outtake_desire:
            self.engage()

    @state(first=True, must_finish=True)
    def outtake(self) -> None:
        self.injector.injecting()
        if not self.injector.has_note:
            self.next_state(self.let_note_travel)

    @timed_state(0.5, must_finish=True, next_state="done")
    def let_note_travel(self) -> None:
        pass
