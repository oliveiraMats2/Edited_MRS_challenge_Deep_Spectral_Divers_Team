# Edited_MRS_challenge_Deep_Spectral_Divers_Team

This repository contains the code for the Deep Spectral Divers team's submission to the Edited-MRS Reconstruction Challenge. The objective of the challenge is to investigate machine learning models that can reconstruct spectra using significantly less data than current Edited-MRS scans, resulting in faster scan times.

## Challenge Description

Edited Magnetic Resonance Spectroscopy (MRS) is used to quantify metabolites that are overlapped by those of higher concentration in typical scans. The challenge focused on quantifying Gamma Aminobutyric Acid (GABA), which is overlapped by creatine and glutamate. High-quality data in Edited-MRS scans requires long scan times. The challenge proposed the use of machine learning models to reconstruct spectra using three quarters less data, enabling four times faster Edited-MRS scans.

Participants in the challenge were provided with simulated and in vivo data training sets representing GABA-edited MEGA-PRESS scans composed of two subspectra (ON and OFF). Scripts for data augmentation, including adding noise, frequency, and phase shifts, were also provided. The models submitted by the teams were evaluated on simulated data, homogeneous in vivo data (single-vendor), and heterogeneous in vivo data (multi-vendor) using quantitative metrics such as mean squared error, signal-to-noise ratio, linewidth, and peak shape.

The results of the challenge were summarized and submitted for a joint publication

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Permissions and citations](#Permissions and citations)

## Installation

1. Clone the repository:

   ```bash
   git clone [repository_url]

2. Navigate to the project directory:

   ```bash
   cd [project_directory]
   
3. Install the required dependencies:

    ```bash
   pip install -r requirements.txt

## Permissions and citations

If you use our model inference in your research please cite

 
