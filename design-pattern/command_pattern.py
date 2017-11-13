"""
from
https://en.wikipedia.org/wiki/Command_pattern#Python
"""
# invoker, command, receiver, client


class Switch:
    """invoker"""
    def __init__(self):
        self._history = ()

    @property
    def history(self):
        return self._history

    def execute(self, command):
        self._history += (command,)
        command.execute()


class Command:
    """Command interface"""
    def __init__(self, obj):
        self._obj = obj

    def execute(self):
        raise NotImplementedError


class TurnOnCommand(Command):

    def execute(self):
        self._obj.turn_on()


class TurnOffCommand(Command):

    def execute(self):
        self._obj.turn_off()


class Light:

    def turn_on(self):
        print('light on')

    def turn_off(self):
        print('light off')


class LightSwitchRemote:

    def __init__(self):
        self._lamp = Light()
        self._switch= Switch()

    @property
    def history(self):
        return self._switch.history

    def pressed(self, cmd):
        cmd = cmd.strip().upper()

        if cmd == 'ON':
            self._switch.execute(TurnOnCommand(self._lamp))
        elif cmd == 'OFF':
            self._switch.execute(TurnOffCommand(self._lamp))
        else:
            print('on or off')


remote = LightSwitchRemote()
remote.pressed('on')
remote.pressed('off')
remote.pressed('offsfadsfsaf')
remote.pressed('on')
print(remote.history)



