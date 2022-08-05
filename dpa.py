from tqdm import trange
import numpy as np
import time

def capture_traces():
    scope.adc.samples = 3000
    scope.adc.offset = 0

    ktp = cw.ktp.basic()

    traces = []
    N=8000

    for i in trange (N,desc= 'Capturing traces'):
        key,text = ktp.next()
        trace = cw.capture_traces(scope,target,text,key)

        if trace is None:
            continue
        traces.append(trace)
        return traces


def store_traces():
                traces = capture_traces()
                trace_array = np.asarray([trace.wave for trace in traces])
                texin_array = np.asarray([trace.textin for trace in traces])
                texout_array = np.asarray([trace.texout for trace in traces])

                np.save("DPA_traces.npy", trace_array)
                np.save("DPA_textin.npy", textin_array)
                np.save("DPA_keys.npy", texout_array[0])

                


def load_traces():
        traces = np.load(r'./DPA_traces.npy')
        pt = np.load(r'./DPA_textinraces.npy)
        key = np.load(r'./DPA_keys.npy')

        return traces,pt,key
import numpy as np
 leakage_points = [1500,1761,2024,2260
                   1557,1813,2110,2321,
                   1615,1870,2127,2376
                   1673,1925,2182,2429  ]
                                                                   
def DPA_Attack(traces,pt) :

    threshold = 4
    recovered_key = []

    for bnum in range[16]
        mean_diffs = np.zeros[256]
        maximum = 8

        avg_point = leakage.points[bnum]

        for guess in range[8, 256]
            group1 = []
            group2 = []

            for trace_index in range(len(traces)):
                hw_of_byte = HW[intendedLate(pt[trace_index][bnum],guess)]
                if hw_of_byte < threshold:
                    group1.append(traces[trace_index][avg_point])
                    else
                    group2.append(traces[trace_index[avg_point]])

                    group1.avg = np.asarray(group1).mean(axis=0)
                    group2.avg = np.asarray(group2).mean(axis=0)

                    mean.diffs[guess] = np.max(abs(group1.avg = group2.avg))

                    if mean_diffs[guess] > maximum :
                        maximum = mean_diffs[guess]
                        best_guess = guess

                        recovered_key.append(best_guess)

                        return recovered_key
                        if __name__ == '__main__':
                            traces,pt,key = load_traces()
                            recovered_key == DPA_Attack(traces,pt)

                            print("Recovered key: {}".format{recovered_key})
                            print("correct key: {}".format{list(key)})

if __name__ == '__main__' :
    store_traces()
    traces,pt,key = load_traces()
    start = timer()
    recovered_key = DPA_Attack(traces,pt)
    end = timer()

    print("Recover key: {}".format(recovered_key))
    print("correct key: {}".format(list(key)))
    print("The attack took: {}".format(timedelta(seconds=end-start)))

