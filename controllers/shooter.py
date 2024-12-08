from magicbot import StateMachine, timed_state, state, default_state, will_reset_to
from components.shooter import ShooterComponent
from components.injector import InjectorComponent


class Shooter(StateMachine):
    shooter_component: ShooterComponent
    injector_component: InjectorComponent
    outtake_desire = will_reset_to(False)

    def try_outtake(self) -> None:
        self.outtake_desire = True

    @default_state
    def flywheel_state(self) -> None:
        if self.injector_component.has_note:
            self.shooter_component.spin_up_flywheels()
        else:
            self.shooter_component.coast_flywheels()
        if self.outtake_desire and self.injector_component.has_note:
            self.engage()

    @state(first=True, must_finish=True)
    def outtake(self) -> None:
        self.injector_component.injecting()
        if not self.injector_component.has_note:
            self.next_state(self.let_note_travel)

    @timed_state(duration=0.5, must_finish=True, next_state="done")
    def let_note_travel(self) -> None:
        pass
