import React from "react";

import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import { makeStyles } from "@material-ui/core/styles";
import Avatar from "@material-ui/core/Avatar";
import { deepOrange, deepPurple } from "@material-ui/core/colors";

import ApiService from "../../Sevices/ApiService";
import ApiUrl from "../../ServerApi";
import DispBoard from "./DispBoard";

function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
  root: {
    width: "80rem",
    marginLeft: "5%",
    "& > * + *": {
      marginTop: theme.spacing(2),
    },
  },
  orange: {
    color: theme.palette.getContrastText(deepOrange[500]),
    backgroundColor: deepOrange[500],
  },
  purple: {
    color: theme.palette.getContrastText(deepPurple[500]),
    backgroundColor: deepPurple[500],
  },
}));

const DashBoard = (props) => {
  const classes = useStyles();
  const [data, setData] = React.useState({});
  const [open, setOpen] = React.useState(false);
  const [message, setMessage] = React.useState(null);

  React.useEffect(() => {
    ApiService.fetchUserById(window.localStorage.getItem("userId")).then(
      (res) => {
        let user = res.data;
        //console.log(data);
        data._id = user._id;
        data.studentName = user.studentName;
        data.runID = user.runID;
        data.labType = user.labType;
        data.experimentName = user.experimentName;
        setData({ ...data });
        //console.log(data);
      }
    );

    playingUser();
  }, []);

  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  const goBack = () => {
    window.localStorage.removeItem("userId");
    props.history.push("/app");
  };

  const playingUser = () => {
    setMessage(
      `RunId ${window.localStorage.getItem("userId")} experiment is encaged...`
    );
    setOpen(true);
  };

  return (
    <div className={classes.root}>
      <button
        title="Exit"
        onClick={goBack}
        style={{
          border: "none",
          background: "none",
          zIndex: 100000,
          position: "absolute",
          top: 10,
          right: 10,
        }}
      >
        <Avatar className={classes.purple}>
          {`${data.studentName}`.substring(0, 2)}
        </Avatar>
      </button>
      <DispBoard data={data} />
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>
    </div>
  );
};

export default DashBoard;
