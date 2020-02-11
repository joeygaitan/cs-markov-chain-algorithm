import React, {Component} from 'react';
import { BrowserRouter,Switch,Route } from 'react-router-dom';
import './App.css'

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
    return fetch('https://markov-chain-j-g.herokuapp.com/')
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {
      console.log(myJson)
    })
  }

  render() {
     
    return (
      <div className='center-screen'>
        <h1>hello friend</h1>
      </div>
    );
  }
}

export default App;
