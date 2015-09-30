## Description of Atomic Data for the MCRT Code Python
### Archive: data39 

This is a directory which contains all of the various types
of data that one might want to use.  This includes spectral
models for use with python as well as atomic data and linelists.

this particular version is an archived atomic dataset which one should use if trying to reproduce the results of:

* Sim et al. 2005, MNRAS, 363, 615
* Long & Knigge 2002, ApJ, 579, 725
* Noebauer et al. 2010, ApJ, 719, 1932

I would recommend running with something like Python 58. 

### Atomic Datasets

**Masterfiles:** These data sets have their masterfiles in the masterfiles folder. To use put data/masterfile in your parameter file.

* h3: 3 level Hydrogen only macro-atom 
* h4: 4 level Hydrogen only macro-atom
* h10: 10 level Hydrogen only macro-atom
* h20: 20 level Hydrogen macro-atom only (Sim et al. 2005)
* standard39: standard data set using atomic 39 (Long & Knigge 2002, Noebauer et al. 2010)
* standard_sn_kurucz: dataset with Supernovae abundances, for use for comparison with Tardis.

**Folders:** All macro atom data contains in atomic_macro. Atomic data for the required version in atomicxx, i.e. standard77 uses atomic77.


### Disk/Stellar Models

To use put data/masterfile.ls in your parameter file, e.g. data/model_kurucz91. 

* kurucz91.ls: Kurucz model atmospheres. Grid goes to 50,000K and log(g) = 5
* disk06.ls: Disk 06 models
* lejeune.ls: A set of stellar models from lejeune.  Not yet used. Their advantage is that they go further into the IR than kurucz

**Folders:** Masterfiles have same names as folders, except for the d14 and kur_tlusty_hybrid models which are contained in disk14 folder.


### Using Old Atomic Data

The branch `old_data` contains the archived atomic datasets. You can checkout old versions with the following command, providing you have pulled the old_data branch from the remote repository

```
git checkout dataxx
```

where xx is a string like 77. This will actually get the old version of the data, complete with old formats. This means, for example, that the photoionization data from VFKY may not be tabulated, so you will need a version of the code which corresponds to the atomic data version number.

To simply run old datasets with the current format philosophy, use the masterfiles in the directory.

