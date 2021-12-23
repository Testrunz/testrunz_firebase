import React ,{useState,useEffect}from 'react';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Button from '@material-ui/core/Button';
import { useStateValue } from '../../data/StateProvider';
import { actionTypes } from "../../data/reducer"
import { GiSoapExperiment } from 'react-icons/gi';
import { BiLogOutCircle } from 'react-icons/bi';

const useStyles = makeStyles((theme) => ({
  root: {
   // flexGrow: 1,
   width:"100%",
   display:"block"
  },
  
}));

export default function NavBar() {
  useEffect(()=>{
    dispatch({
      type: actionTypes.SET_USER,
      user: JSON.parse(localStorage.getItem('userdetail')),
   });
  
  },[])
  const classes = useStyles();
 
  const [{user}, dispatch] = useStateValue();
  console.log(user)
  
  const runz = () => {
    window.localStorage.clear();
    
   return (window.location.href = "/");
  }
  const home = () => {
   return (window.location.href = "/#/app");  
  }
  const login  = (
    <>
    <Button onClick={home} color="inherit" >TESTRUNZ <GiSoapExperiment/> </Button>
    <Button onClick={runz} color="inherit"  edge="end">logout <BiLogOutCircle/></Button>
    
    </>
  )
  const logout  = (
    <Button onClick={runz} color="inherit"  >TESTRUNZ <GiSoapExperiment/></Button>
  )
 
  return (
     <div className={classes.root}>
      <div>
      
      <AppBar position="static" style={{width:"100%"}}>
        {/* <Toolbar className={classes.title}> */}
        <Toolbar >
        {user ? login : logout}
       
        </Toolbar>
      </AppBar>
    </div>
    </div>
  );
}



