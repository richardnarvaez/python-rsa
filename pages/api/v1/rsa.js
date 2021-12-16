// Next.js API route support: https://nextjs.org/docs/api-routes/introduction
const { exec } = require('child_process')

export default async function handler(req, res) {
   console.log('Empieza la ejecucion de la llamada a la API')
   const childPython = await exec('python3', ['rsa.py', '1', '2'])
   console.log('Lo hizo')

   // console.log('stdout:', childPython.stdout)
   // console.error('stderr:', childPython.stderr)

   await childPython.stdout.on('data', (data) => {
      console.log(`stdout: ${data.toString()}`)
   })

   console.log('SE PASO')

   childPython.stderr.on('data', (data) => {
      console.error(`stderr: ${data}`)
   })

   childPython.on('exit', (code) => {
      res.status(200).json({ name: code })
      console.log(`child process exited with code ${code}`)
   })

   childPython.stdin.pipe('hola')
   res.status(200).json({ name: 'John Doe' })
}
