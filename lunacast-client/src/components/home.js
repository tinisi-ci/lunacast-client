import React, { Component } from 'react';
import './home.css';

class Home extends Component {
  render() {
    return (
      <div className="home">
        <div className="home-header">
          <h2>Welcome!</h2>
          <iframe className="video" src="https://www.youtube.com/embed/1wQRxH0jRyI?autoplay=1" allowFullScreen="allowFullScreen"></iframe>
        </div>
      </div>
    );
  }
}

export default Home;
