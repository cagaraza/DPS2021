import requests 

# sample submission content format for DPS 2021 AI Engineer Challenge
# {
# "github":"https://github.com/ACCOUNT/REPO",
# "email":"EMAIL",
# "url":"DEPLOYED_ENDPOINT", 
# "notes":"NOTES" // Not mandatory
# }

# POST https://dps-challenge.netlify.app/.netlify/functions/api/challenge
# Authorization: Basic 0942804753 
# Content-Type: application/json 

url = 'https://cagarazadps2021.ey.r.appspot.com/'
data={'github': 'https://github.com/cagaraza/DPS2021', 'email': 'cagaraza@gmail.com', 'url': 'https://cagarazadps2021.ey.r.appspot.com/', 'notes': 'Model deployed are for the three categories and type insgesamt. SARIMA is utilized due to the time-series nature of data. Training data utilized is until year 2020. Main SDK for data exploration and modeling is Jupyter Notebook. Deployment platform of choice is GCP Gcloud SDK'}
response = requests.post(url, data)
response.json()


