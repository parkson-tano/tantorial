import React from 'react'

function SubjectCreate() {
  return (
      <div className="container mx-auto mt-8 p-4">
          <h1 className="text-2xl font-bold mb-4">Manage Subjects</h1>
         
          <form className="mb-4">
              <div className="mb-2">
                  <label className="block text-gray-600" for="subjectName">Subject Name:</label>
                  <input type="text" id="subjectName" name="subjectName" className="w-full p-2 border border-gray-300 rounded"/>
              </div>
              <div className="mb-2">
                  <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Create Subject</button>
              </div>
          </form>
         
          <div className="mb-4">
              <h2 className="text-xl font-semibold mb-2">Subjects List</h2>
              <ul>
                  <li className="mb-2">
                      <span className="text-gray-800">Mathematics</span>
                      <span className="ml-2">
                          <button className="px-2 py-1 text-red-600 hover:text-red-800">Delete</button>
                          <button className="px-2 py-1 text-blue-600 hover:text-blue-800">Edit</button>
                      </span>
                  </li>
                  <li className="mb-2">
                      <span className="text-gray-800">Science</span>
                      <span className="ml-2">
                          <button className="px-2 py-1 text-red-600 hover:text-red-800">Delete</button>
                          <button className="px-2 py-1 text-blue-600 hover:text-blue-800">Edit</button>
                      </span>
                  </li>
            
              </ul>
          </div>
 
          <form className="mb-4 hidden">
              <div className="mb-2">
                  <label className="block text-gray-600" for="updatedSubjectName">Update Subject Name:</label>
                  <input type="text" id="updatedSubjectName" name="updatedSubjectName" className="w-full p-2 border border-gray-300 rounded"/>
              </div>
              <div className="mb-2">
                  <button type="submit" className="px-4 py-2 bg-blue-500 text-white rounded hover:bg-blue-600">Update Subject</button>
              </div>
          </form>
      </div>
  )
}

export default SubjectCreate