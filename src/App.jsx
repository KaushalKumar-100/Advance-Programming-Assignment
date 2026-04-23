import React, { useState } from "react";
import "./App.css";

const availableCourses = ["DS", "AP", "TOC", "CAO", "DBMS", "OS", "CN", "Java"];

function App() {
  const [students, setStudents] = useState(new Map());

  const [studentName, setStudentName] = useState("");
  const [rollNo, setRollNo] = useState("");
  const [cgpa, setCgpa] = useState("");
  const [selectedCourses, setSelectedCourses] = useState([]);

  const [filterCourse, setFilterCourse] = useState("");
  const [filterStudent, setFilterStudent] = useState("");

  // Select maximum 4 subjects
  const handleCourseChange = (course) => {
    if (selectedCourses.includes(course)) {
      setSelectedCourses(selectedCourses.filter((c) => c !== course));
    } else {
      if (selectedCourses.length < 4) {
        setSelectedCourses([...selectedCourses, course]);
      } else {
        alert("You can select maximum 4 subjects only");
      }
    }
  };

  // Add student
  const addStudent = () => {
    if (
      studentName.trim() === "" ||
      rollNo.trim() === "" ||
      cgpa.trim() === "" ||
      selectedCourses.length === 0
    ) {
      alert("Please fill all fields");
      return;
    }

    const newStudent = {
      id: Date.now(),
      name: studentName,
      rollNo,
      cgpa: parseFloat(cgpa).toFixed(2),
      enrolledCourses: new Set(selectedCourses),
    };

    const newMap = new Map(students);
    newMap.set(newStudent.id, newStudent);

    setStudents(newMap);

    // Reset fields
    setStudentName("");
    setRollNo("");
    setCgpa("");
    setSelectedCourses([]);
  };

  const removeStudent = (id) => {
    const newMap = new Map(students);
    newMap.delete(id);
    setStudents(newMap);
  };

  const studentList = [...students.values()];

  // Sort by CGPA (highest first)
  const sortedStudents = [...studentList].sort(
    (a, b) => b.cgpa - a.cgpa
  );

  // Unique courses
  const uniqueCourses = studentList.reduce((acc, student) => {
    student.enrolledCourses.forEach((course) => acc.add(course));
    return acc;
  }, new Set());

  // Filter by student name + course
  const filteredStudents = sortedStudents.filter((student) => {
    const matchCourse = filterCourse
      ? student.enrolledCourses.has(filterCourse)
      : true;

    const matchStudent = filterStudent
      ? student.name.toLowerCase().includes(filterStudent.toLowerCase())
      : true;

    return matchCourse && matchStudent;
  });

  return (
    <div className="container">
      <h1>Student Course Enrollment Dashboard</h1>

      <div className="input-section">
        <input
          type="text"
          placeholder="Enter Student Name"
          value={studentName}
          onChange={(e) => setStudentName(e.target.value)}
        />

        <input
          type="text"
          placeholder="Enter Roll Number"
          value={rollNo}
          onChange={(e) => setRollNo(e.target.value)}
        />

        <input
          type="number"
          placeholder="Enter CGPA"
          value={cgpa}
          onChange={(e) => setCgpa(e.target.value)}
        />

        <div className="courses">
          {availableCourses.map((course) => (
            <label key={course} className="course-tag">
              <input
                type="checkbox"
                checked={selectedCourses.includes(course)}
                onChange={() => handleCourseChange(course)}
              />
              {course}
            </label>
          ))}
        </div>

        <button onClick={addStudent}>Add Student</button>
      </div>

      <h2>Filters</h2>

      <div className="input-section">
        <input
          type="text"
          placeholder="Filter by Student Name"
          value={filterStudent}
          onChange={(e) => setFilterStudent(e.target.value)}
        />

        <input
          type="text"
          placeholder="Filter by Course"
          value={filterCourse}
          onChange={(e) => setFilterCourse(e.target.value)}
        />
      </div>

      <h2>Unique Courses</h2>

      <div className="courses">
        {[...uniqueCourses].map((course, index) => (
          <span key={index} className="course-tag">
            {course}
          </span>
        ))}
      </div>

      <h2>Students</h2>

      {filteredStudents.map((student) => (
        <div key={student.id} className="card">
          <p><b>ID:</b> {student.id}</p>
          <p><b>Name:</b> {student.name}</p>
          <p><b>Roll No:</b> {student.rollNo}</p>
          <p><b>CGPA:</b> {student.cgpa}</p>

          <div className="courses">
            {[...student.enrolledCourses].map((course) => (
              <span key={course} className="course-tag">
                {course}
              </span>
            ))}
          </div>

          <button
            className="remove-btn"
            onClick={() => removeStudent(student.id)}
          >
            Remove
          </button>
        </div>
      ))}
    </div>
  );
}

export default App;
