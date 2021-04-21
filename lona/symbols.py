from lona.types import Symbol


class VIEW_RUNTIME_STATE(Symbol):
    NOT_STARTED = Symbol('NOT_STARTED', 10)

    RUNNING = Symbol('RUNNING', 21)
    WAITING_FOR_IOLOOP = Symbol('WAITING_FOR_IOLOOP', 22)
    SLEEPING = Symbol('SLEEPING', 23)
    WAITING_FOR_INPUT = Symbol('WAITING_FOR_INPUT', 24)

    FINISHED = Symbol('FINISHED', 31)
    CRASHED = Symbol('CRASHED', 32)
    STOPPED_BY_USER = Symbol('STOPPED_BY_USER', 33)
    STOPPED_BY_SERVER = Symbol('STOPPED_BY_SERVER', 34)