
def scan_chromosome(min_dist_reso, max_dist_reso, chromosome,
                    bam_dict, size, step, start_bin, end_bin, model):
    res = []
    # distance to diagonal
    for dist in range(min_dist_reso, max_dist_reso, step):
        for bstart in range(start_bin, end_bin, step):
            start1 = bstart
            end1   = start1 + size
            start2 = end1 + dist + 1
            end2   = start2 + size
            # avoid falling outside wanted region
            if end2 > end_bin:
                continue
            # midpoint of the matrix used as label
            label = '{}_{:.0f}_{:.0f}'.format(chromosome,
                                              (start1 + end1) // 2,
                                              (start2 + end2) // 2 + 1)
            # extract submatrix from Hi-C, as a vector
            matrix = [[[bam_dict[(p1, p2)]] for p2 in range(start2, end2)]
                      for p1 in range(start1, end1)]
            # predict if the matrix adjusts to the model
            prediction = model.predict([[matrix]])
            res.append((label, prediction))
    return res
