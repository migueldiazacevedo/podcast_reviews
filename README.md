# Podcast Reviews - 2 million reviews on 100k podcasts

---

## Overarching Investigation

- **What categories of podcasts are popular?**
- **What makes a 5-star podcast? What makes a 1-star podcast?**
- **How do reviewer tendencies vary and differ?**

---

## Technical Goals

1. **Working with a SQLite Database**
2. **Using Python-based Data Analysis Packages such as Pandas**
3. **Data Visualization**
4. **Hypothesis Testing and Statistical Inference**
5. **Making a Dashboard Using [Looker Studio](https://lookerstudio.google.com/reporting/4b70c021-6318-464d-aacb-676f92817f84)**

---

## Description

This project delves into a dataset containing 2 million reviews on 100k podcasts, available on Kaggle ([Podcast Reviews Dataset](https://www.kaggle.com/datasets/thoughtvector/podcastreviews/versions/28)). The analysis encompasses statistical examination of podcast ratings across various categories, employing both traditional statistical methods and resampling techniques like bootstrap and permutation procedures. Assumptions such as normality and independence of samples are rigorously assessed.

### Additional Analysis

- Analyze podcast ratings statistically across different categories using traditional statistics as well as bootstrap and permutation procedures.
- Assess statistical assumptions such as normality and independence of samples.
- Analyze the length of 1-star vs 5-star comedy podcasts.
- Compare paired non-parametric samples of podcast ratings on two podcasts.

---

## Conclusions

- **5-star reviews are the most common for all categories.**
- **Most podcasts are rated similarly (5-stars).**
- **Ratings are not normally distributed.**
- **Negatively reviewed podcast categories (e.g., News-Government) receive more 3-star reviews than positively reviewed podcast categories (e.g., Business).**
- **1-star reviews are slightly longer than 5-star reviews.**
- **People who rate two podcasts do so similarly.**

---

### Dependencies

- python>=3.10.13
  - ipython
  - jupyter
  - matplotlib
  - numpy
  - pandas
  - pyarrow
  - scipy
  - seaborn
  - statsmodels

see requirements.txt for more details and versions used in development environment

## Files Included

- `podcast_reviews.ipynb`: Jupyter Notebook containing the analysis code
- `podcast_utils.py`: Python script with utility functions
- `requirements.txt`: File containing the project dependencies
- `LICENSE`: [MIT](https://opensource.org/license/mit)

## Getting Started
1. Clone the repository 
   
2. Create a virtual environment using the requirements.txt file provided<br>
   e.g. 
```bash
python3 -m venv podcast_reviews/
# activate the venv and install all requirements provided 
source podcast_reviews/bin/activate
pip install -r requirements.txt
```
3. Open the Jupyter notebook file, podcast_reviews.ipynb, in your Jupyter environment and step through to see analysis.
   