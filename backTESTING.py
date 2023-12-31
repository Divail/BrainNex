import mne
import matplotlib.pyplot as plt
from mne import pick_types
from mne.channels import make_standard_montage
from mne.io import concatenate_raws, read_raw_edf
from mne.datasets import eegbci

class EEG():
    ica_bool = False # True if ICA preprocessing has been applied
    
    def __init__(self, raw): #file_path):
        self.raw = raw
        #self.file_path = file_path
        #self.raw = self.load_edf_data(file_path)
        #self.montage() # Instantiate montage
        
    # Loading the EDF raw data
    def load_edf_data(self, file_path):
        # Load the .edf data from the file and return it as raw data
        raw = mne.io.read_raw_edf(file_path, preload=True)
        return raw
    
    # Reseting the raw file 
    def reset_raw(self):
        # Reloading the raw file in order to reset it
        self.raw = self.load_edf_data(self.file_path)
        self.montage()
    
    # Set Montage
    def montage(self):
        # Needs work
        eegbci.standardize(self.raw)  # Set channel names
        montage = make_standard_montage("standard_1005")
        self.raw.set_montage(montage)
        
    # PSD
    def power_spectral_density(self):
        # Compute the power spectral density of raw data and plot
        self.raw.compute_psd().plot(average = True, picks = 'data', exclude = 'bads')
        
        plt.show()

    # PSD - Channel(s)
    def power_spectral_density_channels(self, picks = None):
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
        self.ica_bool = True
        #self.ica.exclude = [15]  # ICA components
    
    # ICA - Components 1D Series
    def plot_ica_components_1D(self, picks = None):
        # Plot the 1D time series of each ICA component
        if self.ica_bool == True:
            self.ica.plot_sources(self.raw, picks = picks, title = 'ICA - Components 1D Series')
        
            plt.show()
        else:
            print("Plase apply ICA Preprocessing")
        
    # ICA - Components Topomap
    def plot_ica_components_topomap(self, picks = None):
        if self.ica_bool == True:
            # Plot Ica Components Topomap
            self.ica.plot_components(picks = picks, title = 'ICA Components Topomap')
            
            plt.show()
        else:
            print("Plase apply ICA Preprocessing")
            
    # ICA - Components' Properties
    def plot_ica_components_properties(self, picks = None):
        if self.ica_bool == True:
            # Plot ICA components' Properties
            self.ica.plot_properties(self.raw, picks = picks) #picks = self.ica.exclude
        else:
            print("Plase apply ICA Preprocessing")                                                                                                           

    # Find the covariance of channels of raw data and plot
    #noise_cov = mne.compute_raw_covariance(raw, method="shrunk")
    #fig_noise_cov = mne.viz.plot_cov(noise_cov, raw.info, show_svd=False)

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
    eeg.plot_ica_components_properties([18,11,17])
    
    eeg.plot_ica_components_1D()
    eeg.plot_ica_components_topomap([0,6,7])
    eeg.plot_ica_components_properties()
    
    eeg.power_spectral_density()
    eeg.power_spectral_density_channels(picks2)

    eeg.lowpass_filtering()
    
    eeg.power_spectral_density()
    eeg.reset_raw()
    eeg.power_spectral_density()
    eeg.preprocessing_ICA()
    eeg.plot_ica_components_1D()
    eeg.power_spectral_density()
    eeg.plot_electrode()
    eeg.power_spectral_density_channels(picks2)
    
    eeg.highpass_filtering()
    
    eeg.power_spectral_density()
    eeg.plot_ica_components_1D([0,7,5])
    eeg.power_spectral_density_channels(picks2)
    
    eeg.bandpass_filtering()
    
    eeg.power_spectral_density()
    eeg.plot_ica_components_1D([5,9,11])
    eeg.power_spectral_density_channels(picks2)