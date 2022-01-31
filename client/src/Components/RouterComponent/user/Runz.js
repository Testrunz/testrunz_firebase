import React, { useEffect, useState, useContext } from "react";

import axios from "axios";

import Divider from "@mui/material/Divider";

import AddCircleOutlineIcon from "@material-ui/icons/AddCircleOutline";

import { DataGrid } from "@material-ui/data-grid";

import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";

import Modal from "react-modal";

import ApiUrl from "../../../ServerApi";
import ApiService from "../../../Sevices/ApiService";

import AddUserComponent from "./AddUserComponent";
import EditUserComponent from "./EditUserComponent";

import { useStateValue } from "../../../data/StateProvider";
import MaterialTable from 'material-table';


import {FaRegEdit} from 'react-icons/fa';
import Loading from "./Lodaing"


function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

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
      return;
    }

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

  const editUser = (id) => {
    //window.localStorage.clear();
    window.localStorage.setItem("userId", id);
    openModale();
    console.log("this is id", id);
  };

  const playUser = (id) => {
    window.localStorage.removeItem("userId");
    window.localStorage.setItem("userId", id);
    props.history.push(`/userdash/${id}`);
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
        //time:toString(userr.time) ,
        time: Date(userr.time),

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
        style={customStyles}
        contentLabel="Example Modal"
      >
        <EditUserComponent closeModale={closeModale} />
      </Modal>
      <div style={{ maxWidth: '100%' }}>
        {loadingscreen ?<Loading/>:
        <MaterialTable
          columns={columns1}
          data={rows}
          title="Runz"
          onRowClick= {(e,data) => playUser(data.ProcedureId)}
          actions={[
           {
              icon: () => <FaRegEdit/>,
              tooltip: "Edit",
              onClick: (e, data) => editUser(data.ProcedureId)
            },

          ]}
          editable={{
            onRowDelete: (selectedRow) => new Promise((resolve, reject) => {
              deleteUser(selectedRow.ProcedureId)
              console.log(selectedRow)
              setTimeout(() => resolve(), 500);
            }),

          }}
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
            }
          ]} 
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