import Head from 'next/head'
import Image from 'next/image'

import FirstHalf from "../components/firsthalf";

import SecondHalf from "../components/secondhalf";

export default function Home() {
  return (
    <>
  
  <div className="">
      <div className="w-1/2 h-full relative">
        <Image src="/bg.png" alt="Your Image" layout="fill" objectFit="cover" />
      </div>
      <div className="w-1/2 h-full bg-black text-white flex items-center justify-center">
        <div className="text-center">
          <h1 className="text-4xl font-bold">Title</h1>
          <p className="text-xl mt-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et mauris nec nisl tincidunt pharetra. Proin dignissim ex sit amet urna dignissim suscipit.</p>
        </div>
      </div>
    </div>
    </>
  )
}
