import Head from 'next/head'
import Image from 'next/image'


export default function Home() {
  return (
    <>
     <div className="h-screen flex items-center justify-center">
      <Image
        src="/animated_bg.gif"
        alt="background image"
        
        layout="fill"
        objectFit="cover"
        objectPosition="center"
      />
      <h1 className="text-white text-4xl font-bold">Title</h1>
    </div>
    </>
  )
}