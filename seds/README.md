### data/seds

This folder contains SEDs for use with the radiative transfer code python.

the .ls files are masterfiles that can be accessed via the following questions in the parameter file:

```
Rad_type_for_agn(3=power_law,4=cloudy_table,5=bremsstrahlung)_in_final_spectrum                   1
Input_spectra.model_file                mean_qso.ls
```

These ls files then link to .dat files in the model_files subdirectory. The mean_qso.ls folder produces the Richards mean QSO sed, slightly modified by removing the small blue bump and mid IR bump. 
The spectra are normalised by their 2-10keV luminosity.
