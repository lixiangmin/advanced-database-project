import axios from 'axios';
import FormData from 'form-data';
import {sprintf} from 'sprintf-js';


import constants from './constants';

const BASE_URL = "http://127.0.0.1:8080";
const USER_LOGIN_PATH = BASE_URL + "/user/login";
const RECOMMEND_MOVIES = BASE_URL + "/movie/recommend/movies";
const GET_MOVIE_BY_ID = BASE_URL + "/movie/%s";
const GET_MOVIE_LIST = BASE_URL + "/movie/list";
const GET_MOVIE_LIST_BY_TEXT = BASE_URL + "/movie/searchByText";
const GET_MOVIE_LIST_BY_GENRE_ID = BASE_URL + "/movie/searchByGenreId";
const GET_MOVIE_LIST_BY_MOVIE_ID = BASE_URL + "/movie/searchByMovieId";
const GET_THE_TYPES_OF_MOVIE = BASE_URL + "/movie/getTypes";
const GET_THE_CREWS_OF_MOVIE = BASE_URL + "/movie/getCrews";
const GET_THE_CASTS_OF_MOVIE = BASE_URL + "/movie/getCasts";
const GET_MOVIES_WITH_TYPE = BASE_URL + "/genre/getMovies";
const GET_THE_RECOMMENDS_OF_MOVIE = BASE_URL + "/movie/recommend/%s";
const GET_MOVIE_TYPES = BASE_URL + "/genre";

function request(axiosOpt, dataOpt) {
    const successCb = checkCb(dataOpt.successCb);
    const failCb = checkCb(dataOpt.failCb);
    const notLoginCb = checkCb(dataOpt.notLoginCb);

    axios(axiosOpt)
        .then(resp => {
            if (resp.status !== 200 || !resp.data) {
                failCb(constants.TOAST_NET_ERR);
                return;
            }
            if (resp.data.code === constants.NOT_LOGIN_CODE) {
                notLoginCb(resp.data.msg);
                return;
            }
            if (resp.data.code !== 0) {
                failCb(resp.data.msg);
                return;
            }
            successCb(resp.data, resp);
        })
        .catch(err => {
            console.log(err);
            failCb(constants.TOAST_NET_ERR);
            return;
        });
}


function checkCb(cb) {
    return cb && typeof cb === "function" ? cb : function () {
    };
}


export function userLogin(data, opt) {
    const form = new FormData();
    form.append("username", data.username);
    request({
        method: "POST",
        url: USER_LOGIN_PATH,
        data: form
    }, opt);
}

export function recommendMovies(opt) {
    request({
        method: "GET",
        url: RECOMMEND_MOVIES,
    }, opt);
}

export function moviesWithType(params, opt) {
    request({
        method: "GET",
        url: GET_MOVIES_WITH_TYPE,
        params: params
    }, opt);
}

export function findTheTypesOfMovie(params, opt) {
    request({
        method: "GET",
        url: GET_THE_TYPES_OF_MOVIE,
        params: params
    }, opt);
}

export function findTheCrewsOfMovie(params, opt) {
    request({
        method: "GET",
        url: GET_THE_CREWS_OF_MOVIE,
        params: params
    }, opt);
}

export function findTheCastsOfMovie(params, opt) {
    request({
        method: "GET",
        url: GET_THE_CASTS_OF_MOVIE,
        params: params
    }, opt);
}

export function findTheRecommendsOfMovie(movieId, opt) {
    const path = sprintf(GET_THE_RECOMMENDS_OF_MOVIE, movieId);
    request({
        method: "GET",
        url: path
    }, opt);
}

export function movieTypes(opt) {
    request({
        method: "GET",
        url: GET_MOVIE_TYPES,
    }, opt);
}

export function findMovieById(movieId, opt) {
    const path = sprintf(GET_MOVIE_BY_ID, movieId);
    request({
        method: "GET",
        url: path
    }, opt);
}

export function findMovieList(params, opt) {
    request({
        method: "GET",
        url: GET_MOVIE_LIST,
        params: params
    }, opt);
}

export function findMovieListByText(params, opt) {
    request({
        method: "GET",
        url: GET_MOVIE_LIST_BY_TEXT,
        params: params
    }, opt);
}

export function findMovieListByGenreId(params, opt) {
    request({
        method: "GET",
        url: GET_MOVIE_LIST_BY_GENRE_ID,
        params: params
    }, opt);
}

export function findMovieListByMovieId(params, opt) {
    request({
        method: "GET",
        url: GET_MOVIE_LIST_BY_MOVIE_ID,
        params: params
    }, opt);
}



