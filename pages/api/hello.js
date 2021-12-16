// Next.js API route support: https://nextjs.org/docs/api-routes/introduction

import axios from 'axios'

export default function handler(req, res) {
   console.log('sasas', req.query)
   const { message, pub_key } = req.query
   console.log('sasas', message, pub_key)
   const options = {
      method: 'GET',
      url: 'https://60aw1qb0w9.execute-api.us-east-2.amazonaws.com/ptyhon-rsa',
      headers: { 'Content-Type': 'application/json', 'Access-Control-Allow-Origin': '*' },
      data: JSON.stringify({ message, pub_key }),
   }

   axios
      .request(options)
      .then(function (response) {
         console.log(response.data)
         res.status(200).json({ result: response.data.result })
      })
      .catch(function (error) {
         console.error(error)
         res.status(404)
      })
}
