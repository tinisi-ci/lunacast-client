import React, { Component } from 'react';
import { BrowserRouter as Router, Route } from 'react-router-dom';
import Layout from './components/layout.js';
import Home from './components/home.js';
import AboutUs from './components/aboutUs.js';

class App extends Component {
  render() {
    return (
      <Router>
        <div>
          <Layout>
            <Route exact={true} component={Home} path="/" />
            <Route component={AboutUs} path="/about-us" />
          </Layout>
        </div>
      </Router>
    );
  }
}

export default App