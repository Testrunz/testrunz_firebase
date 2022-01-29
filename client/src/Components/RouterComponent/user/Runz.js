import React, { useEffect, useState, useContext } from "react";

import axios from "axios";

import Divider from "@mui/material/Divider";

import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";

import { DataGrid } from "@material-ui/data-grid";
import TextField from "@material-ui/core/TextField";

import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import Typography from "@material-ui/core/Typography";

import Modal from "react-modal";

import ApiUrl from "../../../ServerApi";
import ApiService from "../../../Sevices/ApiService";

import AddUserComponent from "./AddUserComponent";
import EditUserComponent from "./EditUserComponent";

import { useStateValue } from "../../../data/StateProvider";
import MaterialTable from 'material-table';


import {FaRegEdit} from 'react-icons/fa';
import {RiShareForwardFill} from 'react-icons/ri';

import Loading from "./Lodaing"
import { Button } from "@material-ui/core";


function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const style = {
  marginTop: "55px",
  display: "flex",
  justifyContent: "center",
};


const useStyles = makeStyles((theme) => ({
  root: {
    width: "70vw",
    height: "70vh",
    maxWidth: "75vw",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },
  tablecontainer: {
    borderRadius: "15px",
    overflowX: "hidden",
  },
  tableCellhead: {
    fontWeight: "bold",
    backgroundColor: "#3F51B5",
    align: "center",
    // color:theme.palette.getContrastText(theme.palette.primary.dark)
  },
  tableCellbody: {
    fontWeight: "bold",
    align: "center",

    // color:theme.palette.getContrastText(theme.palette.primary.dark)
  },
  buttons: {
    "&:hover": {
      backgroundColor: "grey",
    },
  },
}));

const customStyles = {
  content: {
    top: "50%",
    left: "50%",
    width: "50%",
    height: "55%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
};

const customStylesshare = {
  content: {
    top: "50%",
    left: "50%",
    width: "30%",
    height: "35%",
    right: "auto",
    bottom: "auto",
    marginRight: "-50%",
    transform: "translate(-50%, -50%)",
    borderRadius: "2%",
  },
};


const customStylescell = {
  content: {
    color: "red",
    backgroundColor: "black",
  },
};
const fetchuser = async () => {
  let ress = await ApiService.fetchUsers();
  console.log("rkijriotjioprjtfgjeriogj", ress);
  return ress;
};

const Runz = (props) => {
  let rows = [];
  const [{ user }, dispatch] = useStateValue();
  const classes = useStyles();
  const [open, setOpen] = React.useState(false);
  const [users, setUsers] = useState([]);
  const [message, setMessage] = useState(null);
  const [modalOpenAdd, setModalOpenAdd] = useState(false);
  const [modalOpenEdit, setModalOpenEdit] = useState(false);
  const [loadingscreen, setLoadingscreen]=useState(true)
  const [sharewith, setSharewith]=useState("")
  const [datatoshare, setDatatoshare]=useState({})
  const columns1 = [
    { title: "ID", field: "id" },
    { title: "Procedure Name", field: "ProcedureName"  },
    // { title: "Template Id", field: "TemplateId" },
    // { title: "Experiment Name", field: "ExperimentName" },
     { title: "Lab Name", field: "labname" },
    { title: "Procedure ID    ", field: "ProcedureId" ,sorting:false },
    { title: "Description", field: "description" },
    { title: "Created Time", field: "time" },
  ];

  const [page, setPage] = React.useState(0);
  const [rowsPerPage, setRowsPerPage] = React.useState(10);
  const handleChangePage = (event, newPage) => {
    setPage(newPage);
  };


  const handleChangeRowsPerPage = (event) => {
    setRowsPerPage(+event.target.value);
    setPage(0);
  };


  // model setup
  const openModal = () => {
    // window.localStorage.clear();
    setModalOpenAdd(() => true);
  };

  const openModale = () => setModalOpenEdit(() => true);
  const closeModal = () => setModalOpenAdd(() => false);
  const closeModale = () => setModalOpenEdit(() => false);


  const value = async () => {
    const usersdum = await ApiService.fetchUsers().then((res) => res);
    console.log("asdsaddsadafdwfsfas", usersdum);
    setLoadingscreen(false)
    setUsers(() => usersdum.data.data);
  };


  useEffect(() => {
    value();
    console.log(user);
  }, [modalOpenAdd, modalOpenEdit]);

  
  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;  }
    setOpen(false);
  };

  const deleteUser = async (userId) => {
    await ApiService.deleteUser(userId).then(() => {
      setUsers((prevUser) => prevUser.filter((user) => user._id !== userId));
      setMessage("User deleted successfully.");
    });
    const deleteUser = users.find((user) => user._id === userId);
    await axios.delete(`${ApiUrl}/notes/${deleteUser.runID}`);
    setOpen(true);
  };

  // const editUser = (id) => {
  //   //window.localStorage.clear();
  //   window.localStorage.setItem("userId", id);
  //   openModale();
  //   console.log("this is id", id);
  // };

  const shareRunz =(data)=>{
    // window.localStorage.setItem("userId", id);
    openModale();
    setDatatoshare(data)
    console.log("this is iddetail", data);
    console.log("this is id", datatoshare);
  }
  
  
  const sharerunzwith =()=>{
    // window.localStorage.setItem("userId", id);
   
      let users={
         _id:datatoshare.ProcedureId,
          procedureDescription: datatoshare.description,
          labType: datatoshare.labname,
          experimentName: datatoshare.ProcedureName,
          sharewith:sharewith,
      }
      let usermail ={
        _id:datatoshare.ProcedureId,
         procedureDescription: datatoshare.description,
         labType: datatoshare.labname,
         experimentName: datatoshare.ProcedureName,
         sharewith:sharewith,
         name:user.name
     }


      closeModale()
    ApiService.editUser(users).then((res) => {
      setMessage("User Added successfully.");
      
    });
    ApiService.mailUser(usermail).then((res) => {
      console.log("mail sent successfully.");
      
    });
  }



  const playUser = (id) => {
    window.localStorage.removeItem("userId");
    window.localStorage.setItem("userId", id);
    props.history.push(`/userdash/${id}`);
    // console.log("runid runz page", id)
  };
  let individuals = users.filter(function (userr) {return userr.userid == user._id;}).reverse();
individuals.map((userr, ident) => {
   
      return rows.push({
        id: ident+1,
        ProcedureName: userr.experimentName,
        // TemplateId: userr.runID.slice(userr.runID.length - 12),
        // ExperimentName: userr.experimentName,
        labname:userr.labType,
        ProcedureId: userr._id,
        description:userr.procedureDescription,
        time:Date(userr.time) ,

      });

  });

  return (
    <div className={classes.root}>
    
      <Modal
        isOpen={modalOpenAdd}
        appElement={document.getElementById('root')}
        style={customStyles}
        contentLabel="add runz Modal"
        disableBackdropClick="true"
        sx={{ overflow: 'hidden' }}
        
      >
        <AddUserComponent closeModal={closeModal} />
      </Modal>

      <Modal
        isOpen={modalOpenEdit}
        onRequestClose={closeModale}
        style={customStylesshare}
        contentLabel="Example Modal"
        
      >
         <Typography variant="h4" style={style}>
        Share Runz
      </Typography>
      <br/><br/>
    {datatoshare.ProcedureId}
      <div >
     <label>Share With:</label>&nbsp;&nbsp;&nbsp;&nbsp;
              <TextField id="outlined-basic"  size="small" variant="outlined" value={sharewith} onChange={(e)=>setSharewith(e.target.value)} />
       
      </div> 
     <Button onClick={()=>sharerunzwith()}>Share</Button> 
      </Modal>
      <div style={{ maxWidth: '100%' }}>
        {loadingscreen ?<Loading/>:
        <MaterialTable
          columns={columns1}
          data={rows}
          title="Runz"
          onRowClick= {(e,data) => playUser(data.ProcedureId)}
     
          options={{
            actionsColumnIndex: -1, grouping:true,  pageSizeOptions:[5,10,15],pageSize:10,headerStyle: {
              zIndex:0
            }     
          }}
          localization={{
            pagination:{labelRowsSelect:"Runz"}
          }}
          actions={[
            {
              icon: 'add',
              tooltip: 'Add Runz',
              isFreeAction: true,
              onClick:() => openModal()
            },
            {
              icon: () => <RiShareForwardFill/>,
              tooltip: "Share",
               onClick: (e, data) => shareRunz(data)
              // onClick: (e, data) => alert(data.ProcedureId)
            },
          ]} 
          editable={{
            onRowDelete: (selectedRow) => new Promise((resolve, reject) => {
              deleteUser(selectedRow.ProcedureId)
              console.log(selectedRow)
              setTimeout(() => resolve(), 500);
            }),

          }}
        />
        }
      </div>
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>


    </div>
  );
};

export default Runz;
