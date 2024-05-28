# <span style="color: grey;"> SeismoAugment: A Comprehensive Data Augmentation Python Toolkit for Deep Learning </span>


The **SeismoAugment** toolkit addresses a significant challenge in seismological studies: the limited availability of region- and depth-specific labeled data. This scarcity poses a preliminary drawback when applying deep learning and machine learning techniques. To enhance model performance, we propose data augmentation as a simple yet effective solution.

## Getting Started

### Clone the Repository Locally

To clone the repository to your local machine, use the following command:

```bash
git clone https://github.com/ISR-AIML/SeismoAugment.git
```

### Running in Google Colab

1. Open a new notebook in Google Colab.
2. Execute each step individually in separate cells using the following commands:

```python
!git clone https://github.com/ISR-AIML/SeismoAugment
%cd SeismoAugment
!pip install -r requirements.txt  # After restarting the session
%cd SeismoAugment
%run SeismoAugment.ipynb
```

### Installation Via pip

```bash
pip install -r requirements.txt
```

### Installation Via Conda

Choose one of the following options:

1. Create a Conda environment from the provided environment.yml file:

```python
conda env create -f environment.yml
```

2. Alternatively, install the dependencies directly from the requirements.txt file:

```python
conda install --file requirements.txt
```

## Example mseed files provided in the Repo are from **SCEDC**

**_SCEDC (2013): Southern California Earthquake Data Center. Caltech. Dataset. doi:10.7909/C3WD3xH1._**

![White_noise](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/db64d62e-beed-481d-a6f7-039bd1169669)
_Example of adding random noise at levels 20%, 40%, 60%, and 80% to the signal._

![bandpass_noise](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/98f3a745-1ed7-4f2d-83d9-afff27dba0f6)
_Example of adding non-periodic noise in the range of 15-30 Hz. Changes in frequency content of the added noise can be observed in the corresponding signal._

![mono_freq](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/614712ff-da18-44c8-a63d-efc8746c0de5)
_Example of adding periodic noise at 30 Hz, change in frequency content of added noise can be observed in the corresponding spectrograms._

[email]: isr3aiml@gmail.com
