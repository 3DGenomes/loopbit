import numpy as np

def scan_chromosome(min_dist_reso, max_dist_reso, chromosome, bam_dict, size, step, start_bin, end_bin, model):
    res = []
    for dist in range(min_dist_reso, max_dist_reso, step):
        for bstart in range(start_bin, end_bin, step):
            start1 = bstart
            end1   = start1 + size
            start2 = end1 + dist + 1
            end2   = start2 + size
            if end2 <= end_bin:
                mean1, mean2 = (start1 + end1) // 2, (start2 + end2) // 2
                label = '{}_{}_{}'.format(chromosome, mean1, mean2)
                vector = np.array([bam_dict[(p1, p2)] for p1 in range(start1, end1)
                                   for p2 in range(start2, end2)])
                prediction = model.predict([vector.reshape(-1, size, size, 1)])
                res.append((label, prediction))
    return res
