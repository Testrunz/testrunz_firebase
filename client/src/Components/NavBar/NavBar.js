import React ,{useState,useEffect, useLayoutEffect}from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import { useStateValue } from '../../data/StateProvider';
import { actionTypes } from "../../data/reducer"
import { GiSoapExperiment } from 'react-icons/gi';
import { BiLogOutCircle } from 'react-icons/bi';
import Typography from '@mui/material/Typography';
import Grid from '@mui/material/Grid';
import "./Navbar.css"
import IconButton from '@mui/material/IconButton';
import MenuIcon from '@mui/icons-material/Menu';
import { useHistory, Link } from "react-router-dom";
import Menu from '@mui/material/Menu';
import MenuItem from '@mui/material/MenuItem';
import InnerNav from './InnerNav';
import OuterNav from './OuterNav';
import IntermediateNav from './IntermediateNav';


const useStyles = makeStyles((theme) => ({
  root: {

   width:"100%",

   display:"block"
  },

  
}));

export default function NavBar() {
  const classes = useStyles();
  const [{user}, dispatch] = useStateValue();
  useLayoutEffect(()=>{
    dispatch({
      type: actionTypes.SET_USER,
      user: JSON.parse(localStorage.getItem('userdetail')),
   });
  
  },[])

 

  return (
     <div className={classes.root}>
      {console.log(user)}
      {user ? user.showOnce ? <InnerNav/> : <IntermediateNav/> :  <OuterNav/> }
    </div>
  );
}



