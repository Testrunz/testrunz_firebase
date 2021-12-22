
import { useStateValue } from '../../../data/StateProvider';


import React, { useState, useEffect } from "react";
import axios from "axios";
import { ToastContainer, toast } from "react-toastify";
import "react-toastify/dist/ReactToastify.min.css";
import { useHistory, Link } from "react-router-dom";
import MenuItem from '@material-ui/core/MenuItem';
import Select from '@material-ui/core/Select';
import Button from '@mui/material/Button';

import ApiUrl from "../../../ServerApi";
import { actionTypes } from "../../../data/reducer"
const Userprofile = () => {

  const [{ user }, dispatch] = useStateValue();
  const history = useHistory()
  const [editbt, setEditbt] = useState(false)

  const [credit, setCredit] = useState({
    designation: user.designation,
    collegeName: user.collegeName,
    department: user.department,
    country: user.country,
    state: user.state,
    year: user.year,
    semester: user.semester,
    btnText: "Submit",
    _id: user._id,
  });


  const {
    designation,
    collegeName,
    department,
    country,
    state,
    year,
    semester,
    btnText,
    _id,
  } = credit;

  const handleChange = (name) => (event) => {
    setCredit({ ...credit, [name]: event.target.value, });
  };



  const clickSubmit = (event) => {
    event.preventDefault();

    setCredit({ ...credit, btnText: "Submitting" });
    fetch(`${process.env.REACT_APP_API}/users/update`, {
      method: "PATCH",
      headers: {
        "Content-Type": "application/json"
      },
      body: JSON.stringify({
        designation,
        collegeName,
        department,
        country,
        state,
        year,
        semester,
        _id,
      }),
    })
      .then(response => response.json())
      .then(data => {
        console.log(data.updated)
        localStorage.setItem("userdetail", JSON.stringify(data.updated))
                dispatch({
                  type: actionTypes.SET_USER,
                  user: JSON.parse(localStorage.getItem('userdetail')),
                })
        setCredit({
          ...credit,
          designation: user.designation,
          collegeName: user.collegeName,
          department: user.department,
          country: user.country,
          state: user.state,
          year: user.year,
          semester: user.semester,
          btnText: "Submit",
        });
        setEditbt(!editbt)
        console.log("noerror");
      })
      .catch((error) => {
        console.error('Error:', error);
      });
  }



  return (
    <div>

      <Button variant="contained" color="primary" style={{ alignItems: "right" }} onClick={() => setEditbt(!editbt)}>edit</Button>
      <br />

      <hr />
      {editbt ?

        <div>
          <form>
            <div className="form-group">
              <label className="text-muted">Designation</label>
              <Select
                labelId="demo-simple-select-label"
                id="demo-simple-select"
                value={designation}
                onChange={handleChange("designation")}
                // text={text.postTo}
                className="form-control"
                name="postTo">
                <MenuItem value="student">Student</MenuItem>
                <MenuItem value="teacher">Teacher</MenuItem>
                <MenuItem value="admin">Admin</MenuItem>
              </Select>
            </div>



            <div className="form-group">
              <label className="text-muted">College Name</label>
              <input
                onChange={handleChange("collegeName")}
                type="text"
                className="form-control"
                value={collegeName}
              />
            </div>
            <div className="form-group">
              <label className="text-muted">Department</label>
              <input
                onChange={handleChange("department")}
                type="text"
                className="form-control"
                value={department}
              />
            </div>
            <div className="form-group">
              <label className="text-muted">Country</label>
              <input
                onChange={handleChange("country")}
                type="text"
                className="form-control"
                value={country}
              />
            </div>
            <div className="form-group">
              <label className="text-muted">State</label>
              <input
                onChange={handleChange("state")}
                type="text"
                className="form-control"
                value={state}
              />
            </div>
            {credit.designation === "student" && (
              <>
                <div className="form-group">
                  <label className="text-muted">Year</label>
                  <input
                    onChange={handleChange("year")}
                    className="form-control"
                    value={year}
                    type="number"
                    min="1"
                    max="4"
                  />
                </div>
                <div className="form-group">
                  <label className="text-muted">Semester</label>
                  <input
                    onChange={handleChange("semester")}
                    className="form-control"
                    value={semester}
                    type="number"
                    min="1"
                    max="8"
                  />
                </div>
              </>
            )}
            <br />
            <div style={{ alignItems: "center" }}>
              <button className="btn btn-primary" onClick={clickSubmit}>
                {btnText}
              </button>
              <br />

            </div>
          </form>
        </div>
        :
        <div>
          <span>Name:</span>

          <span>{user.name}</span>
          <br />

          <span>Email:</span>
          <span>{user.email}</span>
          <br />
          <span>Designation:</span>
          <span>{user.designation}</span>
          <br />
          <span>CollegeName:</span>
          <span>{user.collegeName}</span>
          <br />
          <span>Department:</span>
          <span>{user.department}</span>
          <br />
          <span>Role:</span>
          <span>{user.role}</span>
          <br />
          <span>Country:</span>
          <span>{user.country}</span>
          <br />
          <span>State:</span>
          <span>{user.state}</span>
          <br />
          <span>Year:</span>
          <span>{user.year}</span>
          <br />
          <span>Semester:</span>
          <span>{user.semester}</span>
        </div>


      }


    </div>
  );
};

export default Userprofile;
