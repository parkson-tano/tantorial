import React from 'react'

function TeacherUpcoming() {
  return (
    <div className="bg-gray-100 mx-3">
      <div className="container mx-auto">
        <div className="max-w-lg mx-auto bg-white rounded-lg shadow-lg overflow-hidden">

          <div className="bg-blue-500 text-white py-4 px-6">
            <h2 className="text-2xl font-semibold">Upcoming Course</h2>
          </div>


          <div className="py-4 px-6">
            <h3 className="text-xl font-semibold text-gray-800">Course Title</h3>
            <p className="text-gray-600 text-sm mt-2">Course Description Lorem ipsum dolor sit amet, consectetur adipiscing elit.</p>


            <div className="mt-4">
              <p className="text-gray-700">
                <span className="font-semibold">Date:</span> September 20, 2023
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Time:</span> 10:00 AM - 12:00 PM
              </p>
              <p className="text-gray-700">
                <span className="font-semibold">Location:</span> Online
              </p>
            </div>
          </div>


          <div className="bg-gray-100 py-4 px-6 border-t border-gray-300">
            <a href="#" className="text-blue-500 hover:underline mr-4">View Details</a>
            <a href="#" className="text-blue-500 hover:underline">Edit Course</a>
          </div>
        </div>
      </div>
    </div>
  )
}

export default TeacherUpcoming