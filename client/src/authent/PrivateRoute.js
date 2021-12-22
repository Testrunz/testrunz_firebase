
import { Route, Redirect } from 'react-router-dom';

import React, { useState, useEffect } from "react";
import { useStateValue } from '../data/StateProvider';
import { actionTypes } from "../data/reducer"

const PrivateRoute = ({ component: Component, ...rest }) => {
    
     return (
   <>
    <Route {...rest} render={props => ( localStorage.getItem('userdetail') ? <Component {...props} /> :  
    <Redirect to="/signin" />)} />   </>                      
)}


export default PrivateRoute;