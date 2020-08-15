import React from "react";
import { connect } from "react-redux";
import { BrowserRouter as Router, Route, Switch } from "react-router-dom";


import Page404 from "./Page404";
import Nav from "./Nav";
import Login from "./Login";
import SignUp from "./SignUp";
import Footer from "./Footer";
import * as jwtDecode from "jwt-decode";
import { authenticateUser } from '../actions/auth';


class App extends React.Component {
  componentDidMount() {
    const token = localStorage.getItem("token");

    if (token) {
      const user = jwtDecode(token);
      this.props.dispatch(
        authenticateUser({
          email: user.email,
          name: user.name,
        })
      );
      //anything that has to be fetched initially
    }
  }

  render() {
    return (
      <Router>
        <div>
          {/*Navbar */}
          <Nav />

          <Switch>
            {/*Routes*/}
           {/* <Route path="/" component={SignUp} />*/}
            <Route path="/login" component={Login} />
            <Route path="/signup" component={SignUp} />
            <Route component={Page404} />
          </Switch>



          {/*Footer */}
          <Footer />
        </div>
      </Router>
    );
  }
}

function mapStateToProps(state) {
  return {
    auth: state.auth,
  };
}

export default connect(mapStateToProps)(App);
