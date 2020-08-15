import React from "react";
import { connect } from "react-redux";
import { Link } from "react-router-dom";
import { logoutUser } from "../actions/auth";

class Nav extends React.Component {
  logout = () => {
    localStorage.removeItem("token");
    this.props.dispatch(logoutUser());
  };

 

  render() {
    const { auth } = this.props;
    return (
      <div>
        {/*Navbar */}
        <nav className="nav">
          <div className="left-div">
            {/*on clicking the logo it will take to the homepage */}
            <Link to="/">
              <span className="main-logo">TEAM 69</span>
            </Link>
          </div>
          <div className="right-nav">
            {auth.isLoggedIn && (
              <div className="user">
                <span>{auth.user.name}</span>
              </div>
            )}

            <div className="nav-links">
              <ul>
                {!auth.isLoggedIn && (
                  <li>
                    <Link to="/login">LogIn</Link>
                  </li>
                )}
                {auth.isLoggedIn && <li onClick={this.logout}>Logout</li>}
                {!auth.isLoggedIn && (
                  <li>
                    <Link to="/signup">Register</Link>
                  </li>
                )}
              </ul>
            </div>
          </div>
        </nav>
      </div>
    );
  }
}

function mapStateToProps(state) {
  return {
    auth: state.auth,
  };
}

export default connect(mapStateToProps)(Nav);
