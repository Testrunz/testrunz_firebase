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
import AccountCircleIcon from '@material-ui/icons/AccountCircle';

import Avatar from '@mui/material/Avatar';




const useStyles = makeStyles({
    // logout: {
    //     marginRight:"205px",
    //     '&:hover': {
    //         cursor: 'pointer'
    //       },
    //       color:"white"
    // }, 
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
    const [anchorEl, setAnchorEl] = React.useState(null);
const [randomColor, setRandomColor] = React.useState();
    const handleClick = (event) => {
      setAnchorEl(event.currentTarget);
    };
  
    const handleClose = () => {
      setAnchorEl(null);
    };
    const runz = () => {
      window.localStorage.clear();
      setAnchorEl(null);
     return (window.location.href = "/");
    }
    const home = () => {
      window.localStorage.removeItem("userId");
     return (window.location.href = "/#/app");  
    }

    useEffect(() => {
 
      setRandomColor('#'+Math.floor(Math.random()*16777215).toString(16)) // # added
      console.log(randomColor)
    }, [])

    return (
        <div>
            <AppBar position="static" style={{ width: "100%" }}>
                <Toolbar>
                    <Typography onClick={home} className={classes.pointer} sx={{ flexGrow: 1 }} variant="h6" component="div" >TESTRUNZ </Typography>
                  
                    <Avatar  size="small"  style={{backgroundColor:randomColor,marginRight:"70px"}} className={classes.logout} onClick={handleClick}>
                    {`${user.name}`.substring(0, 2)}
</Avatar>


      {/* <button className={classes.logout} style={{color:"white"}} onClick={handleClick}>hello</button> */}
      <Menu
        id="simple-menu"
        anchorEl={anchorEl}
        keepMounted
        open={Boolean(anchorEl)}
        onClose={handleClose}
      >
        <MenuItem onClick={handleClose}>Profile</MenuItem>
        <MenuItem onClick={runz}>Logout</MenuItem>
      </Menu>

                 
            
                </Toolbar>
            </AppBar>

        </div>
    )
}

export default InnerNav
