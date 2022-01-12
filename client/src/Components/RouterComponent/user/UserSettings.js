import React,{useEffect} from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import { Box } from "@material-ui/core";
import { AppBar } from "@material-ui/core";

import Dummy from "./Dummy"

const useStyles = makeStyles((theme) => ({
    root: {
      flexGrow: 1,
      backgroundColor: theme.palette.background.paper,
      display: "flex",
    //   height: "80vh",
      padding: "auto",
    },
    tabs: {
      borderRight: `1px solid ${theme.palette.divider}`,
    },
  }));
  

function TabPanel(props) {
    const { children, value, index, ...other } = props;
  
    
    return (
      <div
        role="tabpanel"
        hidden={value !== index}
        id={`vertical-tabpanel-${index}`}
        aria-labelledby={`vertical-tab-${index}`}
        {...other}
      >
        {value === index && (
          <Box p={1}>
            <div>{children}</div>
          </Box>
        
        )}
      
      </div>
    );
  }
export default function SimpleTabs() {
    const classes = useStyles();
    const [value, setValue] = React.useState(0);
  
    const handleChange = (event, newValue) => {
      setValue(newValue);
    };
  
    return (
      <div className={classes.root}>
        
        <AppBar position="static" >
          <Tabs value={value} onChange={handleChange} aria-label="simple tabs example"  >
            <Tab label="Manage App" style={{width:"20%"}} />
            <Tab label="Access Control" style={{width:"20%"}}/>
            <Tab label="Custom Fields"  style={{width:"20%"}}/>
            <Tab label="Custom Columns" style={{width:"20%"}}/>
          </Tabs>
        </AppBar>
        <TabPanel value={value} index={0}>
        < Dummy/>
        </TabPanel>
        <TabPanel value={value} index={1}>
        < Dummy/>
        </TabPanel>
        <TabPanel value={value} index={2}>
        < Dummy/>
        </TabPanel>
        <TabPanel value={value} index={3}>
        < Dummy/>
        </TabPanel>
      </div>
    );
  }