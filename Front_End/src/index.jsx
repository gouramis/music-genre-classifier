import * as ajaxRequests from './ajaxRequests.js'
import React from 'react';
import ReactDOM from 'react-dom';
import PageTwo from './pageTwo.js';

//creaate main page for our application
class MainPage extends React.Component{
  //create constructor for class that holds the page states
  constructor(props){
    super(props);

    this.state = {
      // States are hardcoded for now
      landingPage: true,
      secondPageState: false,
      songTitle: '',
      artist: '',
      predictedGenre: '',
      predictedScore: '',
      actualGenre: '',
      actualScore: '',
      modelScore: ''
    }
  }
  //create goto page state functions
  //in here setState will rerender the dom
  gotolandingPage = () =>{
    this.setState({
      landingPage: true,
      secondPageState: false,
    })
  }

  //Navigate to page two (results page) and send AJAX request to backend.
  //Search button was pushed
  gotoPageTwoState = () =>{
    this.setState({
      landingPage: false,
      secondPageState: true,
    })
    //call ajaxrequest, must wait for page to render.
    const song = this.state.songTitle
    setTimeout(function() {ajaxRequests.sbm(song, 'False'); }, 1000);
  }

  //Navigate to page two (results page) and send AJAX request to backend.
  //Feeling Lucky or Random Song button was pushed
  gotoFeelingLucky = () => {
    this.setState({
      landingPage: false,
      secondPageState: true,
    })
    
    //call ajaxrequest, must wait for page to render.
    const song = this.state.songTitle
    setTimeout(function () {ajaxRequests.sbm(song, 'True');}, 1000);
  }

  //Get the song title entered by the user from the input field
  handleTextChange = (event) =>{
    this.setState({
      songTitle: event.target.value
    })
  }

  render() {
    //first page
    if(this.state.landingPage === true){
      return (
        <main>
          <div className="pageContainer">
            <div className="boxContent">
              <div className="title">
                <div id="LandingPage">
                  Moosic Classifier
                </div>
                <div id="description">
                  music genre classifier
                </div>
              </div>
              <div id="textInput">
                <input
                  id="songInput"
                  placeholder="Enter Song Title"
                  style={{height: 40, fontSize:40}}
                  onChange={this.handleTextChange}
                />
                <div className="buttons">
                  <button id="buttonStyle" onClick={this.gotoPageTwoState}> Search </button>
                  <button id="buttonStyle" onClick={this.gotoFeelingLucky}> Feeling Lucky </button>
                </div>
              </div>
            </div>
          </div>
        </main>
      );
      //second page
    } else if(this.state.secondPageState === true) {
      return (
        <PageTwo pageState={this.gotolandingPage} parentStates={this.state} feelingLucky={this.gotoFeelingLucky}/>   
      );
    }
  }
}
ReactDOM.render(
    <MainPage />,
    document.getElementById('root')
);
