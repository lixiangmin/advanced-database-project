import axios from 'axios';
import FormData from 'form-data';

import constants from './constants';

const BASE_URL = "http://127.0.0.1:8080";
const USER_LOGIN_PATH = BASE_URL + "/user/login";


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
  return cb && typeof cb === "function" ? cb : function () { };
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



