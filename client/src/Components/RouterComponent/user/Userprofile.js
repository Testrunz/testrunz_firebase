
import { useStateValue } from '../../../data/StateProvider';

import Divider from '@mui/material/Divider';
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

import Card from '@mui/material/Card';
import CardActions from '@mui/material/CardActions';
import CardContent from '@mui/material/CardContent';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
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
<div style={{display:"flex",justifyContent:"flex-end"}}>
      <Button variant="contained"  style={{ backgroundColor:"#F1C232",color:"black" }} onClick={() => setEditbt(!editbt)}>edit</Button>
      </div>
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
            <div >
              <Button style={{ backgroundColor:"#F1C232",color:"black" }} onClick={clickSubmit}>
                {btnText}
              </Button>
              <br />

            </div>
          </form>
        </div>
        :
        <div>

<Card>
  <CardContent style={{backgroundColor:"#E7EBF0"}}>
  <Grid container spacing={2} columns={16}>
  <Grid item xs={8}>
  <span style={{fontWeight: "bold"}}>Name:</span>
<br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.name}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Email:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.email}</span>
  </Grid>

  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Designation:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.designation}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>CollegeName:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.collegeName}</span>
  </Grid>

  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Department:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.department}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Role:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.role}</span>
  </Grid>
  
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Country:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.country}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>State:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.state}</span>
  </Grid>

  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Year:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.year ? user.year :"null"}</span>
  </Grid>
  <Grid item xs={8}>
  <span  style={{fontWeight: "bold"}}>Semester:</span>
  <br/>
<span style={{fontStyle: "italic",color:"gray"}}>{user.semester ? user.semester : "null" }</span>
  </Grid>
</Grid>




  </CardContent>
</Card>


          
          
        </div>


      }


    </div>
  );
};

export default Userprofile;
