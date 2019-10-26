class GameState:
    def __int__(self, state):
        self.Enter = state.Enter
        self.Exit = state.Exit
        self.Pause = state.Pause
        self.Resume = state.Resume
        self.Handle_Events = state.Handle_Events
        self.Update = state.Update
        self.Render = state.Render
        pass


running = None
stack = None


def Change_State(state):
    global stack

    if len(stack) > 0:
        stack[-1].Exit()
        stack.pop()

    stack.append(state)
    state.Enter()


def Push_State(state):
    global stack

    if len(stack) > 0:
        stack[-1].Pause()

    stack.append(state)
    state.Enter()


def Pop_State():
    global stack

    if len(stack) > 0:
        stack[-1].Exit()
        stack.pop()

    if len(stack) > 0:
        stack[-1].Resum()


def Quit():
    global running
    running = False


def Run(start_state):
    global running, stack

    running = True
    stack = [start_state]

    start_state.Enter()

    while running:
        stack[-1].Handle_Events()
        stack[-1].Update()
        stack[-1].Render()

    while len(stack) > 0:
        stack[-1].Exit()
        stack.pop()



