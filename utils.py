import yaml
import numpy as np
import h5py
from scipy import signal

def read_yaml(file: str) -> yaml.loader.FullLoader:
    with open(file, "r") as yaml_file:
        configurations = yaml.load(yaml_file, Loader=yaml.FullLoader)

    return configurations

class ReadDatasets:
    def read_h5_sample_track_3(filename: str) -> tuple[np.ndarray, np.ndarray, np.ndarray, np.ndarray,
    np.ndarray, np.ndarray]:
        with h5py.File(filename) as hf:
            input_ppm_down = hf['data_2048']["ppm"][()]
            input_t_down = hf['data_2048']["t"][()]
            input_transients_down = hf['data_2048']["transient_fids"][()]

            input_ppm_up = hf['data_4096']["ppm"][()]
            input_t_up = hf['data_4096']["t"][()]
            input_transients_up = hf['data_4096']["transient_fids"][()]

        return input_transients_down, input_ppm_down, input_t_down,\
        input_transients_up, input_ppm_up, input_t_up


    @staticmethod
    def read_h5_sample_track_1(filename: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        with h5py.File(filename) as hf:
            ppm = hf["ppm"][()]
            t = hf["t"][()]
            transients = hf["transients"][()]

        return transients, ppm, t

    @staticmethod
    def read_h5_sample_track_2(filename: str) -> tuple[np.ndarray, np.ndarray, np.ndarray]:
        with h5py.File(filename) as hf:
            ppm = hf["ppm"][()]
            t = hf["t"][()]
            transients = hf['transient_fids'][()]

        return transients, ppm, t

    @staticmethod
    def write_h5_track1_predict_submission(filename: str,
                                           spectra_predict: np.ndarray,
                                           ppm: np.ndarray):
        """
        Save the results in the submission format
        Parameters:
            - results_spectra (np.array): Resulting predictions from test in format scan x spectral points
            - ppm (np.array): ppm values associataed with results, in same format
            - filename (str): name of the file to save results in, should end in .h5

        """
        with h5py.File(filename, "w") as hf:
            hf.create_dataset("result_spectra", spectra_predict.shape, dtype=float, data=spectra_predict)
            hf.create_dataset("ppm", ppm.shape, dtype=float, data=ppm)

    @staticmethod
    def write_h5_track2_predict_submission(filename: str,
                                           spectra_predict: np.ndarray,
                                           ppm: np.ndarray):
        """
        Save the results in the submission format
        Parameters:
            - results_spectra (np.array): Resulting predictions from test in format scan x spectral points
            - ppm (np.array): ppm values associataed with results, in same format
            - filename (str): name of the file to save results in, should end in .h5

        """
        with h5py.File(filename, "w") as hf:
            hf.create_dataset("result_spectra", spectra_predict.shape, dtype=float, data=spectra_predict)
            hf.create_dataset("ppm", ppm.shape, dtype=float, data=ppm)
    @staticmethod
    def write_h5_track3_predict_submission(filename:str,
                                            spectra_predict_down: np.ndarray,
                                            ppm_down: np.ndarray,
                                            spectra_predict_up: np.ndarray,
                                            ppm_up: np.ndarray):
        with h5py.File(filename, "w") as hf:
            hf.create_dataset("result_spectra_2048", spectra_predict_down.shape, dtype=float,
                              data=spectra_predict_down)
            hf.create_dataset("ppm_2048", ppm_down.shape, dtype=float, data=ppm_down)
            hf.create_dataset("result_spectra_4096", spectra_predict_up.shape, dtype=float,
                              data=spectra_predict_up)
            hf.create_dataset("ppm_4096", ppm_up.shape, dtype=float, data=ppm_up)




def transform_spectrogram_2D(FID, t, window_size=256, hope_size=64, window='hann', nfft=None):
    # calculating the overlap between the windows
    noverlap = window_size - hope_size

    # checking for the NOLA criterion
    if not signal.check_NOLA(window, window_size, noverlap):
        raise ValueError("signal windowing fails Non-zero Overlap Add (NOLA) criterion; "
                         "STFT not invertible")
    fs = 1 / (t[1] - t[0])
    # computing the STFT
    _, _, Zxx = signal.stft(np.real(FID), fs=fs, nperseg=window_size, noverlap=noverlap,
                            return_onesided=True, nfft=nfft)

    Zxx = Zxx / (np.max(np.abs(Zxx)))
    return Zxx

def pad_zeros_spectrogram(X_dcb, output_shape=(224, 224)):
    matrix = X_dcb
    pad_width = ((0, output_shape[0] - matrix.shape[0]), (0, output_shape[1] - matrix.shape[1]))
    padded_matrix = np.pad(matrix, pad_width, mode="constant")
    return padded_matrix


