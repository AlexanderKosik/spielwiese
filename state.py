# The state machine
#
# states:
READY = 0
WAITING = 1
ERROR = 2

# events:
PING = 0
PONG = 1
TIMEOUT = 2
RETRY = 3


fsm = [ 
        { PING: WAITING, PONG: ERROR, TIMEOUT: ERROR, RETRY: ERROR }, # READY state
        { PING: ERROR, PONG: READY, TIMEOUT: ERROR, RETRY: ERROR },   # WAITING state
        { PING: ERROR, PONG: READY, TIMEOUT: ERROR, RETRY: WAITING }, # ERROR state
      ]

event_translation = {
    "ping": 0,
    "pong": 1,
    "timeout": 2,
    "retry": 3,
    }

def print_state(state: int):
    if state == READY:
        print("Ready")
    elif state == WAITING:
        print("Waiting")
    elif state == ERROR:
        print("Error")
    else:
        print("unknown state")
        raise SystemExit("What happened?!")

state = READY
print_state(state)

while True:
    event = input("Enter event (ping, pong, timeout, retry): ")
    try:
        event_id = event_translation[event]
        state = fsm[state][event_id]
        print_state(state)
    except KeyError:
        print("Unknown event")



