import React, { useState } from 'react'
import "./signup.css"
import template from "./template.png"
import Button from '@mui/material/Button';
import { auth } from "./firebase";
import { useHistory, Link } from "react-router-dom";
import { useStateValue } from '../data/StateProvider';
import { actionTypes } from "../data/reducer"

import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';
import Google1 from "./Google1"
const Signin = () => {

  const [email, setEmail] = useState("")
  const [password, setPassword] = useState("")
  const [{ user }, dispatch] = useStateValue();
  const history = useHistory()
  const [open, setOpen] = React.useState(false);
  const [open1, setOpen1] = React.useState(false);
  const [statusmessage, setStatusmessage] = useState("")
  const vertical ="button"
  const horizontal = "center"



  const handleClose = (event, reason) => {
    if (reason === 'clickaway') {
      return;
    }
    setOpen(false);
    setOpen1(false)
  };





  const authsignin = () => {
    auth.signInWithEmailAndPassword(email, password)
      .then((userCredential) => {
        console.log("successfully signin")
        fetch(`${process.env.REACT_APP_API}/login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
          }),
        })
          .then(response => response.json())
          .then(data => {
            console.log('Success:', data);


            fetch(`${process.env.REACT_APP_API}/users/${data.user._id}`)
              .then(res => res.json())
              .then(json => {
                localStorage.setItem("userdetail", JSON.stringify(json))
                console.log(typeof json)
                dispatch({
                  type: actionTypes.SET_USER,
                  user: JSON.parse(localStorage.getItem('userdetail')),
                });
                setOpen1(true);

              window.setTimeout(() => {
                history.push('/private')
              }, 3000)
              
              })
          })
          .catch((error) => {
            console.error('Error:', error);
          });

      })
      .catch((error) => {
        var errorCode = error.code;
        var errorMessage = error.message;
        console.log("Failure1", errorCode)
        console.log("Failure2", errorMessage)
        setStatusmessage(errorMessage)
        setOpen(true);
      });
  }



  return (
    <div>
      <section>
        <div class="container">
          <div class="user signinupBx">
            <div class="imgBx"><img src={template} alt="" /></div>
            <div class="formBx">
              <form >
                <h2>Sign In</h2>
                <input
                  onChange={e => setEmail(e.target.value)}
                  type="email"
                  value={email}
                  placeholder="Email"
                />
                <input
                  onChange={e => setPassword(e.target.value)}
                  type="password"
                  placeholder="Password"
                  value={password}
                />
                <Button  variant="contained" onClick={authsignin}>Submit</Button>

                <Google1/>
                <p class="signinup">
                  Don't have an account ?
                  <Link to="/signup" className="card-link" > Sign Up.</Link>
                </p>
                <br/>
                <br/>
                <p class="forget">
                <Link to="/forgot_password" className="card-link" > *Forget Password ?</Link>
                </p>
                </form>
                </div>

              
          
          </div>
        </div>
        <Snackbar open={open} autoHideDuration={6000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
          <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
            {statusmessage}
          </Alert>
        </Snackbar>

        <Snackbar open={open1} autoHideDuration={6000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}>
          <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
            SignIn Successful!
          </Alert>
        </Snackbar>
      </section>

    </div>
  )
}

export default Signin






