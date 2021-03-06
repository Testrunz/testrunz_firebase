

import React, { useState, useCallback, useEffect, useRef } from "react";
import path from "path";
import { Editor } from "@tinymce/tinymce-react";
import axios from "axios";
import { makeStyles } from "@material-ui/core/styles";
import ArrowBackIcon from "@material-ui/icons/ArrowBack";
import Snackbar from "@material-ui/core/Snackbar";
import MuiAlert from "@material-ui/lab/Alert";
import RefreshIcon from "@material-ui/icons/Refresh";
import Typography from "@material-ui/core/Typography";
import CardContent from "@material-ui/core/CardContent";
import Button from '@mui/material/Button';
import { nanoid } from "nanoid";
import Grid from '@material-ui/core/Grid';
import ApiUrl from "../../../ServerApi";

import "./procedure.css";

import Card from "@material-ui/core/Card";
import Swal from 'sweetalert2'
const initialValue = {
  experiment: "",
  lab: "",
  department: "",
  year: 0,
  college: "",
  semester:""
};

function Alert(props) {
  return <MuiAlert elevation={6} variant="filled" {...props} />;
}

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
    marginTop: "-2.5rem",
    marginLeft: "-3rem",
    // width: "123rem",
    "& > * + *": {
      marginTop: theme.spacing(5),
      marginLeft: theme.spacing(5),
    },
  },
}));

const App = (props) => {
  let content =
    props.location.pathname.replace("/editProce/", "") ||
    window.localStorage.getItem("proceId");

  const classes = useStyles();
  const titleRef = useRef();
  const labRef = useRef();
  const departmentRef = useRef();
  const yearRef = useRef();
  const collegeRef = useRef();
  const semesterRef = useRef();
  const [state, setState] = useState({ content: "" });
  const [state1, setState1] = useState(initialValue);
  const [open, setOpen] = useState(false);
  const [message, setMessage] = useState(null);

  const updateRef = useRef();
  const [update, setForceUpdate] = useState(false);

  const duplicate = (e) => {
    e.preventDefault();
    if (!titleRef.current.value ){
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Must Enter Experiment Name',
     
      })
    }
    else if (!labRef.current.value){
      Swal.fire({
        icon: 'error',
        title: 'Oops...',
        text: 'Must Enter Lab Name',
     
      })
    }
    else if (titleRef.current.value && labRef.current.value){

    axios
      .post(`${ApiUrl}/procedures`, {
        title: titleRef.current.value,
        html: state.content,
      })
      .then((res) => {
        axios
          .post(`${ApiUrl}/moreInfo`, {
            experimentno: res.data._id,
            experiment: titleRef.current.value,
            lab: labRef.current.value,
            department: departmentRef.current.value||"",
            year: yearRef.current.value||"",
            college: collegeRef.current.value||"",
          })
          .then(() => {
            // console.log("sent meta info");
            axios.post(`${ApiUrl}/labrotories`, {
              name: labRef.current.value,
              experiment: titleRef.current.value,
            })
            Swal.fire(
              'success',
              'Procedure has been Created',
              'success',
            )
            // setShowResults((prev) => !prev)
          })
          .catch((err) => {
            console.error(err)
            Swal.fire({
              icon: 'error',
              title: 'Oops...',
              text: 'Something went wrong Check your internet connection',
           
            })
          });

        setMessage("Template saved successfully.");
        setOpen(true);
      });


    }
    else {

    }
  };





  const handleClose = (event, reason) => {
    if (reason === "clickaway") {
      return;
    }

    setOpen(false);
  };

  const Results = (props) => (
    <Card className="blocks" style={{ backgroundColor: "#E7E9EB" ,position:"absolute",top:"120px",zIndex:10,paddingLeft:10,paddingRight:10}}>
      <CardContent>
        <p>Experiment Name: {state1.experiment ?? "Experiment Title"}</p>
        <input
          className="title"
          placeholder="Experiment Title"
          type="text"
          ref={titleRef}
        />
        <br />
        <br />
        <p>Lab Name: {state1.lab ?? "Lab Type"}</p>
        <input
          className="lab"
          placeholder="Lab Type"
          type="text"
          ref={labRef}
        />
        <br />
        <br />
        <p>Department Name: {state1.department ?? "Department"}</p>
        <input
          className="department"
          placeholder="Department"
          type="text"
          ref={departmentRef}
        />
        <br />
        <br />
        <p>Year: {state1.year ?? "year"}</p>
        <input
          className="year"
          placeholder="Year"
          type="text"
          ref={yearRef}
        />
        <br />
        <br />
        <p>Semester: {state1.semester ?? "year"}</p>
        <input
          className="semester"
          placeholder="Semester"
          type="text"
          ref={semesterRef}
        />
        <br />
        <br />
        <p>College: {state1.college ?? "College"}</p>
        <input
          className="college"
          placeholder="College"
          type="text"
          ref={collegeRef}
        />
        <br />
        <br />
        <br />
        <br />
        <Grid container spacing={1}>

        <Grid item xs={4}>
        <Button variant="contained"  style={{ backgroundColor:"#F1C232",color:"black" }}
          type="submit"
        >Save
          </Button>
          </Grid>

          <Grid item xs={4}>
        <Button variant="contained" style={{ backgroundColor:"#F1C232",color:"black"  }}
          className="buttons"
          onClick={props.onclick}
        >cancel</Button>
         </Grid>
         <Grid item xs={4}>
        <Button variant="contained" style={{ backgroundColor:"#F1C232",color:"black"  }}
          className="buttons"
          onClick={duplicate}
        >Duplicate</Button>
         </Grid>

      

        </Grid>
      </CardContent>
    </Card>
  );

  const Search = () => {
    const [showResults, setShowResults] = useState(false);
    const onClick = (e) => {
      e.preventDefault();
      return setShowResults((prev) => !prev);
    };
    return (
      <div>
        <p
       
         
          className="pointer"
          onClick={onClick}
          style={{
            position: "absolute",
            top:"4.55rem",
            right:"8rem",
           
            zIndex: 1000,
            color: "#222F3E",
           

          }}
        >
          {showResults ? "Hide" : "Show"}
        </p>
        {showResults ? <Results  onclick={onClick}/> : null}
      </div>
    );
  };

  const fetch = useCallback(() => {
    axios.get(`${ApiUrl}/procedures/test/${content}`).then((res) => {
      setState(() => ({ content: res.data.html }));
    });

    axios.get(`${ApiUrl}/moreInfo/${content}`).then((res) => {
  console.log("check",res.data)
      setState1({
        experiment: res.data.ProcedureName,
        lab: res.data.labtype,
        department: res.data.department,
        year: res.data.year,
        college: res.data.college,
        semester:res.data.semester,
        _id:res.data._id
      });
    });
  }, [content]);

  useEffect(() => {
    fetch();
    return () => {};
  }, [fetch]);

  const fetch1 = useCallback(() => {
    setForceUpdate(true);
  }, [content]);

  useEffect(() => {
    fetch1();
    return () => {};
  }, [fetch1]);

  const handleEditorChange = (e) => {
    //console.log("Content was updated:", e.target.getContent());
  };
  const handleSave = (e) => {
    // /moreInfo
// console.log("content here",titleRef.current.value)

    axios
      .patch(`${ApiUrl}/procedures/edit`, {
        title: titleRef.current.value ||  state1.experiment,
        html: e.target.getContent(),
        content:content,
      })
      .then((res) => {
  console.log("done phase1",res.data)
  // console.log("done phase1",titleRef.current.value,labRef.current.value)
        axios
          .patch(`${ApiUrl}/moreInfo/edit`, {
            editid:res.data._id,
            experiment: titleRef.current.value || state1.experiment,
            lab: labRef.current.value || state1.lab,
            department: departmentRef.current.value || state1.department,
            year: yearRef.current.value || state1.year,
            college: collegeRef.current.value || state1.college,
            semester: semesterRef.current.value || state1.semester,
            _id:state1._id
          })
          .then((res) => {
          
            if(res.data == "error"){
              Swal.fire({
                icon: 'error',
                title: 'Oops...',
                text: 'Something went wrong Check your internet connection',
             
              })
            }
            else{
            Swal.fire(
              'success',
              'Procedure has been updated',
              'success',
            )
           setOpen(true);
            }
          });
      });
  };


  const handleChange = (content, editor) => {
    setState({ content });
  };
  const handleSubmit = (e) => {
    e.preventDefault();
  };
  const goBack = () => {
    props.history.push("/procedure");
  };
  return (
    <div className={classes.root}>
      <ArrowBackIcon
        onClick={goBack}
        style={{
          color: "red",
          border: "1px solid black",
          borderRadius: "50%",
          background: "white",
          zIndex: 100000,
          position: "absolute",
          top: 10,
          right: 30,
        }}
      />

      <p
      className="pointer"
        type="submit"
        value="refresh"
        ref={updateRef}
        style={{
          position: "absolute",
          top:"2.05rem",
          right:"2rem",
         
          zIndex: 1000,
          color: "#222F3E",
         

        }}
        onClick={() => {
          console.log("state", state, "state1", state1);
          return fetch();
        }}
      >
        refresh<RefreshIcon />
      </p>
      <br/>
      <Snackbar open={open} autoHideDuration={6000} onClose={handleClose}>
        <Alert onClose={handleClose} severity="success">
          {message}
        </Alert>
      </Snackbar>
      <form method="PATCH" onSubmit={handleSubmit}>
        <Search />

        <Editor
          id="myTiny_Mce"
          initialValue="<p>Initial content</p>"
          apiKey="au50u78j9vjabzcr4icg4v3oknubu08ifv9rfstawlzmdobp"
          init={{
            height: "90vh",
            width:"196.9vh",
            menubar: true,
            selector: "textarea",
            external_plugins: {
              tiny_mce_wiris: `${path.join(
                __dirname,
                "../../../../node_modules/@wiris/mathtype-tinymce5/plugin.min.js"
              )}`,
            },
            plugins: [
              "advlist autolink lists link image code textpattern template",
              "charmap print preview anchor help",
              "searchreplace visualblocks code",
              "insertdatetime media table advtablesort paste wordcount save",
            ],
            toolbar: `undo redo | formatselect | bold italic | \
            alignleft aligncenter alignright | \
            bullist numlist outdent indent | help | image code table customInsertButton customDateButton template tiny_mce_wiris_formulaEditor tiny_mce_wiris_formulaEditorChemistry`,
            image_advtab: true,
            image_title: true,
            automatic_uploads: true,
            file_picker_types: "image",
            file_picker_callback: function (cb, value, meta) {
              var input = document.createElement("input");
              input.setAttribute("type", "file");
              input.setAttribute("accept", "image/*");
              input.onchange = function () {
                var file = this.files[0];

                var reader = new FileReader();
                reader.onload = function () {
                  var id = "blobid" + new Date().getTime();
                  var blobCache =
                    window.tinymce.activeEditor.editorUpload.blobCache;
                  var base64 = reader.result.split(",")[1];
                  var blobInfo = blobCache.create(id, file, base64);
                  blobCache.add(blobInfo);
                  cb(blobInfo.blobUri(), { title: file.name });
                };
                reader.readAsDataURL(file);
              };

              input.click();
            },
            setup: function (editor) {
              editor.ui.registry.addButton("customInsertButton", {
                icon: "edit-block",
                tooltip: "Insert Input Element",
                onAction: function (_) {
                  const value = nanoid(7);
                  editor.insertContent(
                    `&nbsp;<input type='text' id='value_${value}' name='value_${value}'>&nbsp;`
                  );
                },
              });

              var toTimeHtml = function (date) {
                return (
                  '<time datetime="' +
                  date.toString() +
                  '">' +
                  date.toDateString() +
                  "</time>"
                );
              };

              editor.ui.registry.addButton("customDateButton", {
                icon: "insert-time",
                tooltip: "Insert Current Date",
                disabled: true,
                onAction: function (_) {
                  editor.insertContent(toTimeHtml(new Date()));
                },
                onSetup: function (buttonApi) {
                  var editorEventCallback = function (eventApi) {
                    buttonApi.setDisabled(
                      eventApi.element.nodeName.toLowerCase() === "time"
                    );
                  };
                  editor.on("NodeChange", editorEventCallback);

                  /* onSetup should always return the unbind handlers */
                  return function (buttonApi) {
                    editor.off("NodeChange", editorEventCallback);
                  };
                },
              });
            },
            content_style:
              "body { font-family:Helvetica,Arial,sans-serif; font-size:14px }",
          }}
          value={state.content}
          onChange={handleEditorChange}
          onEditorChange={handleChange}
          onSaveContent={handleSave}
        />
       {/* <div className="watermark"></div> */}
      </form>
    </div>
  );
};

export default App;
