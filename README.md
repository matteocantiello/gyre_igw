# IGW with GYRE
Here we're looking at IGWs in main sequence intermediate and massive stars. The idea is to look at g-modes with GYRE using MESA background structures.
We calculate non-adiabatic mdes since we're interested in the surface manifestation of the waves and radiative damping is important. The normalization will come using Daniel Lecoanet theory + numerical simulations (DEDALUS). We then plan to compare to COROT/K2/TESS observations.


The calculations were run with MESA and GYRE for 3,7,10 and 20 Msun models. 
Each mass has modes with l=1,2,3 in the range [1,50] muHz, calculated at 3 different evolutionary stages: Xc (core H fraction) = 0.67, 0.33, 0.01 (roughly corresponding to ZAMS, mid MS and TAMS). Naming convention: 10XC001_1_50mode.txt is for a 10Msun with Xc=0.01, frequencies in the range 1...50 muHz.  The relative MESA profiles can be found in the respective mass folders (xx/LOGS/profile1.data -> Xc = 0.67 , profile2.data -> Xc = 0.33, profile3.data -> Xc = 0.01)
