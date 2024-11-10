from magicbot import StateMachine
from components.shooter import ShooterComponent
from components.injector import InjectorComponent


class Injector(StateMachine):
    shooter: ShooterComponent
    injector: InjectorComponent
