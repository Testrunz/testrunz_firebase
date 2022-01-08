import React from "react";
import { makeStyles } from "@material-ui/core/styles";
import Grid from "@material-ui/core/Grid";
import axios from "axios";
import Context from "../Context";
// import Graph from "../Graph/Graph";
import ApiUrl from "../../../ServerApi";

const useStyles = makeStyles({
  root: {
    width: "1000px",
  },
  paper: {},
});

const Record = ({ data }) => {
  // let graph;
  // if (
  //   data.experimentName === "Lee's Disc Method" ||
  //   data.experimentName === "Polarimeter"
  // ) {
  //   graph = true;
  // } else {
  //   graph = false;
  // }
  const classes = useStyles();
  const [htmlContext, setHtmlContext] = React.useState(null);
  //console.log({ ...data });
  React.useEffect(() => {
    axios
      .get(`${ApiUrl}/procedures/search/${data.experimentName}`)
      .then((res) => {
        setHtmlContext((prev) => {
          if (prev === null) return res.data;
        });
      });
  }, [data.experimentName]);
  
  return (
    <>
      <Grid container className={classes.root} spacing={2}>
        <Grid item xs={7}>
          <div className={classes.paper}>
            <h1>Record section</h1>
           
             <Context value={htmlContext} dataV={data} /> 
          </div>
        </Grid>
        {/* <Grid item xs={5}>
          <div className={classes.paper}>{graph && <Graph data={data} />}</div>
        </Grid> */}
      </Grid>
    </>
  );
};

export default Record;
