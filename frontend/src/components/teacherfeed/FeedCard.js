import React from 'react'

function FeedCard() {
  return (
    <div className="container mx-auto py-8">

      <div className="bg-white shadow-md rounded-md p-4 mb-4">
        <div className="flex justify-between items-center mb-4">
          <div className="flex items-center">
            <img src="teacher-avatar.jpg" alt="Teacher's Profile Picture" className="w-10 h-10 rounded-full"/>
              <div className="ml-3">
                <p className="font-semibold text-lg">Teacher's Name</p>
                <p className="text-gray-500">Course Name</p>
              </div>
          </div>
          <p className="text-gray-500">Posted 2 hours ago</p>
        </div>
        <p className="text-gray-800">Lorem ipsum dolor sit amet, consectetur adipiscing elit. Nullam non urna nec turpis bibendum iaculis.</p>
        <div className="mt-4">
          <button className="text-gray-500 hover:text-blue-500 mr-4">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 10h16M4 14h16M4 18h16"></path>
            </svg>
            Like
          </button>
          <button className="text-gray-500 hover:text-blue-500">
            <svg xmlns="http://www.w3.org/2000/svg" className="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor">
              <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 6h16M4 12h16M4 18h16"></path>
            </svg>
            Comment
          </button>
        </div>
      </div>

    </div>

  )
}

export default FeedCard