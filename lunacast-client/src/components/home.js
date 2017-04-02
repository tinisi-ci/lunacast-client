import React, { Component } from 'react';
import './home.css';

class Home extends Component {
  render() {
    return (
      <div className="home">
        <div className="home-header">
          <h2>Welcome!</h2>
          <iframe width="560" height="315" src="https://www.youtube.com/embed/1wQRxH0jRyI?autoplay=1" frameborder="0" allowfullscreen></iframe>
        </div>
      </div>
    );
  }
}

export default Home;
