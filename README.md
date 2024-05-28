**SeismoAugment:** _A comprehensive Data Augmentation Python Toolkit  as a gateway to Deep Learning_
The present toolkit is developed to address the significant challenge of limited Region and depth specific labeled data  in seismological studies, a preliminary drawback in the application of deep learning and machine learning. 
Data augmentation has emerged as a simple but effective solution to this problem to enhance model performance. 

## To clone the repository :
  git clone https://github.com/ISR-AIML/SeismoAugment.git

**Installation Via pip**
```
pip install -r requirements.txt
```
**Installation Via Conda**
```
conda env create -f environment.yml
```
or
```
conda install --file requirements.txt
```

The Example mseed file provided in the Repo are from **SCEDC** 
**_SCEDC (2013): Southern California Earthquake Data Center. Caltech. Dataset. doi:10.7909/C3WD3xH1._**

![White_noise](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/db64d62e-beed-481d-a6f7-039bd1169669)
_Example of adding Random Noise of levels 20%, 40%, 60%, 80% to signal._
![bandpass_noise](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/98f3a745-1ed7-4f2d-83d9-afff27dba0f6)
_Example of adding Non-periodic noise of range 15-30 Hz, change in frequency content of added noise can be observed in the corresponding spectrograms._
![mono_freq](https://github.com/ISR-AIML/SeismoAugment/assets/163402495/614712ff-da18-44c8-a63d-efc8746c0de5)
_Example of adding periodic noise at 30 Hz, change in frequency content of added noise can be observed in the corresponding spectrograms._
[email]: isr3aiml@gmail.com
