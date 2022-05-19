import sys
from numpy import copy
from scipy.io import wavfile
from scipy.fft import *
from scipy.signal import decimate


def methodHPS(w, signal):
    signalData = []

    for i in range(2):
        signalk = [signal[i * int(w):(i + 1) * int(w)]]

    for data in signalk:
        fft_data = abs(fft(data))
        hpik = copy(fft_data)

        for i in range(2, 6):
            d = decimate(fft_data, int(i))
            hpik[: len(d)] *= d

        signalData.append(hpik)

    result = sum(signalData)

    maleRecognise = sum(result[60: 160])
    femaleRecognise = sum(result[180:270])
    if maleRecognise > femaleRecognise:
        return "M"
    else:
        return "K"


if len(sys.argv) > 1:
    file = sys.argv[1]
    w, signal = wavfile.read(file)
    result = methodHPS(w, signal)
    print(result)
else:
    print("file not specified, enter a file")
