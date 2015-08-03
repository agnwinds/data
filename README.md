## Description of Atomic Data for the MCRT Code Python

This is a directory which contains all of the various types
of data that one might want to use.  This includes spectral
models for use with python as well as atomic data and linelists


### Atomic Datasets

**Masterfiles:** These data sets have their masterfiles in the masterfiles folder. To use put data/masterfile in your parameter file.

* h3: 3 level Hydrogen only macro-atom 
* h4: 4 level Hydrogen only macro-atom
* h10: 10 level Hydrogen only macro-atom
* h20: 20 level Hydrogen macro-atom only (Sim et al. 2005)
* h10_standard78: 10 level Hydrogen macro-atom, standard73 for simple ions 
* h10_hetop_standard78: 10 level Hydrogen macro-atom, 53 level Helium macro-atom topbase, standard78 for simple ions 
* h20_hetop_standard78: 20 level Hydrogen macro-atom, 53 level Helium macro-atom topbase, standard78 for simple ions (Matthews+ 2015)
* standard39: standard data set using atomic 39 (Long & Knigge 2002, Noebauer et al. 2010)
* standard70: standard data set using atomic 39 - interim version of atomic data used during AGN development
* standard73: standard data set using atomic 39 (Higginbottom et al. 2013)
* standard77: standard data set using atomic 77- includes extrapolated XSections (Higginbottom et al. 2014)
* standard78 (STANDARD): standard data set using atomic 78- includes Dere PI data
* standard79 (BETA): standard data set using atomic 79- electron yield data from Kaastra and Mewe and VY inner shell cross sections
* standard_sn_kurucz: dataset with Supernovae abundances, for use for comparison with Tardis.

**Folders:** All macro atom data contains in atomic_macro. Atomic data for the required version in atomicxx, i.e. standard77 uses atomic77.


### Disk/Stellar Models

To use put data/masterfile.ls in your parameter file, e.g. data/model_kurucz91. 

* kurucz91.ls: Kurucz model atmospheres. Grid goes to 50,000K and log(g) = 5
* kurucz_d14.ls: Kurucz model atmospheres run through Synspec. Grid goes to 50,000K and log(g) = 5
* tlusty_d14.ls: TLUSTY model atmospheres. Grid goes to 130,000K and log(g) = 9
* kur_tlusty_hybrid.ls: Kurucz + TLUSTY hybrid model atmosphere's. Current benchmark SA grid for accretion disk.
* disk06.ls: Disk 06 models
* lejeune.ls: A set of stellar models from lejeune.  Not yet used. Their advantage is that they go further into the IR than kurucz

**Folders:** Masterfiles have same names as folders, except for the d14 and kur_tlusty_hybrid models which are contained in disk14 folder.


### Other Folders
Not all currently maintained.

* atomic_old: a collection of old atomic data, mainly various macro atom data which has not been used
			since python ~58 but may be used for reference and in future.

* calculate_atomic: this old folder should probably be archived here.

* hutdisk93: A set of stellar spectra calculated with TLUSTY/Synspec that KSL has used extenstively for calculations in the UV




### Using Old Atomic Data

The branch `old_data` contains the archived atomic datasets. You can checkout old versions with the following command, providing you have pulled the old_data branch from the remote repository

```
git checkout dataxx
```

where xx is a string like 77. This will actually get the old version of the data, complete with old formats. This means, for example, that the photoionization data from VFKY may not be tabulated, so you will need a version of the code which corresponds to the atomic data version number.

To simply run old datasets with the current format philosophy, use the masterfiles in the directory.


### History:

04july -- ksl -- Created separate directories ../data44 and ../data50 that just contains
	the data needed to store the atomic files for running Python.  This directory
	contains the old data, as well as data that may not be need for standard runs
	of the program.  
	atomic49 is the version of the atomic datafile used up to and including python49
	atomic50 is a version that strips out a lot of the less used portions of the 
	atomic data.  
	Ultimately one may be able to discard both of these directoreis in favor of the
	datafiles contained in ../data44 and ../data50, but I was a little unsure that
	I had kept everything I needed for them.

1301 -- JM -- The data is now all in one folder (data). atomic data has the form 
	 atomic/atomicxx/standardxx where xx is two numbers.

1307 -- JM -- data folder still the same. standardxx now in top level directory,
	addresses bug #13

1405 -- JM -- reorganisation of data sets and updated readme. Now only one symbolic link is required, to the data folder.
