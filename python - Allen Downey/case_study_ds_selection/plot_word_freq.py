from readfile import process_file,read_file

import matplotlib.pyplot as plt

filename = 'emma.txt'

line = read_file(filename,skip_footer=True, skip_header=True)
hist = process_file(line)

def rank_freq(hist):
    freqs = list(hist.values())
    freqs.sort(reverse=True)

    # enumerate the ranks and frequencies
    rf = [(r+1,f) for r,f in enumerate(freqs)]
    return rf

def print_ranks(hist):
    for r,f in rank_freq(hist):
        print(r,f)

def plot_ranks(hist, scale='log'):
    t = rank_freq(hist)
    rs,fs = zip(*t)

    plt.clf()
    plt.xscale(scale)
    plt.yscale(scale)
    plt.title('Zipf plot')
    plt.xlabel('rank')
    plt.ylabel('frequency')
    plt.plot(rs,fs, 'r-',linewidth=3)
    plt.show()


plot_ranks(hist)
