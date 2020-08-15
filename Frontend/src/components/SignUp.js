import React, { Component } from "react";
import { Redirect } from "react-router-dom";

import { connect } from "react-redux";
import { signup, clearAuth } from "../actions/auth";

class Signup extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: "",
      password: "",
      name: "",
      confirmPassword: "",
    };
  }
  //to clear the error if it comes on reload or whenever the user shifts fro this page
  componentWillUnmount() {
    this.props.dispatch(clearAuth());
  }
  handleSubmitForm = (e) => {
    e.preventDefault();
    const { email, password, confirmPassword, name } = this.state;
    if (email && confirmPassword && name && password) {
      this.props.dispatch(signup(email, password, confirmPassword, name));
    }
  };
  handleEmail = (e) => {
    this.setState({
      email: e.target.value,
    });
  };
  handleName = (e) => {
    this.setState({
      name: e.target.value,
    });
  };
  handlePassword = (e) => {
    this.setState({
      password: e.target.value,
    });
  };
  handleCPassword = (e) => {
    this.setState({
      confirmPassword: e.target.value,
    });
  };
  render() {
    const { inProgress, error, isLoggedIn } = this.props.auth;
    if (isLoggedIn) {
      return <Redirect to="/" />;
    }
    return (
      <form className="login-form">
        <span className="login-signup-header">SIGN UP</span>
        {error && <div className="alert error-dailog">{error}</div>}
        <div className="field">
          <input
            type="email"
            placeholder="Email"
            required
            onChange={this.handleEmail}
          />
        </div>
        <div className="field">
          <input
            type="password"
            placeholder="password"
            required
            onChange={this.handlePassword}
          />
        </div>
        <div className="field">
          <input
            type="text"
            placeholder="name"
            required
            onChange={this.handleName}
          />
        </div>
        <div className="field">
          <input
            type="password"
            placeholder="confirm password"
            required
            onChange={this.handleCPassword}
          />
        </div>
        <div className="field">
          <button onClick={this.handleSubmitForm} disabled={inProgress}>
            SignUp
          </button>
        </div>
      </form>
    );
  }
}
function mapStateToProps(state) {
  return {
    auth: state.auth,
  };
}

export default connect(mapStateToProps)(Signup);
