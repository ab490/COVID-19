# COVID-19
Analysis of COVID-19 data from various data sources and model time to the arrival of the next confirmed case of Covid-19 in India.

1. The data file Covid19IndiaData_.xlsx presents the Indian patient level data until 30th March 2020. I have written a python code to do the following: \
(i) Calculated and plotted the probability mass function (pmf) of the age of infected patients. Evaluated the expected age of an infected patient from this pmf and the variance of the pmf. \
(ii) Calculated and plotted the conditional pmfs of infected patients conditional to the patients being Recovered and Dead. Calculated the expectation and variance of the pmfs.\ 
(iii) Found the conditional pmf of the age of all infected patients conditional to the gender of the patient. 

2. The data file Covid19WorldData_.xlsx presents patient-level case data from China and other parts of the world. This includes the following information — Exposure date (E), Symptoms onset date (O), Hospitalisation date (H), and Date of death (X) in case of deceased patients. The data also includes whether the patient is/was a resident of Wuhan (China). I have written a python code to do the following: \
(i) Calculated and plotted the pmf of the incubation period, which is defined as the durationbetween the date of infection exposure (E) and the date of onset of symptoms (O).
Calculate the mean incubation period and the variance of the distribution. \
(ii) Calculated the expected incubation period by including and excluding Wuhan residents and compared the values. Then calculated the expected incubation period for surviving and deceased patients. \
(iii) Calculated the pmfs of the onset to hospitalization (H − O) for dead patients, onset to death (X − O) and hospitalization to death (X − H). Also, compared the H − O pmf for surviving and dead patients.

3. The exponential distribution is ideal to model waiting times. In this problem, I have used the exponential distribution to model time to the arrival of the next confirmed case of Covid-19 in India. Based upon data of confirmed cases from the source www.covid19india.org, between 17th April 2020 and 23rd April 2020, there were on average 1373 confirmed cases per day, i.e., on average around 57 cases per hour. I have written a python code to do the following:\
(i) Plotted the probability density function of the wait time for the next Covid-19 confirmed case.\
(ii) Found the probability of the wait time for the next Covid-19 confirmed case to be less than or equal to 1 minute.\
(iii) Found the probability of the wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes.\
(iv) Found the probability of the wait time for the next Covid-19 confirmed case to be more than 2 minutes.\
(v) Supposing the average number of cases per hour doubled, found the probability of wait time for the next Covid-19 confirmed case to be between 1 minute and 2 minutes.

