
import { Route, Redirect } from 'react-router-dom';

import React, { useState, useEffect ,useLayoutEffect} from "react";
import { useStateValue } from '../data/StateProvider';
import { actionTypes } from "../data/reducer"

const PrivateRoute = ({ component: Component, ...rest }) => {
  const [{user}, dispatch] = useStateValue();
  useLayoutEffect(()=>{
    dispatch({
      type: actionTypes.SET_USER,
      user: JSON.parse(localStorage.getItem('userdetail')),
   });
  },[])
     return (
   <>
    <Route {...rest} render={props => ( localStorage.getItem('userdetail') ? <Component {...props} /> :  
    <Redirect to="/signin" />)} />   
    </>                      
)}


export default PrivateRoute;