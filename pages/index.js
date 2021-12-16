import Head from 'next/head'
import Image from 'next/image'
import { useEffect, useState } from 'react'
import styles from '../styles/Home.module.css'

import axios from 'axios'
export default function Home() {
   const [cry, setCry] = useState(null)
   const [pub_key, setPub_key] = useState('')
   const [message, setMessage] = useState('')

   //  useEffect(() => {
   //     getData()
   //  }, [])

   const getData = async () => {
      console.log('sdasdasdasd', pub_key)
      console.log(message)
      const res = await fetch(
         `https://python-rsa.vercel.app/api/hello?message=${message}&pub_key=${pub_key}`
      )
      const data = await res.json()
      console.log(data)
      setCry(data)
   }

   return (
      <div className={styles.container}>
         <Head>
            <title>Create Next App</title>
            <meta name="description" content="Generated by create next app" />
            <link rel="icon" href="/favicon.ico" />
            {/* <script src="https://cdn.tailwindcss.com"></script> */}
         </Head>

         <main className={styles.main}>
            <h1>{cry && cry.result}</h1>
            <div>
               <input
                  id="message"
                  className="bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  "
                  placeholder="Message"
                  value={message}
                  onChange={(e) => {
                     setMessage(e.target.value)
                  }}
               />
            </div>

            <input
               id="pub"
               className="mt-3 bg-gray-50 border border-gray-300 text-gray-900 sm:text-sm rounded-lg focus:ring-blue-500 focus:border-blue-500 block w-full p-2.5  "
               placeholder="Public Key"
               value={pub_key}
               onChange={(e) => {
                  setPub_key(e.target.value)
               }}
            />
            <button
               onClick={getData}
               className="mt-4 bg-green-500 px-5 py-3 text-sm shadow-sm font-medium tracking-wider  text-green-100 rounded-full hover:shadow-2xl hover:bg-green-600"
            >
               Generate
            </button>
         </main>
      </div>
   )
}
