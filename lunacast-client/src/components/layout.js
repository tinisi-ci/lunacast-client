import React from 'react';
import { Link } from 'react-router-dom';
import './layout.css';

class Layout extends React.Component {
  render() {
    return (
      <div>
        <div className="logo">
        </div>
        <ul className="menu">
          <li className="menu-item"><Link to="/">Home</Link></li>
          <li className="menu-item"><Link to="/about-us">About</Link></li>
        </ul>
        <div>
          {this.props.children}
        </div>
      </div>
    );
  }
}

export default Layout;
