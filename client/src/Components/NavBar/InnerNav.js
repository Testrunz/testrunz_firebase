import React from 'react';
import Typography from '@mui/material/Typography';
import Toolbar from '@material-ui/core/Toolbar';
import { useHistory ,useLocation} from "react-router-dom";
const InnerNav = () => {
  const history = useHistory()
  const runz = () => {
   history.push("/mypage");
  }
  const logout = () => {
    window.localStorage.clear();
    history.push("/mypage");
  }
  return (
  <div>
     <Toolbar>
             <Typography onClick={runz} sx={{ flexGrow: 1 }} > <span>Test</span><span style={{backgroundColor:"#F1C232"}}>RunZ</span></Typography>
           </Toolbar>
  </div>
  );
};

export default InnerNav;
