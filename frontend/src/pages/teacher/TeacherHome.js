import React from 'react'
import TeacherTimeLine from '../../components/teacherfeed/TeacherTimeLine'
import FeedCard from '../../components/teacherfeed/FeedCard'
import TeacherUpcoming from '../../components/teacherfeed/TeacherUpcoming'

function TeacherHome() {
  return (
    <div className="container mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
      <div className="flex flex-col lg:flex-row">
        <div className="flex flex-col w-full lg:w-2/3 space-y-4">
          <TeacherTimeLine />
          <FeedCard />
        </div>
        <div className="flex flex-col w-full lg:w-1/3 space-y-5">
          <TeacherUpcoming />
        </div>
      </div>
      
    </div>
  )
}

export default TeacherHome