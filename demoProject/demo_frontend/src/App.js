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
import SearchPage from "./pages/search";

function App() {
    return (
        <div className="App">
            <BrowserRouter>
                <Switch>
                    <Route path="/" exact component={LoginPage}/>
                    <Route path="/home" component={HomePage}/>
                    <Route path="/login" component={LoginPage}/>
                    <Route path="/movieInfo/:id" component={MovieInfoPage}/>
                    <Route path="/search" component={SearchPage}/>
                </Switch>
            </BrowserRouter>
        </div>
    );
}

export default App;
