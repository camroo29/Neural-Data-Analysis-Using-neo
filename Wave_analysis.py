import neo
import numpy as np


class WaveAnalysis:

    def __init__(self, file):
        reader = neo.Spike2IO(filename=file).read()[0]  # 1 block, 1 segment
        segment = reader.segments[0]
        self.signals = segment.analogsignals
        self.event_times = segment.events[0].times

    def signal_spikes(self, signal_index):
        self._spike_at(signal_index, 0)

    def _spike_at(self, signal_index, event_idx, delta=2e-04):
        """
        :param signal_index: What signal?
        :param event_idx: Index into the event time
        :param delta:
        :return:
        """
        x = self.signals[signal_index].times
        y = self.signals[signal_index]

        time = self.event_times[event_idx].magnitude

        left = time - delta  # lower bound from event.times
        right = time + delta  # upper bound from event.times

        print(time)
        arr = [(float(x[idx].magnitude), float(y[idx].magnitude)) for idx in
               np.where(np.logical_and(x >= left, x <= right))[0]]
        print(arr)
        print([abs(time - x) for x, y in arr])


if __name__ == '__main__':
    analysis = WaveAnalysis("A:\Campus Work\Wave_analysis\EEP data\J5-527.smr")
    analysis.signal_spikes(1)
