print "main.py run"

@hook.enable
def onenable():
    print "Plugin enabled . by SuperBaronDEV"

@hook.disable
def ondisable():
    print "Plugin disabled . by SuperBaronDEV"

@hook.command
def example(sender, command, label, args):
    sender.sendMessage("you just used command /example!")
