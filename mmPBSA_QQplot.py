# Amber MMP(G)BSA Energy Terms Post Processing: Q-Q Plot

# Written by Pin-Chih Su & Cheng-Chieh Tsai. Last modified on Nov 12,2015

# Tested in python 2.7.6, scipy-0.13.3, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7

# This script will read Amber MMP(G)BSA energy terms outputs and make a Q-Q plot to see

# if the free energy data points are normally distributed.

import pylab 

import scipy.stats as stats

import matplotlib.pyplot as plt

import os

import sys, getopt

import numpy as np

def main(argv):
    
    inputfile = ''
   
    outputfile = ''

    frame_number = ''
   
    try:
       
        opts, args = getopt.getopt(argv,"hi:o:f:",["ifile=","ofile=","fnumber"])
      
    except getopt.GetoptError:
       
        print 'python mmPBSA_QQplot.py -i <inputfile> -o <outputfile> -f <frame_number>'
      
        sys.exit(2)
      
    for opt, arg in opts:
       
        if opt == '-h':
          
            print '\n'+'(1) Usage: python mmPBSA_QQplot.py -i <inputfile> -o <outputfile>'

            print '\n'+'(2) Example: python mmPBSA_QQplot.py -i input_6000.csv -o output -f 2400 (the frame number in the input_6000.csv is 2,400)'

            print '\n'+'(3) The "-f" tag should be an integer equal to the MD trajectory frame number used in the MM-P(G)BSA calculation. Output plots are jpg files'
            
            print '\n'+'(4) Please make sure you have python, scipy, matplotlib installed'
            
            print '\n'+'(5) Tested in python 2.7.6, scipy-0.13.3, matplotlib.pyplot-1.3.1, and Linux Redhat 5.0/Windows 7'

            print '\n'+'(6) Written by Dr.Pin-Chih Su and Cheng-Chieh Tsai'

            print '\n'+'(7) If you use this script, please cite: Journal of Computational Chemistry, 2015, 36,1859-1873'

            print '\n'+'(8) More details are available at https://sites.google.com/site/2015pcsu/data-science/mmpbsa'

            sys.exit()
         
        elif opt in ("-i", "--ifile"):
          
            inputfile = arg
         
        elif opt in ("-o", "--ofile"):
          
            outputfile = arg

        elif opt in ("-f", "--fnumber"):
          
            frame_number = arg

    file=open(inputfile,'r')

##    np.seterr(divide='ignore', invalid='ignore')
                       
    DELTATOTAL=[]

    time=frame_number.split()

    for x in time:

        line=file.readlines()

        for a in line:

            if 'DELTA Energy Terms' in a:
        
                tick=2

                while tick <float(x)+2:                                                 # Tell Python how many lines to read.
                                                                                        # The sample file has 2402 lines to read
                    DELTATOTAL.append(float(line[line.index(a)+tick].split(',')[3]))    # Read the column of DELTATOTAL

                    tick=tick+1

    stats.probplot(DELTATOTAL, dist="norm", plot=pylab)

    plt.ylabel("Theoretical Quantiles (Rank-based Z-score)")

    plt.xlabel("Sample Quantiles (kcal/mol)") 

    plt.title("Sample Q-Q Plot")

    plt.savefig(outputfile+".jpg",dpi=100)

    plt.clf()

    plt.close()

if __name__ == "__main__":
    
   main(sys.argv[1:])

