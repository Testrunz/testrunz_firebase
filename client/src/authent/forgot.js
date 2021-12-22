import React, { useState } from "react";
import { auth } from "./firebase";
import template from "./template.png"
import { useHistory, Link } from "react-router-dom";
import Button from '@mui/material/Button';


import "./signup.css"


import Alert from '@mui/material/Alert';
import Snackbar from '@mui/material/Snackbar';

const Forgot = () => {
  const [email, setEmail] = useState("");
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




  const clickSubmit = (event) => {
    
    event.preventDefault();
   console.log("change password");
   auth.sendPasswordResetEmail(email)
  .then(() => {
    setOpen1(true);

    window.setTimeout(() => {
      history.push('/signin')
    }, 3000)
  })
  .catch((error) => {
    var errorCode = error.code;
    var errorMessage = error.message;
    console.log("1",errorCode)
    console.log("2",errorMessage)
    setStatusmessage(errorMessage)
    setOpen(true);
  });
  };

  return (

    <div>
    <section>
      <div class="container">
        <div class="user signinupBx">
        <div class="imgBx"><img src={template} alt="" /></div>
          <div class="formBx">
            <form >
              <h2>Forget Password</h2>
              <input
                onChange={e => setEmail(e.target.value)}
                type="email"
                value={email}
                placeholder="Email"
              />
             

             <Button  variant="contained" onClick={clickSubmit}>send</Button>
            
            </form>
            
          </div>
        </div>
      </div>
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}  anchorOrigin={{ vertical, horizontal }}>
        <Alert onClose={handleClose} severity="error" sx={{ width: '100%' }}>
          {statusmessage}
        </Alert>
      </Snackbar>

      <Snackbar open={open1} autoHideDuration={6000} onClose={handleClose} anchorOrigin={{ vertical, horizontal }}> 
        <Alert onClose={handleClose} severity="success" sx={{ width: '100%' }}>
          Reset link sent to your email {email} 
        </Alert>
      </Snackbar>
    </section>

  </div>




















  );
};

export default Forgot;
