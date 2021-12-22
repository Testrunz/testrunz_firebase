import React from 'react'
import { auth, provider } from "./firebase";
import Button from '@mui/material/Button';
import { useStateValue } from '../data/StateProvider';
import { useHistory, Link } from "react-router-dom";

import { actionTypes } from "../data/reducer"
const Google1 = () => {
  const [{ user }, dispatch] = useStateValue();
  const history = useHistory()
  const googlesignin = () => {
    auth.signInWithPopup(provider)
      .then((result) => {
        console.log("user", result);
        const email = result.user.email
        const name = result.user.displayName
        console.log("success")

        fetch(`${process.env.REACT_APP_API}/google_login`, {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({
            email: email,
            name: name
          }),
        }).then(response => response.json())
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
                history.push("/private");
              })

          })
          .catch((error) => {
            console.error('Error:', error);
          });

      })

      .catch((error) => alert(error.message))
  }

  return (
    <div>
      <Button variant="contained" color="error"style={{backgroundColor:"#EA4335"}} onClick={googlesignin} > Google</Button>
    </div>
  )
}

export default Google1
