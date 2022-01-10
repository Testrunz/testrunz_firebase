import React, { useState, useEffect, useLayoutEffect } from 'react';
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



const useStyles = makeStyles({
    logout: {
        paddingRight:"75px",
        '&:hover': {
            cursor: 'pointer'
          }
    }, 
    pointer: {

        '&:hover': {
            cursor: 'pointer'
          }
    }, 
 
  });



const InnerNav = () => {
    const classes = useStyles();

    const [{user}, dispatch] = useStateValue();
    const history = useHistory()
    
    const runz = () => {
      window.localStorage.clear();
      
     return (window.location.href = "/");
    }
    const home = () => {
     return (window.location.href = "/#/app");  
    }

    

    return (
        <div>
            <AppBar position="static" style={{ width: "100%" }}>
                <Toolbar>
                    <Typography onClick={home} className={classes.pointer} sx={{ flexGrow: 1 }} variant="h6" component="div" >TESTRUNZ </Typography>
                    <Typography onClick={runz} className={classes.logout} variant="h6" component="div">logout</Typography>
                </Toolbar>
            </AppBar>

        </div>
    )
}

export default InnerNav
