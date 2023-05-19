# Edited_MRS_challenge_Deep_Spectral_Divers_Team

This repository contains the code for the Deep Spectral Divers team's submission to the Edited-MRS Reconstruction Challenge. It enables inference using the models used in the challenge, aiming to reconstruct GABA spectra faster by utilizing less data compared to current Edited-MRS scans. For each Track we trained a separate model, ending with four final models: Track 01, Track 02, Track 03 with 2048 data points and Track 03 with 4096 data points.

## Challenge Description

Edited Magnetic Resonance Spectroscopy (MRS) is used to quantify metabolites that are overlapped by those of higher concentration in typical scans. The challenge focused on quantifying Gamma Aminobutyric Acid (GABA), which is overlapped by creatine and glutamate. High-quality data in Edited-MRS scans requires long scan times. The challenge proposed the use of machine learning models to reconstruct spectra using three quarters less data, enabling four times faster Edited-MRS scans.

Participants in the challenge were provided with simulated and in vivo data training sets representing GABA-edited MEGA-PRESS scans composed of two subspectra (ON and OFF). Scripts for data augmentation, including adding noise, frequency, and phase shifts, were also provided. The models submitted by the teams were evaluated on simulated data, homogeneous in vivo data (single-vendor), and heterogeneous in vivo data (multi-vendor) using quantitative metrics such as mean squared error, signal-to-noise ratio, linewidth, and peak shape.

The results of the challenge were summarized and submitted for a joint publication

Challenge webpage: https://sites.google.com/view/edited-mrs-rec-challenge/home?authuser=0

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Citation](#citation)

## Installation

1. Clone the repository:

   ```bash
   git clone [repository_url]

2. Navigate to the project directory:

   ```bash
   cd [project_directory]
   
3. Check the Python version in requirements.txt and install the required dependencies:

    ```bash
   pip install -r requirements.txt
   
## Usage

Getting the predictions from the models:

1. Ensure you have the tracks dataset in the right .h5 format
2. Run the script:

Instructions for **Tracks 01 and 02**:

    python save_predicts_track01.py [config_file] [weights] [test_data_path] [save_folder_path]

or 

    python save_predicts_track02.py [config_file] [weights] [test_data_path] [save_folder_path]

Replace [config_file] with the path to the YAML configuration for the track.

Replace [weights] with the path to the weights file for the track.

Replace [test_data_path] with the path to the track .h5 file containing the test dataset.

Replace [save_folder_path] with the folder path which the predict .h5 file will be saved.

Instructions for **Track 03**:

    python save_predicts_track03.py [config_file_down] [config_file_up] [weights_down] [weights_up] [test_data_path] [save_folder_path]


Replace [config_file_down] with the path to the YAML configuration for the track 03 downsampled (2048).

Replace [config_file_up] with the path to the YAML configuration for the track 03 upsampled (4096).

Replace [weights_down] with the path to the weights file for the track 03 downsampled (2048).

Replace [weights_up] with the path to the weights file for the track 03 upsampled (4096).

Replace [test_data_path] with the path to the track .h5 file containing the test dataset.

Replace [save_folder_path] with the folder path which the predict .h5 file will be saved.

3. The script will perform inference on each sample in the test dataset using the model.

4. The predicted spectra and ppm values will be saved in an output file named track01.h5, track02.h5, or track03.h5, depending on the respective script. These files will be located in the folder [save_folder_path] provided.


## Citation

If you use our model inference in your research please cite


      Deep Spectral Divers. (2023). Code repository for the Deep Spectral Divers team's submission to the Edited-MRS Reconstruction Challenge. Retrieved from https://github.com/oliveiraMats2/Edited_MRS_challenge_Deep_Spectral_Divers_Team (Dias, G., Ueda, L., Costa, P., Rittner, L,Oliveira, M., Dertkigil, S.). 
 
