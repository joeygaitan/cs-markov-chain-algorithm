import React, {Component} from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import './App.css'

class App extends Component {
  constructor(props){
    super(props)

    this.state = {
      quotes:[],
      stuff: 0
    }
  }

  componentDidMount = async () => {
    this.getQuotes()
  }

  getQuotes = async () => {
    //'https://markov-chain-j-g.herokuapp.com/'
    return fetch("http://127.0.0.1:5000/")
    .then((response) => {
      return response.json();
    })
    .then((myJson) => {
      this.setState({quotes: [...myJson]})
    })
  }

  render() {
    return (
      <div className='center-screen'>
        {this.state.quotes.map((element)=>{
          return <h1>{element}</h1>
        })}
      </div>
    );
  }
}

export default App;
