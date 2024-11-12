from magicbot import StateMachine, state
from components.injector import InjectorComponent


class Injector(StateMachine):
    injector_component: InjectorComponent

    def try_intake(self) -> None:
        self.engage()

    @state(first=True, must_finish=True)
    def intaking(self) -> None:
        self.injector_component.intaking()
        if self.injector_component.has_note():
            self.done()
