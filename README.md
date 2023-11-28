# BrainNex EEG Visualization Program

## Overview

**BrainNex EEG Studio** is a graphical user interface (GUI) application designed for visualizing and analyzing EEG (Electroencephalogram) data. It allows users to upload EEG data, perform various preprocessing tasks, and visualize the data in different ways.

## Usage

To run the program, execute the `frontmain.py` file. The application provides a main window with a toolbar and various options for interacting with EEG data.

## Main Features

### Upload EEG Data:

Click the "Upload" button to load EEG data from a local file (EDF or FIF format).
The program supports loading files through the file dialog.

### Read Live EEG Data (Future Development):

The "Read Time Data" button is intended for reading live EEG data. This feature is a part of future development.

### Split Screen:

Click the "Split screen" button to split the main window into two separate windows, each displaying EEG data independently.

### Menu Options:

Access additional functionalities through the menu options provided in the toolbar.
Options include preprocessing using ICA, plotting ICA properties, plotting ICA in 1D, plotting ICA topomap, power spectral density analysis, and various filtering options.

### Dark and Light Theme:

Change the theme of the application between dark and light using the theme icons in the system tray.

### Tray Menu:

Access theme change options and return to the main screen through the system tray icon.

## Theme Options

The program provides options to switch between dark and light themes. Users can access these options through the system tray icon menu.

## Dependencies

The program relies on various Python libraries, including mne, numpy, matplotlib, pyqtgraph, qdarktheme, and qtawesome. Ensure these libraries are installed before running the application.

## Contact Information

For inquiries or permission regarding the code, please contact [DmytroLevytskyi7@gmail.com](mailto:DmytroLevytskyi7@gmail.com).

## Notes

All rights to this code are reserved, and no part of it should be used, modified, or distributed for commercial use without explicit written permission.

**Note:** Ensure that you have the necessary dependencies installed before running the program. The `components.py` file contains additional classes used in the main program.

Feel free to reach out if you have any questions or need further assistance.
