import mne
import numpy as np
import matplotlib.pyplot as plt
from globals import *
from mne.channels import make_standard_montage
from mne.datasets import eegbci
from mne.decoding import CSP
from mne.preprocessing import ICA
from mne import Epochs, events_from_annotations, pick_types
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
from sklearn.model_selection import ShuffleSplit, cross_val_score
from sklearn.pipeline import Pipeline
from mne.io import concatenate_raws, read_raw_edf

mne.viz.set_browser_backend("matplotlib")


class EEG:
    def __init__(self, file_path=None):
        if file_path != None:
            self.file_path = file_path
            self.raw = self.load_edf_data(self.file_path)

    # Loading the EDF raw data
    def load_edf_data(self, file_path):
        self.ica_bool = False
        self.psd_bool = False
        self.file_path = file_path
        # Load the .edf data from the file and return it as raw data
        self.raw = mne.io.read_raw_edf(file_path, preload=True)
        self.montage()
        return self.raw

    # Reseting the raw file
    def reset_raw(self):
        # Reloading the raw file in order to reset it
        self.raw = self.load_edf_data(self.file_path)
        message = "Changes successfully reverted."
        show_popup_message("SUCCSESS", message)

    # Set Montage
    def montage(self):
        # Needs work
        eegbci.standardize(self.raw)  # Set channel names
        montage = make_standard_montage("standard_1005")
        self.raw.set_montage(montage)

    # PSD
    def power_spectral_density(self):
        # Compute the power spectral density of raw data and plot
        self.raw.compute_psd().plot(average=True, picks="data", exclude="bads")
        self.psd_bool = True
        message = "PSD applied succesfully."
        show_popup_message("SUCCSESS", message)
        plt.show()
        return True
    
    #add psd plot here

    # PSD - Channel(s)
    def power_spectral_density_channels(self, picks=None):
        if self.psd_bool == True:
            # Plot a power spectral density of raw data for a specific channel(s)
            self.raw.compute_psd().plot(picks=picks, exclude="bads")

            plt.show()
            return True
        else:
            message = "Please apply PSD first"
            show_popup_message("ERROR", message)
            print("PSD has not been calculated")
            return False

    # PSD - Topomap
    def topomap_PSD(self):
        if self.psd_bool == True:
            # Plot topomap (heatmap) of power spectral density of raw data
            self.raw.compute_psd().plot_topomap()

            plt.show(block=True)
            return True
        else:
            message = "Please apply PSD first"
            show_popup_message("ERROR", message)
            print("PSD has not been calculated")
            return False

    # Filtering - Band-pass
    def bandpass_filtering(
        self, low_frq=7.0, high_frq=13.0, fir_design="firwin", skip_by_annonation="edge"
    ):
        # Apply band-pass filter
        self.raw.filter(
            low_frq,
            high_frq,
            fir_design=fir_design,
            skip_by_annotation=skip_by_annonation,
        )
        message = "Bandpass filter applied succesfully."
        show_popup_message("SUCCSESS", message)
        self.raw.plot()
        plt.show()
        return True

    # Filtering - Low pass
    def lowpass_filtering(self, high_frq=30.0, fir_design="firwin"):
        low_frq = None
        self.raw.filter(low_frq, high_frq, fir_design=fir_design)
        message = "Lowpass filter applied succesfully."
        show_popup_message("SUCCSESS", message)
        self.raw.plot()
        plt.show()
        return True

    # Filtering - High pass
    def highpass_filtering(self, low_frq=20.0, fir_design="firwin"):
        high_frq = None  # High frq limit
        self.raw.filter(low_frq, high_frq, fir_design=fir_design)
        message = "Highpass filter applied succesfully."
        show_popup_message("SUCCSESS", message)
        self.raw.plot()
        plt.show()
        return True

    # Electrodes
    def plot_electrodes(self):
        # Plot sensor (electrode) locations on a head
        self.raw.plot_sensors(ch_type="eeg", show_names=True)
        plt.show()
        return True

    # ICA - Preprocessing
    def preprocessing_ICA(self, n_components=20, random_state=97, max_iter=800):
        # Apply ICA to Raw data
        self.ica = ICA(
            n_components=n_components, random_state=random_state, max_iter=max_iter
        )
        self.ica.fit(self.raw)
        self.ica_bool = True
        message = "ICA Preprocessing applied"
        show_popup_message("SUCCSESS", message)
        return True

    # ICA - Components 1D Series
    def plot_ica_components_1D(self, picks=None):
        # Plot the 1D time series of each ICA component
        if self.ica_bool == True:
            self.ica.plot_sources(
                self.raw, picks=picks, title="ICA - Components 1D Series"
            )

            plt.show()
            return True
        else:
            message = "Please apply ICA Preprocessing first"
            show_popup_message("ERROR", message)
            return False

    # ICA - Components Topomap
    def plot_ica_components_topomap(self, picks=None):
        if self.ica_bool == True:
            # Plot Ica Components Topomap
            self.ica.plot_components(picks=picks, title="ICA Components Topomap")

            plt.show()
            return True
        else:
            print("Plase apply ICA Preprocessing first")
            message = "Please apply ICA Preprocessing first"
            show_popup_message("ERROR", message)
            return False

    # ICA - Components' Properties
    def plot_ica_components_properties(self, picks=None):
        if self.ica_bool == True:
            # Plot ICA components' Properties
            self.ica.plot_properties(self.raw, picks=picks)  # picks = self.ica.exclude
            return True
        else:
            print("Plase apply ICA Preprocessing first")
            message = "Please apply ICA Preprocessing first"
            show_popup_message("ERROR", message)
            return False

    # Common Spatial Pattern - CSP
    def common_spatial_pattern(self, n_components=10, tmin=-0.2, tmax=0.5, event_id = None):
        print(n_components)
        print(tmin)
        print(tmax)
        #tmin, tmax = -1.0, 4.0
        #event_id = dict(hands=2, feet=3)
        #subject = 1
        #runs = [6, 10, 14]  # motor imagery: hands vs feet

        #raw_fnames = eegbci.load_data(subject, runs)
        #self.raw = concatenate_raws([read_raw_edf(f, preload=True) for f in raw_fnames])
        #eegbci.standardize(self.raw)  # set channel names
        #montage = make_standard_montage("standard_1005")
        #self.raw.set_montage(montage)

        events, _ = events_from_annotations(self.raw, event_id=event_id)#dict(T1=2, T2=3))

        picks = pick_types(self.raw.info, meg=False, eeg=True, stim=False, eog=False, exclude="bads")

        # Read epochs (train will be done only between 1 and 2s)
        # Testing will be done with a running classifier
        epochs = Epochs(
            self.raw,
            events,
            event_id=event_id,
            tmin=tmin,
            tmax=tmax,
            proj=True,
            picks=picks,
            baseline=None,
            preload=True,
        )
        epochs_train = epochs.copy().crop(tmin=tmin, tmax=tmax)
        labels = epochs.events[:, -1] - 2
        
        # Apply CSP
        scores = []
        epochs_data = epochs.get_data()
        epochs_data_train = epochs_train.get_data()
        cv = ShuffleSplit(10, test_size=0.2, random_state=42)
        cv_split = cv.split(epochs_data_train)

        # Assemble a classifier
        lda = LinearDiscriminantAnalysis()
        csp = CSP(n_components=n_components, reg=None, log=True, norm_trace=False)

        # Use scikit-learn Pipeline with cross_val_score function
        clf = Pipeline([("CSP", csp), ("LDA", lda)])
        scores = cross_val_score(clf, epochs_data_train, labels, cv=cv, n_jobs=None)

        # Printing the results
        class_balance = np.mean(labels == labels[0])
        class_balance = max(class_balance, 1.0 - class_balance)
        print(
            "Classification accuracy: %f / Chance level: %f" % (np.mean(scores), class_balance)
        )

        # plot CSP patterns estimated on full data for visualization
        csp.fit_transform(epochs_data, labels)

        csp.plot_patterns(epochs.info, ch_type="eeg", units="Patterns (AU)", size=1.5)