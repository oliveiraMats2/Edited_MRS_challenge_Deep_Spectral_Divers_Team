# Edited_MRS_challenge_Deep_Spectral_Divers_Team

This repository contains the code for the Deep Spectral Divers team's submission to the Edited-MRS Reconstruction Challenge. It enables inference using the models used in the challenge, aiming to reconstruct GABA spectra faster by utilizing less data compared to current Edited-MRS scans.

## Challenge Description

Edited Magnetic Resonance Spectroscopy (MRS) is used to quantify metabolites that are overlapped by those of higher concentration in typical scans. The challenge focused on quantifying Gamma Aminobutyric Acid (GABA), which is overlapped by creatine and glutamate. High-quality data in Edited-MRS scans requires long scan times. The challenge proposed the use of machine learning models to reconstruct spectra using three quarters less data, enabling four times faster Edited-MRS scans.

Participants in the challenge were provided with simulated and in vivo data training sets representing GABA-edited MEGA-PRESS scans composed of two subspectra (ON and OFF). Scripts for data augmentation, including adding noise, frequency, and phase shifts, were also provided. The models submitted by the teams were evaluated on simulated data, homogeneous in vivo data (single-vendor), and heterogeneous in vivo data (multi-vendor) using quantitative metrics such as mean squared error, signal-to-noise ratio, linewidth, and peak shape.

The results of the challenge were summarized and submitted for a joint publication

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
   
3. Check the Python version and Install the required dependencies:

    ```bash
   pip install -r requirements.txt
   
## Usage

Prepare the input files:

1. Ensure you have the tracks dataset in the right .h5 format
2. Run the script:

For Tracks 01 and 02:

    python script.py [config_file] [weights] [test_data_path] [save_file_path]

Replace [config_file] with the path to the YAML configuration for the track.

Replace [weights] with the path to the weights file for the track.

Replace [test_data_path] with the path to the track .h5 file containing the test dataset.

3. The script will perform inference on each sample in the test dataset using the model.

4. The predicted spectra and ppm values will be saved in an output file named track01.h5 located in the folder [save_file_path] provided.


## Citation

If you use our model inference in your research please cite


      Deep Spectral Divers. (2023). Code repository for the Deep Spectral Divers team's submission to the Edited-MRS Reconstruction Challenge. Retrieved from https://github.com/oliveiraMats2/Edited_MRS_challenge_Deep_Spectral_Divers_Team (Dias, G., Ueda, L., Costa, P., Rittner, L,Oliveira, M., Dertkigil, S.). 
 
