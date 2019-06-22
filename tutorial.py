from bluesky import RunEngine
from bluesky.callbacks.best_effort import BestEffortCallback
from bluesky.utils import install_kicker


bec = BestEffortCallback()

RE = RunEngine(bec)

install_kicker()