import Head from 'next/head'
import Image from 'next/image'

import FirstHalf from "../components/firsthalf";

import SecondHalf from "../components/secondhalf";

export default function Home() {
  return (
    <>
  
  <div className="">
    hello
     
        <Image src="/bg.png" alt="Your Image" layout="fill" objectFit="cover" />
      
     
    </div>
    </>
  )
}
