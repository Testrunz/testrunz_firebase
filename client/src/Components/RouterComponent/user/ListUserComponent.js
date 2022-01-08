import React,{useEffect} from "react";
import PropTypes from "prop-types";
import { makeStyles } from "@material-ui/core/styles";
import Tabs from "@material-ui/core/Tabs";
import Tab from "@material-ui/core/Tab";
import Box from "@material-ui/core/Box";


import Runz from "./Runz";
import Procedure from "./ProcedureList";
import User from "./User";
import Setup from "./Setup";



import { actionTypes } from '../../../data/reducer';
import { useStateValue } from '../../../data/StateProvider';
import Deleteaccount from "./Deleteaccount";


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

TabPanel.propTypes = {
  children: PropTypes.node,
  index: PropTypes.any.isRequired,
  value: PropTypes.any.isRequired,
};

function a11yProps(index) {
  return {
    id: `vertical-tab-${index}`,
    "aria-controls": `vertical-tabpanel-${index}`,
  };
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    backgroundColor: theme.palette.background.paper,
    display: "flex",
    height: "80vh",
    padding: "auto",
   
   
  },
  tabs: {
    borderRight: `1px solid ${theme.palette.divider}`,
  },
}));



const ListUserComponent = (props) => {
  const [value, setValue] = React.useState(0);
  const [{user}, dispatch] = useStateValue();
  
  const classes = useStyles();
  const handleChange = (event, newValue) => {
    setValue(newValue);
  };
 

  // useEffect(() => {
  //   dispatch({
  //     type: actionTypes.SET_USER,
  //      user: JSON.parse(localStorage.getItem('userdetail')),
  //  });
  //  console.log("check",localStorage.getItem('userdetail'))
  
  // },[])
    
  return (
    <div className={classes.root}>
 
 
      <Tabs
        orientation="vertical"
        value={value}
        onChange={handleChange}
        aria-label="Vertical tabs example"
        className={classes.tabs}
      >
       
        <Tab label="Runz" {...a11yProps(0)} />
        <Tab label="Procedure" {...a11yProps(1)} />
        <Tab label="User" {...a11yProps(2)} />
        <Tab label="Setup" {...a11yProps(3)} />

      </Tabs>
      <TabPanel value={value} index={0} >
        <Runz {...props} />
      </TabPanel>
      <TabPanel value={value} index={1}>
        <Procedure {...props} />
      </TabPanel>
      <TabPanel value={value} index={2}>
      <User {...props} />
      </TabPanel>
      <TabPanel value={value} index={3}>
        <Setup {...props} />
        <Deleteaccount/>
      </TabPanel>
 
     
     
    </div>
  );
};

export default ListUserComponent;
