import numpy as np
from scipy.ndimage.morphology import generate_binary_structure, binary_erosion, binary_closing, binary_dilation
from scipy.ndimage.filters import maximum_filter, median_filter
from scipy.ndimage.measurements import label, find_objects


def get_chunks(array, area, output, tag):
    ## define connected bins to check, in this case, all the surrounding bins (8-d)
    neighborhood = generate_binary_structure(2,2)
    ## put all the pixels maximal value in therir neighborhood
    local_max = maximum_filter(array, footprint=neighborhood)==array
    ## detect background of the array
    background = (array==0)
    ## remove background from array, to only keep peaks
    eroded_background = binary_erosion(background, structure=neighborhood, border_value=1)
    detected_peaks = local_max ^ eroded_background
    ## in order to extract the chunks, fill gaps
    dilation = binary_dilation(detected_peaks, structure=np.ones((area,area))).astype(np.int)
    ## extraction of loops and write results
    labeled_array, num_features = label(dilation, structure=neighborhood)
    positions = find_objects(labeled_array, max_label= num_features+1)
    w = open(output+'/%s_chunk_loops.tsv' %(tag), 'w')
    for n, p in enumerate(positions):
        try:
            xstart, xend = p[0].start, p[0].stop
            ystart, yend = p[1].start, p[1].stop
            position_anchor1 = min(xstart, xend) + start_bin
            position_anchor2 = min(ystart, yend) + start_bin
            w.write('{}\t{}\t{}\n'.format(crm, position_anchor1, position_anchor2))
        except TypeError:
            continue
    w.close()
