import mne
import numpy as np
import matplotlib.pyplot as plt
from mne import Epochs, pick_types, events_from_annotations
from mne.channels import make_standard_montage
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci
from mne.preprocessing import ICA
from mne import io
from mne.datasets import sample
from mne.minimum_norm import read_inverse_operator, compute_source_psd

class EEG():
    def __init__(self, raw):
        self.raw = raw
        self.rawLow = None
        self.rawHigh = None
        self.rawBand = None
        self.ica = None

    # PSD
    def power_spectral_density(self):
        # Compute the power spectral density of raw data and plot
        self.raw.compute_psd().plot(average = True, picks = 'data', exclude = 'bads')
        
        plt.show()

    # PSD - Channel(s)
    def power_spectral_density_channels(self, picks):
        # Plot a power spectral density of raw data for a specific channel(s)
        self.raw.compute_psd().plot(picks = picks, exclude = 'bads')
        
        plt.show()

    # PSD - Topomap
    def topomap_PSD(self):
        # Plot topomap (heatmap) of power spectral density of raw data
        self.raw.compute_psd().plot_topomap()
        
        plt.show()

    # Filtering - Band-pass
    def bandpass_filtering(self, low_frq = 7.0, high_frq = 13.0, fir_design = 'firwin', skip_by_annonation = 'edge'):
        # Apply band-pass filter
        self.raw.filter(low_frq, high_frq, fir_design = fir_design, skip_by_annotation = skip_by_annonation)
        
        self.raw.plot()
        plt.show()

    # Filtering - Low pass    
    def lowpass_filtering(self, high_frq = 30.0, fir_design = 'firwin'):
        low_frq = None
        self.raw.filter(low_frq, high_frq, fir_design = fir_design)
        
        self.raw.plot()
        plt.show()
        
    # Filtering - High pass
    def highpass_filtering(self, low_frq = 20.0, fir_design = 'firwin'):
        high_frq = None # High frq limit
        self.raw.filter(low_frq, high_frq, fir_design = fir_design)  
        
        self.raw.plot()
        plt.show()
    
    # Electrodes   
    def plot_electrode(self):
        # Plot sensor (electrode) locations on a head
        self.raw.plot_sensors(ch_type="eeg")
        
        plt.show()
    
    # ICA - Preprocessing
    def preprocessing_ICA(self, n_components = 20, random_state = 97, max_iter = 800):
        # Apply ICA to Raw data
        self.ica = mne.preprocessing.ICA(n_components = n_components, random_state = random_state, max_iter = max_iter)
        self.ica.fit(self.raw)
        #self.ica.exclude = [15]  # ICA components
    
    # ICA - Components 1D Series
    def plot_ica_components_1D(self, picks = None):
        # Plot the 1D time series of each ICA component
        self.ica.plot_sources(self.raw, picks = picks, title = 'ICA - Components 1D Series')
        
        plt.show()
        
    # ICA - Components Topomap
    def plot_ica_components_topomap(self, picks = None):
        # Plot Ica Components Topomap
        self.ica.plot_components(picks = picks, title = 'ICA Components Topomap')
        
        plt.show()
        
        
    #self.ica.plot_properties(self.raw, picks = self.ica.exclude)                                                                                                               

    # Find the covariance of channels of raw data and plot
    #noise_cov = mne.compute_raw_covariance(raw, method="shrunk")
    #fig_noise_cov = mne.viz.plot_cov(noise_cov, raw.info, show_svd=False)

    # Plot ICA components
    #mne.viz.plot_ica_sources(self.ica, self.raw)
    #self.ica.plot_components()
    #self.ica.plot_overlay(self.raw)
    
'''
# PSD
def power_spectral_density(raw):
    # Compute the power spectral density of raw data and plot
    raw.compute_psd().plot(average=True, picks="data", exclude="bads")
    
    plt.show()

# PSD - Channel(s)
def power_spectral_density_channels(raw, picks):
    # Plot a power spectral density of raw data for a specific channel(s)
    raw.compute_psd().plot(picks=picks, exclude="bads")
    
    plt.show()

# PSD - Topomap
def topomap_PSD(raw):
    # Plot topomap (heatmap) of power spectral density of raw data
    raw.compute_psd().plot_topomap()

# Filtering - Band-pass
def bandpass_filtering(raw):
    # Apply band-pass filter
    low = 7.0 # Low frq limit
    high = 30.0 # High frq limit
    firDesign = 'firwin'
    skip_byan = "edge"
    raw.filter(low, high, fir_design=firDesign, skip_by_annotation=skip_byan)
    
    raw.plot()
    plt.show()

# Filtering - Low pass    
def low_pass_filtering(raw):
    low = None # Low frq limit
    high = 50. # High frq limit
    firDesign = 'firwin' # firwin - default, additional ones are: firwin2, firwin3
    raw.filter(low, high, fir_design=firDesign)
    
    raw.plot()
    plt.show()
    
# Filtering - High pass
def high_pass_filtering(raw):
    low = 1. # Low frq limit
    high = None # High frq limit
    firDesign = 'firwin' # firwin - default, additional ones are: firwin2, firwin3
    raw.filter(low, high, fir_design=firDesign)  
    
    
    raw.plot()
    plt.show()
 
# Electrodes   
def plot_electrode(raw):
    # Plot sensor (electrode) locations on a head
    raw.plot_sensors(ch_type="eeg")
    
    plt.show()
'''

if __name__ == "__main__":
    tmin, tmax = -1.0, 4.0
    event_id = dict(hands=2, feet=3)
    subject = 1
    runs = [6, 10, 14]  # motor imagery: hands vs feet

    raw_fnames = eegbci.load_data(subject, runs)
    raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
    
    eeg = EEG(raw)
    
    #################################################
    eegbci.standardize(raw)  # set channel names
    montage = make_standard_montage("standard_1005")
    eeg.raw.set_montage(montage)
    #################################################
    
    #events, _ = events_from_annotations(raw, event_id=dict(T1=2, T2=3))

    #picks = pick_types( raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads" )
    
    picks = pick_types(
        eeg.raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads"
    )
    
    eeg.topomap_PSD()
    
    eeg.plot_electrode()
    
    picks2 = ["AFz", "CPz"]
    
    eeg.preprocessing_ICA()
    eeg.plot_ica_components_1D()
    eeg.plot_ica_components_topomap()
    
    eeg.power_spectral_density()
    eeg.power_spectral_density_channels(picks2)

    eeg.lowpass_filtering()
    
    eeg.power_spectral_density()
    eeg.plot_ica_components_1D()
    eeg.power_spectral_density_channels(picks2)
    
    eeg.highpass_filtering()
    
    eeg.power_spectral_density()
    eeg.plot_ica_components_1D([0,7,5])
    eeg.power_spectral_density_channels(picks2)
    
    eeg.bandpass_filtering()
    
    eeg.power_spectral_density()
    eeg.plot_ica_components_1D([5,9,11])
    eeg.power_spectral_density_channels(picks2)