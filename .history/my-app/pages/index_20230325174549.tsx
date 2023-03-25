import Head from 'next/head'
import Image from 'next/image'

import FirstHalf from "../components/firsthalf";

import SecondHalf from "../components/secondhalf";

export default function Home() {
  return (
    <>
  
  <div className="">
    
     
        <Image src="/bg.png" width={100} height={400} alt="Your Image"  />
      
     
    </div>
    </>
  )
}
