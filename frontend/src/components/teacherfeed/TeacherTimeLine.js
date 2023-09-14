import React from 'react'

function TeacherTimeLine() {
  return (
    <div className="min-h-auto bg-gray-100 flex justify-center">
      <div className="bg-white p-8 rounded-lg shadow-lg w-full">
        <h2 className="text-2xl font-semibold mb-4">Create a New Post</h2>


          <div className="mb-4">
            <label for="title" className="block text-gray-700 font-medium">Type of Content:</label>
            <select className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:border-blue-500">
              <option value="1">Lesson</option>
              <option value="2">Post</option>
              <option value="3">Remainder</option>
            </select>
          </div>
          <div className="mb-4">
            <label for="title" className="block text-gray-700 font-medium">Title:</label>
            <input
              type="text"
              id="title"
              name="title"
              className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:border-blue-500"
              placeholder="Enter the post title"
            />
          </div>
          <div className="mb-4">
            <label for="content" className="block text-gray-700 font-medium">Content:</label>
            <textarea
              id="content"
              name="content"
              rows="4"
              className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:border-blue-500"
              placeholder="Enter the post content"
            ></textarea>
          </div>
          <div className="mb-4">
            <label for="tags" className="block text-gray-700 font-medium">Tags:</label>
            <input
              type="text"
              id="tags"
              name="tags"
              className="w-full border border-gray-300 rounded px-3 py-2 focus:outline-none focus:border-blue-500"
              placeholder="Enter tags (comma-separated)"
            />
          </div>
          <div className="flex justify-end">
            <button
              type="submit"
              className="bg-blue-500 text-white rounded px-4 py-2 hover:bg-blue-600 focus:outline-none focus:bg-blue-600"
            >
              Create Post
            </button>
          </div>

      </div>
    </div>

  )
}

export default TeacherTimeLine