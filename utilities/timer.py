import time


class timer:

    def __init__(self):
        self._done = False

    def turn_off(self) -> None:
        """Stops current timer from running"""
        self._done = True

    def turn_on(self) -> None:
        """Allows timers to be started again

        TODO: name sounds like it also restarts active timers, rename or add that functionality (storing arguments)
        """
        self._done = False

    def run_after(self, num_secs: int, func: callable, **kwargs) -> None:
        """Continuously runs a function after a certain amount of time or until timer is turned off

        NOTE: Currently a blocking function, probably fine but could spin it off into a thread
        NOTE: Does not account for time spent running func, tbd if needed

        Args:
            - num_secs: an integer representing the amount of time in seconds to wait between running the function
            - func: a function to be ran every num_secs amount of time
            - kwargs: any arguments to be passed to func
        """
        start_time = time.time()
        while not self._done:
            if time.time() - num_secs > start_time:
                func(kwargs)
                start_time = time.time()
