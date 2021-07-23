const hotpTotpGenerator = require('hotp-totp-generator');
secret_key = hotpTotpGenerator.totp({
    key: "cagaraza@gmail.comDPSCHALLENGE",
    x: 120,
    digits: 10,
    T0: 0,
    algorithm: 'sha512'
  });

console.log(secret_key);


const https = require('https')

data=JSON.stringify({
  'github': 'https://github.com/cagaraza/DPS2021',
  'email': 'cagaraza@gmail.com',
  'url': 'https://cagarazadps2021.ey.r.appspot.com/',
  'notes': 'Model deployed are for the three categories and type insgesamt. SARIMA is utilized due to the time-series nature of data. Training data utilized is until year 2020. Main SDK for data exploration and modeling is Jupyter Notebook. Deployment platform of choice is GCP Gcloud SDK'
})


var auth = 'Basic ' + Buffer.from(secret_key);
console.log(auth)
console.log(data)
const options = {
  auth: auth,
  hostname: 'dps-challenge.netlify.app',
  port: 443,
  path: '/.netlify/functions/api/challenge',
  method: 'POST',
  headers: {
    'Content-Type': 'application/json',
    'Content-Length': data.length,
    'Authorization': auth
  }
}

const req = https.request(options, res => {
  console.log(`statusCode: ${res.statusCode}`)

  res.on('data', d => {
    process.stdout.write(d)
  })
})

req.on('error', error => {
  console.error(error)
})
req.write(data)
req.end()