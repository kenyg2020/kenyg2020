import numpy as np
from base_signal import BaseSignal

class Sinusoidal(BaseSignal):

    def __init__(self, amplitude=1.0, ftype ="sin"):
        if ftype not in ["sin", "cos", "tan"]:
            raise ValueError, "ftype not correctly defined. Options are sin, cos and tan."

        self.amplitude = amplitude
        self.ftype_dict = {"sin": np.sin, "cos": np.cos, "tan": np.tan}
        self.ftype = self.ftype_dict[ftype]
        self.setFreqFlag = False

    def sample_next(self, samples, errors):
        
        assert self.setFreqFlag == True, "Frequency not set for Sinusoidal object"
        self.curr_sample += self.resolution
        return self.amplitude*self.ftype(self.curr_sample), self.curr_sample


    def sample(self, nsamples=100):

        assert self.setFreqFlag == True, "Frequency not set for Sinusoidal object"
        timeVec = np.linspace(0, nsamples*self.resolution, num=nsamples)
        signal = self.amplitude*self.ftype(timeVec)

        return signal, timeVec

    def setFrequency(self, frequency):
        self.resolution = 1./frequency
        self.curr_sample = -resolution
        self.setFreqFlag = True





