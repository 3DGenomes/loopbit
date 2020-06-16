import numpy as np

def scan_chromosome(min_dist_reso, max_dist_reso, chromosome, bam_dict, size, step, start_bin, end_bin, model):
    res = []
    for dist in range(min_dist_reso, max_dist_reso, step):
        for bstart in range(start_bin, end_bin, step):
            start1, end1 = bstart, bstart + size
            start2, end2 = end1 + (dist + 1), (end1 + (dist + 1)) + size
            if end2 <= end_bin:
                mean1, mean2 = (start1 + end1) / 2, (start2 + end2) / 2
                label = chromosome+'_'+str(int(mean1))+'_'+str(int(mean2))
                matrix = np.zeros((size, size))
                for x, p1 in enumerate(range(start1, end1)):
                    for y, p2 in enumerate(range(start2, end2)):
                        matrix[x,y] = bam_dict[(p1, p2)]
                if np.count_nonzero(matrix) != 0:
                    vector = matrix.flatten()
                    prediction = model.predict([vector.reshape(-1, size, size, 1)])
                    res.append((label, prediction))
    return res
