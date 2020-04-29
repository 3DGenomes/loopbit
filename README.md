<img src="https://github.com/3DGenomes/loopbit/blob/master/loopbit_logo.png" height= "225" width="500" align="center">

This add-on of TADbit allows you to run `Loopbit`, a Convolutional Neural Network (CNN) able to identify chromatin loops from 3C-based experiments [CITE PAPER].

<!-- TOC depthFrom:1 depthTo:8 withLinks:1 updateOnSave:1 orderedList:0 -->

  - [Requirements](#requirements)
  - [Installation](#installation)
  - [Quick start](#quick-start)
      - [Scan region of interest or full chromosome](#scan-region-of-interest-or-full-chromosome)
      - [Plot the results](#plot-the-results)
  - [Usage](#usage)
  - [Contributors](#contributors)
  - [Citation](#citation)

<!-- /TOC -->

# Requirements
Loopbit was written and tested using Python 3.6, 3.7.
It requires the packages `matplotlib` (3.2.1), `scipy` (1.0.0), `numpy` (1.14.5), `tensorflow` (1.10.0), and `seaborn` (0.9.0) and `tqdm` (4.32.2).

# Installation

In order to install the package you can download the code from our [GitHub repo](https://github.com/3DGenomes/loopbit) and install it manually. If needed, the dependencies will be downloaded automatically; if you encounter problems, try to install the other [requirements](#requirements) manually.

```bash
git clone https://github.com/3DGenomes/loopbit # or download manually
cd loopbit
python setup.py install
```

# Quick start
After the installation, you can run the provided example to familiarize with the functions of loopbit.

Use `loopbit -h` for quick help and orientation.

## Scan region of interest or full chromosome
For the tutorial we are going to use a region of the chromosome 21 from the replicate H of . We are going to analyze a 1 Mb region, from 33,379,000 to 34,379,000.

```bash
loopbit scan \
example/chr21_GM12878_replicateH.tsv \
chr21 \
45000-3000000 \
5000 \
9 \
3 \
example/ \
```
It will generate a output file with 2 columns, with a label and its probability of being a loop. The label will be <chromosome_binI_binJ>:

*chr21_562183_562202	1.7374185596594756e-19*

*chr21_562186_562205	1.4961456010730012e-13*

## Plot the results
In order to visualize the results we will run the following command-line:

```bash
loopbit plot \
example/chr21_GM12878_replicateH.tsv \
example/loopbit_results_chr21.tsv \
33379694-34327701\
5000\
example/ \
```
This is the plot that will be displayed, containing the contact information in the upper triangle, and the probabilities cloud in the lower triangle:

<img src="https://github.com/3DGenomes/loopbit/blob/master/loopbit_33379694_34327701_region.png" height= "500" width="500" align="center">

# Usage
Loopbit has these two main commands: 
* `scan` to scan the region of interest or the full chromosome to obtain the loop prediction.
* `plot` to generate a plot of a region of interest with the contact matrix and the cloud of probabilities.

## scan
First, the region of interest or the full chromosome have to be scanned, thus obtaining the loop prediction value. To run `scan`, the following arguments are needed:

* A normalized Hi-C matrix file in a TSV format. 
  This should be tab-delimited, where each line has three columns:
  \<row index\> \<column index\> \<value\>

* The name of the chromosome or a specific label to use to store results.
* Interval of distance to check the presence of chromatin loops (bp). For example, if we want to inspect from 45kb to 3Mb, we will put 45000-3000000.
* Resolution of the experiment to inspect, in bp.
* Number of bins considered to check if contains a loop. For example, if we put 9, submatrices of 9x9 will be used to check if contains a loop.

<NOTE: Recommended to have around 9 bins, no less than 3>
* Step size to scan, if 1, it will scan all the chromosome moving +1bin each time
* Directory to store the results.

## plot
This function allows to observe the results from a region of interest.
* A normalized Hi-C matrix file in a TSV format. 
  This should be tab-delimited, where each line has three columns:
  \<row index\> \<column index\> \<value\>
* The outplut file from loopbit.
* Region of interest to be plotted with the following format, in bp: start-end.
* Resolution of the experiment to inspect, in bp.
* Directory to store the results.

<NOTE: there is the parameter -G or gaussian that can be changed if needed. By default is 4. Here you can learn more about how this filter works: https://docs.scipy.org/doc/scipy/reference/generated/scipy.ndimage.gaussian_filter.html >

Frequently asked questions
--------------------------

Check the label `FAQ <https://github.com/3DGenomes/TADbit/issues?utf8=%E2%9C%93&q=is%3Aissue+label%3AFAQ+>`_ in TADbit issues.

If your question is still unanswered feel free to open a new issue.

# Contributors
This add-on of TADbit is currently developed at the  `MarciusLab <http://www.marciuslab.org>`_ with the contributions of Silvia Galan and François Serra.

# Citation
Please, cite this article if you use TADbit.

Serra, F., Baù, D., Goodstadt, M., Castillo, D. Filion, G., & Marti-Renom, M.A. (2017).
**Automatic analysis and 3D-modelling of Hi-C data using TADbit reveals structural features of the fly chromatin colors.**
*PLOS Comp Bio* 13(7) e1005665. `doi:10.1371/journal.pcbi.1005665 <https://doi.org/10.1371/journal.pcbi.1005665>`_
