import React, {Component} from 'react';
import { BrowserRouter,Switch,Route } from 'react-router-dom';
import './App.css';

class App extends Component {
  constructor(props){
    super(props)

    this.state = {
      quotes:[]
    }
  }

  componentDidMount = async () => {
    this.getQuotes()
  }

  getQuotes = async () => {
    return fetch('http://localhost:5000')
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {
      console.log(myJson)
    })
  }

  render() {
     
    return (
      <div>
        <h1>hello</h1>
      </div>
    );
  }
}

export default App;
