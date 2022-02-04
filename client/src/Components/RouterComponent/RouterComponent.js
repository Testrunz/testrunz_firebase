import React from "react";
import { HashRouter as Router, Route, Switch } from "react-router-dom";

import Home from "../../Home";
import ListUserComponent from "./user/ListUserComponent";
import AddUserComponent from "./user/AddUserComponent";
import EditUserComponent from "./user/EditUserComponent";
import UserDashComponent from "../DashBoard/DashBoard";
import ListProcedure from "./user/ProcedureList";
import AddProcedure from "./user/Procedure";
import EditProcedure from "./user/ProcedureEdit";

import Signup from "../../authent/Signup";
import Signin from "../../authent/Signin";
import Forgot from "../../authent/forgot";

import Sidelayout from "./user/Sidelayout"
import Private from "../../core/private";


import PrivateRoute from "../../authent/PrivateRoute";
import AdminRoute from "../../authent/AdminRoute";

import Google1 from "../../authent/Google1";
import Runz from "./user/Runz";
import Mypage from "./user/Mypage";
import Procedurelist from "./user/ProcedureList";
import User from "./user/User";

const RouterComponent = () => {
  return (
    <div>
        <Router>
          
        <Sidelayout>
          <Switch>
            <Route path="/" exact component={Home} />
            <Route path="/signup" exact component={Signup} />
            {/* <Route path="/signin" exact component={Signin} /> */}
            <Route path="/signin" exact component={Signin} />
            <Route path="/Google1" exact component={Google1} /> 
            <Route path="/forgot_password" component={Forgot} />
            <PrivateRoute path="/private" exact component={Private} />
            <PrivateRoute path="/runz" exact component={Runz} /> 
            <PrivateRoute path="/app" exact component={Mypage} /> 
            <PrivateRoute path="/procedure" exact component={Procedurelist} /> 
            <PrivateRoute path="/profile" exact component={User} /> 
            <PrivateRoute path="/add-user" exact component={AddUserComponent} />
            <PrivateRoute
              path="/edit-user"
              exact
              component={EditUserComponent}
            />
            <PrivateRoute
              path="/userdash/:token"
              component={UserDashComponent}
            />
            <PrivateRoute path="/listProce" exact component={ListProcedure} />
            <PrivateRoute path="/addProce" exact component={AddProcedure} />
            <PrivateRoute
              path="/editProce/:id"
              exact
              component={EditProcedure}
            />
          </Switch>
          </Sidelayout>
        </Router>
    </div>
  );
};

export default RouterComponent;
