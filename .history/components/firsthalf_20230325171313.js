import React from 'react'

const firsthalf = () => {
  return (
    <div className="flex w-full h-screen">
      <div className="w-1/2 h-full bg-cover bg-center" style={{ backgroundImage: "url('/your-image.jpg')" }}></div>
      <div className="w-1/2 h-full flex items-center justify-center bg-black text-white">
        <div className="text-center">
          <h1 className="text-4xl font-bold">Title</h1>
          <p className="text-xl mt-4">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam et mauris nec nisl tincidunt pharetra. Proin dignissim ex sit amet urna dignissim suscipit.</p>
        </div>
      </div>
    </div>
  )
}

export default firsthalf