
import React from 'react';
import Drawer from '@mui/material/Drawer';
import Typography from '@mui/material/Typography';
// import { makeStyles } from '@mui/styles';
import { makeStyles } from '@material-ui/core/styles';

import List from '@mui/material/List';
import ListItemButton from '@mui/material/ListItemButton';
import ListItemIcon from '@mui/material/ListItemIcon';
import ListItemText from '@mui/material/ListItemText';
import { ListItem } from '@material-ui/core';
import PlayCircleOutlineIcon from '@material-ui/icons/PlayCircleOutline';
import AssignmentTurnedInIcon from '@material-ui/icons/AssignmentTurnedIn';
import AccountCircleIcon from '@material-ui/icons/AccountCircle';
import SettingsIcon from '@material-ui/icons/Settings';
import ListIcon from '@material-ui/icons/List';
import PersonIcon from '@mui/icons-material/Person';
import { useHistory ,useLocation} from "react-router-dom";
import Divider from '@mui/material/Divider';
// import Navbar from "../../NavBar/NavBar"
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import { useStateValue } from '../../../data/StateProvider';
import InnerNav from '../../NavBar/InnerNav';
import PrivateNav from '../../NavBar/PrivateNav';
import OuterNav from '../../NavBar/OuterNav';
// import SettingsIcon from '@mui/icons-material/Settings';
import InventoryIcon from '@mui/icons-material/Inventory';
import HelpIcon from '@mui/icons-material/Help';
const drawerWidth= 200


    const useStyles = makeStyles((theme)=>{
        return {
            drawer:{
                width:drawerWidth
            },
            page:{
                width:"100%",
                padding:theme.spacing(3)
        
            },
            drawerpaper:{
                width:drawerWidth
            },
            root:{
                display:'flex'
            },
            active:{
                backgroundColor:"#F1C232",
                color:"#fff",
            },
            appbar:{
                width:`calc(100% - ${drawerWidth}px)`,
                backgroundColor:"#fff",
                color:"#000",
              
            },
            appbaro:{
                width:`100%`,
                backgroundColor:"#fff",
                color:"#000",
              
            },
            toolbar: theme.mixins.toolbar,
     
        }
     
      });
      




const Sidelayout = ({children}) => {
    const classes= useStyles()  
    const history = useHistory()
    const location = useLocation()
    const [{ user }, dispatch] = useStateValue();
    const menuItem =[
        {
            text:"My Page",
            icon:<ListIcon/>,
            path:"/app"
        },
        {
            text:"Runz",
            icon:<PlayCircleOutlineIcon/>,
            path:"/runz"
        },
        {
            text:"Procedure",
            icon:<AssignmentTurnedInIcon/>,
            path:"/procedure"
        },
        {
            text:"Inventry",
            icon:<InventoryIcon/>,
            path:"/inventry"
        },
    ]
    const menuItem2 =[
        {
            text:"Settings",
            icon:<SettingsIcon/>,
            path:"/settings"
        },
        {
            text:"Support",
            icon:<HelpIcon/>,
            path:"/support"
        },
        {
            text:"Profile",
            icon:<AssignmentTurnedInIcon/>,
            path:"/profile"
        },
    ]


  return (
      <div className={classes.root}>

{user ? user.showOnce ? 
// inside the app
       <AppBar className={classes.appbar}  elevation={1}>
          <InnerNav/>
       </AppBar>
:
// inprivate page for restriction
       <AppBar className={classes.appbaro}  elevation={1}>
        <PrivateNav/>
       </AppBar>
:
// outerpage
       <AppBar className={classes.appbaro}  elevation={1}>
         <OuterNav/>
       </AppBar>
}

  {user ? user.showOnce ?   <Drawer  
        className={classes.drawer}
        variant="permanent"
        anchor="left"
        classes={{paper:classes.drawerpaper}}
      >
<List>
<ListItem  sx={{ flexGrow: 1 }}>
            <ListItemIcon><PersonIcon/></ListItemIcon>
            <ListItemText primary={user.name}/>
        </ListItem>
        <Divider/>
   
    {menuItem.map(item=>(
        <ListItem 
         button 
        key={item.text}
        onClick={()=>history.push(item.path)}
        className={location.pathname== item.path ? classes.active : null}
       
        >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text}/>
        </ListItem>
       
    ))} 
    <br/>
  <Divider/>
  <br/>   <br/>  
     {menuItem2.map(item=>(
        <ListItem 
         button 
        key={item.text}
        onClick={()=>history.push(item.path)}
        className={location.pathname== item.path ? classes.active : null}
     
       
        >
            <ListItemIcon>{item.icon}</ListItemIcon>
            <ListItemText primary={item.text}/>
        </ListItem>
       
    ))}

   
</List>



    
      </Drawer> :null:null }
      <div className={classes.page}>
          <div className={classes.toolbar}></div>
      {children}
      </div>
  </div>
  );
};

export default Sidelayout;

