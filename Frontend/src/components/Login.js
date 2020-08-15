import React, { Component } from 'react';
import { Redirect } from 'react-router-dom';
import { connect } from 'react-redux';
import { login, clearAuth } from '../actions/auth';

class Login extends Component {
  constructor(props) {
    super(props);
    this.state = {
      email: '',
      password: '',
    };
  }
  //to clear the error if it comes on reload or whenever the user shifts from this page
  componentWillUnmount() {
    this.props.dispatch(clearAuth());
  }

  handleSubmitForm = (e) => {
    e.preventDefault();
    const { email, password } = this.state;
    if (email && password) {
      this.props.dispatch(login(email, password));
    }
  };
  handleEmail = (e) => {
    this.setState({
      email: e.target.value,
    });
  };
  handlePassword = (e) => {
    this.setState({
      password: e.target.value,
    });
  };
  render() {
    const { inProgress, error, isLoggedIn } = this.props.auth;

    //so that logged in user don't sees the login page
    if (isLoggedIn) {
      return <Redirect to="/" />;
    }
    return (
      <form className="login-form">
        <span className="login-signup-header">LOG IN</span>
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
          <button onClick={this.handleSubmitForm} disabled={inProgress}>
            Log In
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

export default connect(mapStateToProps)(Login);