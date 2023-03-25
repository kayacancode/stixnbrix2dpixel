import React from 'react'
import  Image from 'next/image'
const FirstHalf = () => {
  return (
    <div className="relative h-screen">
    <div className="absolute inset-0">
        <Image
            src="/bg.png"
            alt="background image"
            fill
        />
    </div>
   
</div>
  )
}

export default FirstHalf