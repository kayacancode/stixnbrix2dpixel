import React from 'react'
import  Image from 'next/image'
const SecondHalf = () => {
  return (
    <div className="relative h-screen">
    <div className="">
        <Image
            src="/bg.png"
            alt="background image"
            fill
        />
    </div>
   
</div>
  )
}

export default SecondHalf