import './App.css';
import {
    BrowserRouter,
    Switch,
    Route,
} from "react-router-dom";
import HomePage from "./pages/home";
import LoginPage from "./pages/login";
import React from "react";
import MovieInfoPage from "./pages/movie_info";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Switch>
                    <Route path="/home" component={HomePage}/>
                    <Route path="/login" component={LoginPage}/>
                    <Route path="/movieInfo" component={MovieInfoPage}/>
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default App;
