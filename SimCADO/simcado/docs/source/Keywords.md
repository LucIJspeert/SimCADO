# List of Keywords for Controlling SimCADO

## Parameters regarding the simulated "observation"

```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
OBS_DATE                0           # [dd/mm/yyyy] Date of the observation [not yet implemented]
OBS_TIME                0           # [hh:mm:ss] Time of the observation [not yet implemented]
OBS_RA                  0           # [deg] RA of the object [not yet implemented]
OBS_DEC                 0           # [deg] Dec of the object [not yet implemented]
OBS_ALT                 0           # [deg] Altitude of the object [not yet implemented]
OBS_AZ                  0           # [deg] Azimuth of the object [not yet implemented]
OBS_ZENITH_DIST         60          # [deg] from zenith
OBS_PARALLACTIC_ANGLE   0           # [deg] rotation of the source relative to the zenith
OBS_SEEING              0.6         # [arcsec]

OBS_EXPTIME             60          # [sec] simulated exposure time
OBS_NDIT                1           # [#] number of exposures taken
OBS_NONDESTRUCT_TRO     2.6         # [sec] time between non-destructive readouts in the detector
OBS_REMOVE_CONST_BG     yes         # remove the minimum background value

OBS_INPUT_SOURCE_PATH   none        # Path to input Source FITS file
OBS_FITS_EXT            0           # the extension number where the useful data cube is

OBS_OUTPUT_DIR          default     # Path to save output in

OBS_OUT_SIGNAL          yes         # yes/no to saving the signal component of the observation
OBS_OUT_NOISE           yes         # yes/no to saving the noise component of the observation
OBS_OUT_READOUT         yes         # yes/no to saving the readout component of the observation
OBS_OUT_REDUCED         yes         # yes/no to saving a background subtracted readout image
```


## Parameters relating to the simulation
```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
SIM_DETECTOR_PIX_SCALE  0.004       # [arcsec] plate scale of the detector
SIM_OVERSAMPLING        1           # The factor of oversampling inside the simulation
SIM_PIXEL_THRESHOLD     1           # photons per pixel summed over the wavelength range. Values less than this are assumed to be zero

SIM_LAM_TC_BIN_WIDTH    0.001       # [um] wavelength resolution of spectral curves
SIM_SPEC_MIN_STEP       1E-4        # [um] minimum step size where resampling spectral curves

SIM_FILTER_THRESHOLD    1E-9        # transmission below this threshold is assumed to be 0
SIM_USE_FILTER_LAM      yes         # yes/no to basing the wavelength range off the filter non-zero range - if no, specify LAM_MIN, LAM_MAX
# if "no"
SIM_LAM_MIN             1.9         # [um] lower wavelength range of observation
SIM_LAM_MAX             2.41        # [um] upper wavelength range of observation
SIM_LAM_PSF_BIN_WIDTH   0.1         # [um] wavelength resolution of the PSF layers
SIM_ADC_SHIFT_THRESHOLD 1           # [pixel] the spatial shift before a new spectral layer is added (i.e. how often the spectral domain is sampled for an under-performing ADC)

SIM_PSF_SIZE            511         # size of PSF
SIM_PSF_OVERSAMPLE      no          # use astropy's inbuilt oversampling technique when generating the PSFs. Kills memory for PSFs over 511 x 511
SIM_VERBOSE             no          # [yes/no] print information on the simulation run
SIM_SIM_MESSAGE_LEVEL   3           # the amount of information printed [5-everything, 0-nothing]

SIM_OPT_TRAIN_IN_PATH   none        # Options for saving and reusing optical trains. If "none": "./"
SIM_OPT_TRAIN_OUT_PATH  none        # Options for saving and reusing optical trains. If "none": "./"
SIM_DETECTOR_IN_PATH   none        # Options for saving and reusing detector objects. If "none": "./"
SIM_DETECTOR_OUT_PATH  none        # Options for saving and reusing detector objects. If "none": "./"

SIM_MAX_RAM_CHUNK_GB   2            # Maximum amount of RAM to be taken up by one a single object
SIM_SPEED              10           # 10 = Fast, but skips on details, 1 = Slow, but does everything as accurately as possible
SIM_NUM_CPUS           -1           # Number of CPUs to use for multicore computations. -1 = all idyl cores
```


## General atmospheric parameters

```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
ATMO_USE_ATMO_BG       yes          # [yes/no] 

ATMO_TC                 default     # [filename/default] for atmospheric transmission curve. If "default": <pkg_dir>/data/skytable.fits
ATMO_EC                 default     # [filename/default/none] for atmospheric emission curve. If "default": <pkg_dir>/data/skytable.fits
# If ATMO_EC is "none": set ATMO_BG_MAGNITUDE for the simulation filter. 
ATMO_BG_MAGNITUDE       default     # [ph/s] background photons for the bandpass if ATMO_EC = None

ATMO_TEMPERATURE        0           # deg Celcius
ATMO_PRESSURE           750         # millibar
ATMO_REL_HUMIDITY       60          # %
```


## General Telescope parameters
```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
SCOPE_ALTITUDE          3060        # meters above sea level
SCOPE_LATITUDE          -24.589167  # decimal degrees
SCOPE_LONGITUDE         -70.192222  # decimal degrees

SCOPE_PSF_FILE          default      # [filename/default] import a PSF from a file, if none "default" is <pkg_dir>/data/PSF_POPPY.fits
SCOPE_STREHL_RATIO      1         # [0..1] defines the strength of the seeing halo if SCOPE_PSF_FILE is "default"
SCOPE_AO_EFFECTIVENESS  100         # [%] percentage of seeing PSF corrected by AO - 100% = diff limited, 0% = 0.8" seeing
SCOPE_JITTER_FWHM       0.001       # [arcsec] gaussian telescope jitter (wind, tracking)
SCOPE_DRIFT_DISTANCE    0           # [arcsec/sec] the drift in tracking by the telescope
SCOPE_DRIFT_PROFILE     linear      # [linear, gaussian] the drift profile. If linear, simulates when tracking is off. If gaussian, simulates rms distance of tracking errors

SCOPE_USE_MIRROR_BG     yes         # [yes/no]

# Similar details can be specified for each individual mirror by copying these
# keywords and replacing M1 with Mx. Properties not explicitly specified are
# inherited from M1.
SCOPE_NUM_MIRRORS       6           # number of reflecting surfaces
SCOPE_M1_DIAMETER_OUT   37.3        # meters
SCOPE_M1_DIAMETER_IN    11.1        # meters
SCOPE_M1_TC             default        # Mirror reflectance curve. Default is <pkg_dir>/data/TC_mirror_mgf2agal.dat
SCOPE_M1_TEMP           0           # deg Celsius - temperature of mirror
SCOPE_M2_DIAMETER_OUT   4.2         # meters
SCOPE_M2_DIAMETER_IN    0.          # meters
SCOPE_M3_DIAMETER_OUT   3.8         # meters
SCOPE_M3_DIAMETER_IN    0.          # meters
```


## Parameters regarding the instrument
```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
INST_TEMPERATURE        -190        # deg Celsius - inside temp of instrument

INST_ENTR_NUM_SURFACES  2           # number of surfaces on the entrance window
INST_ENTR_WINDOW_TC     default     # If "default": <pkg_dir>/data/TC_window.dat
INST_DICHROIC_TC        default
INST_FILTER_TC          K          # specify a standard broadband filter of a file path to a transmission curve. Accepted broadband filters: I z Y J H Ks K

INST_NUM_MIRRORS        8           # number of reflecting surfaces in MICADO
INST_NUM_EXT_MIRRORS    8           # number of reflecting surfaces between telescope and instrument (i.e. MAORY)

INST_ADC_PERFORMANCE    100         # [%] how well the ADC does its job
INST_ADC_NUM_SURFACES   4           # number of surfaces in the ADC
INST_ADC_TC             default     # transmission curve of the ADC. If "default": <pkg_dir>/data/

INST_DEROT_PERFORMANCE  100         # [%] how well the derotator derotates
INST_DEROT_PROFILE      linear      # [linear, gaussian] the profile with which it does it's job

INST_DISTORTION_MAP     none        # path to distortion map
```


## General detector parameters
```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------
FPA_USE_NOISE           yes         # [yes/no]

FPA_READOUT_MEDIAN      4           # e-/px
FPA_READOUT_STDEV       1           # e-/px
FPA_DARK_MEDIAN         0.01        # e-/s/px
FPA_DARK_STDEV          0.01        # e-/s/px

FPA_QE                  default     # if "default": <package_path>/data/TC_detector_H4RG.dat
FPA_NOISE_PATH          default     # [default/generate/filename] if "generate": use NGHxRG to create a noise frame. If "default": <package_path>/data/FPA_noise.fits
FPA_GAIN                1           # e- to ADU conversion
FPA_WELL_DEPTH          1E5         # number of photons collectable before pixel is full
FPA_LINEARITY_CURVE     none        #

FPA_PIXEL_MAP           none        # path to a FITS file with the pixel sensitivity map
# if none
FPA_DEAD_PIXELS         1           # [%] if FPA_PIXEL_MAP=none, a percentage of detector pixel which are dead
FPA_DEAD_LINES          1           # [%] if FPA_PIXEL_MAP=none, a percentage of detector lines which are dead

FPA_CHIP_LAYOUT         small       # [small/default/filename] description of the chip layout on the detector array. if "default": <pkg_dir>/data/FPA_chip_layout.dat
```


## HxRG Noise Generator package parameters
SimCADO uses the python code developed by Bernhard Rauscher for the HAWAII 2RG detectors aboard the JWST. See Rauscher (2015) for a summary of what keqwords they mean ([http://arxiv.org/pdf/1509.06264.pdf]())
```
Keyword				Default Value	  [units] Explanation
-----------------------------------------------------------------------------------------------

HXRG_NUM_OUTPUTS        32          # Number of
HXRG_NUM_ROW_OH         8           # Number of row overheads
HXRG_PCA0_FILENAME      default     # if "default": <pkg_dir>/data/FPA_nirspec_pca0.fits
HXRG_OUTPUT_PATH        none        # Path to save the detector noise
HXRG_PEDESTAL           4           # Pedestal noise
HXRG_CORR_PINK          3           # Correlated Pink noise
HXRG_UNCORR_PINK        1           # Uncorrelated Pink noise
HXRG_ALT_COL_NOISE      0.5         # Alternating Column noise
```